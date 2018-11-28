// Google Jam Qualifying Round
//

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include <string.h>
#include <assert.h>
#include <vector>
#include <algorithm>

using namespace std;

// Problem implementation
// ------------------------------------
static const int			ROWS				= 4;
static const int			COLS				= 4;
static const int			STATEBITS_SIZE		= 2;
static const unsigned long	STATEBITS_MASK		= (0x1 << STATEBITS_SIZE) - 1;
static const int			WINPATTERN_LENGTH	= 4;

enum STATEBITS {
	STATEBIT_EMPTY	= 0x0,
	STATEBIT_X		= 0x1,
	STATEBIT_O		= 0x2,
};

struct tInputEntry {
	public:
		unsigned long boardState;

		inline tInputEntry()		{}
		inline ~tInputEntry()		{}
};

struct tPos {
	int row;
	int col;
};

struct tWinCondition {
	unsigned long	testBits;
	const char*		pWinner;
};

typedef vector<tWinCondition> tWinConditionList;

static const tPos WINPATTERNS[][WINPATTERN_LENGTH] = {
	// Four in a row
	{	{0,0}, {0,1}, {0,2}, {0,3}	},
	{	{1,0}, {1,1}, {1,2}, {1,3}	},
	{	{2,0}, {2,1}, {2,2}, {2,3}	},
	{	{3,0}, {3,1}, {3,2}, {3,3}	},

	// Four in a column
	{	{0,0}, {1,0}, {2,0}, {3,0}	},
	{	{0,1}, {1,1}, {2,1}, {3,1}	},
	{	{0,2}, {1,2}, {2,2}, {3,2}	},
	{	{0,3}, {1,3}, {2,3}, {3,3}	},

	// Diagonals
	{	{0,0}, {1,1}, {2,2}, {3,3}	},
	{	{0,3}, {1,2}, {2,1}, {3,0}	},
};

static const int WINPATTERNS_NUM = sizeof( WINPATTERNS ) / (WINPATTERN_LENGTH * sizeof(tPos));



static tWinConditionList winningEntries;

unsigned long createBoardState( unsigned int bits, const tPos* posList, int posListSize ) {

	unsigned long boardState = 0;
	for( int posIndex = 0; posIndex < posListSize; ++posIndex, ++posList ) {
		int shiftCount = ( (posList->row * COLS) + posList->col ) * STATEBITS_SIZE;
		boardState |= (bits << shiftCount);
	}

	return boardState;
}

void addUserWinPatterns( const char *pWinner, unsigned int winnerBits ) {
	tWinCondition winConditionCurr;
	winConditionCurr.pWinner = pWinner;
	for( int pattern = 0; pattern < WINPATTERNS_NUM; ++pattern ) {
		winConditionCurr.testBits = createBoardState( winnerBits, WINPATTERNS[ pattern ], WINPATTERN_LENGTH );

		winningEntries.push_back( winConditionCurr );
	}
}

void initSolver() {
	// Build the win patterns 
	addUserWinPatterns( "X", STATEBIT_X );
	addUserWinPatterns( "O", STATEBIT_O );
}

bool readFileEntry( tInputEntry &outEntry, FILE* pInputFile ) {
	static const int READBUFFER_SIZE = 256;
	char readBuffer[ READBUFFER_SIZE ];

	unsigned long	boardState	= 0;
	int				bitShift	= 0;
	for( int row = 0; row < ROWS; ++row ) {
		fscanf( pInputFile, "%s", readBuffer );
		assert( strlen(readBuffer) < READBUFFER_SIZE );

		for( int col = 0; col < COLS; ++col ) {
			int bits = 0;
			switch( readBuffer[col] ) {
				case 'X':
					bits = STATEBIT_X;
					break;
				case 'O':
					bits = STATEBIT_O;
					break;
				case 'T':
					bits = STATEBIT_X | STATEBIT_O;
					break;

				default:
					break;
			}

			boardState	|= bits << bitShift;
			bitShift	+= STATEBITS_SIZE;
		}
	}

	outEntry.boardState = boardState;

	return true;
}

void processEntry( tInputEntry &entry, FILE* pOutFile ) {
	// Check for the win conditions...
	for (tWinConditionList::iterator it = winningEntries.begin() ; it != winningEntries.end(); ++it) {
		tWinCondition &windCondition = *it;

		if( (entry.boardState & windCondition.testBits) == windCondition.testBits ) {
			fprintf( pOutFile, "%s won", windCondition.pWinner );
			return;
		}
	}
    
	// Check for the incomplete condition...
	unsigned long boardBits = entry.boardState;
	for( int posIndex = 0; posIndex < (ROWS * COLS); ++posIndex ) {
		if( (boardBits & STATEBITS_MASK) == 0 ) {
			fprintf( pOutFile, "Game has not completed" );
			return;
		}

		boardBits >>= STATEBITS_SIZE;
	}

	fprintf( pOutFile, "Draw" );
}

// Framework
// ------------------------------------
enum ARG {
	ARG_EXECUTABLE		= 0,

	ARG_FILENAME_INPUT,

	ARG_NUM
};

class FileHandle {
	private: 
		FILE* mHandle;

	public:
		FileHandle( FILE* handle = NULL )	{ mHandle = handle;							}
		~FileHandle()						{ if( mHandle != NULL ) fclose( mHandle );	}

		FILE* operator=(FILE* handle )		{ mHandle = handle;	return handle;			}
		FILE* operator*()					{ return mHandle;							}
};

int processInputFile( const char* pFileName ) {
	static const char*	FILENAME_OUTPUT			= "results.out";
	static const int	RESULTSBUFFER_SIZE		= 256;

	FileHandle inputFileHandle = fopen( pFileName, "r" );
	if( !(*inputFileHandle) ) {
		printf( "Error opening input file '%s'.\n", pFileName );
		return -1;
	}

	FileHandle outputFileHandle = fopen( FILENAME_OUTPUT, "w+" );
	if( !(*outputFileHandle) ) {
		printf( "Error opening output file '%s'.\n", FILENAME_OUTPUT );
		return -1;
	}

	initSolver();

	int casesNum;
	if( fscanf( *inputFileHandle, "%d", &casesNum ) < 1 ) {
		printf( "Could not identify the number of test cases.\n");
		return -1;
	}

	for( int caseIndex = 0; caseIndex < casesNum; ++caseIndex ) {
		tInputEntry entry;
		if( !readFileEntry(entry, *inputFileHandle) )
			return -1;

		fprintf( *outputFileHandle, "Case #%d: ", caseIndex + 1 );
		processEntry( entry, *outputFileHandle );
		fprintf( *outputFileHandle, "\n" );
	}

	return casesNum;
}

// Entry function
int main(int argc, const char* argv[])
{
	if( argc < ARG_NUM ) {
		printf( "Program expects %d arguments.\n", ARG_NUM - 1 );
		return 0;
	}

	clock_t startTime	= clock();
	int		testCases	= processInputFile( argv[ARG_FILENAME_INPUT] );
	float	elapsedTime = static_cast<float>(clock() - startTime) / CLOCKS_PER_SEC;
	bool	success		= (testCases > 0);

	printf( "     Input: %s\n", argv[ARG_FILENAME_INPUT] );
	printf( "    Status: %s\n", (success ? "SUCCESS!" : "FAILED") );
	printf( "Test cases: %d\n", testCases );
	printf( "      Time: %.3f\n", elapsedTime );

	return (success ? 0 : -1);
}

