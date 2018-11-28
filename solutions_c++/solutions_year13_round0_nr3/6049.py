// Google Jam qualifying round (B)
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
struct tInputEntry {
	public:
		double rangeMin;
		double rangeMax;

		inline tInputEntry()		{}
		inline ~tInputEntry()		{}
};

void initSolver() {
}

bool readFileEntry( tInputEntry &outEntry, FILE* pInputFile ) {
	if( fscanf( pInputFile, "%lf %lf", &outEntry.rangeMin, &outEntry.rangeMax ) < 2 ) {
		printf( "Could read the float range properly" );
		return false;
	}

	return true;
}

bool isPalindrome( double val ) {
	assert( val >= 1 );

	static const int VALUESTRING_SIZE_MAX = 128;

	char valueString[ VALUESTRING_SIZE_MAX ];
	sprintf( valueString, "%.0lf", val );

	int valueStringLength = strlen( valueString );
	assert( valueStringLength < VALUESTRING_SIZE_MAX );

	// Check for the palindrome condition...
	int searchMax = static_cast<int>( ceil( valueStringLength / 2.0 ) );
	for( int searchIndex = 0; searchIndex < searchMax; ++searchIndex ) {
		if( valueString[searchIndex] != valueString[valueStringLength - searchIndex - 1] )
			return false;
	}

	return true;
}

double getInc( double value ) {

	// Modify the increment so that it's within the double significand range...
	int valueExp;
	frexp( value, &valueExp );

	if( valueExp < 53 )
		return 1.0;

	return pow( 2, static_cast<double>(valueExp - 53) );
}

void processEntry( tInputEntry &entry, FILE* pOutFile ) {
	printf( "Processing range: %.0lf - %.0lf\n", entry.rangeMin, entry.rangeMax );

	// Find the range's minimum square root
	double rootMin = ceil( sqrt( entry.rangeMin ) );
	double rootMax = floor( sqrt( entry.rangeMax ) );
	
	int solutions = 0;
	for( double root = rootMin; root <= rootMax; root += getInc(root) ) {
		if( isPalindrome(root) && isPalindrome(root*root) ) {
			printf( "Found fair and square: %.0lf (%.0lf)\n", root*root, root );
			++solutions;
		}
	}

	fprintf( pOutFile, "%d", solutions );
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

