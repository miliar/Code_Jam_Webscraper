#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <fstream>
#include <cstdlib>

using namespace std;

class Token
{
public:
	char c;

	Token( char c )
	{
		this->c = c;
	}

	Token()
	{
		c = '1';
	}
};

class BoardData
{
    Token tokens[4][4];

public:
    void addTokenLine( string data, int numLine )
    {
        tokens[numLine][0] = Token( data[0] );
        tokens[numLine][1] = Token( data[1] );
        tokens[numLine][2] = Token( data[2] );
        tokens[numLine][3] = Token( data[3] );
    }

    void print()
    {
        for( int i = 0; i < 4; ++i )
        {
            for( int j = 0; j < 4; ++j )
                printf( "%c", tokens[i][j].c );
            printf( "\n" );
        }
    }

    char getResult()
    {
    	bool completed = true;
// horizontal
		for( int i = 0; i < 4; ++i )
		{
			char first = tokens[i][0].c;
			if( first == '.' )
			{
				completed = false;
				continue;
			}

			char second = tokens[i][1].c;
			if( second == '.' )
			{
				completed = false;
				continue;
			}

			char third = tokens[i][2].c;
			if( third == '.' )
			{
				completed = false;
				continue;
			}

			char fourth = tokens[i][3].c;
			if( fourth == '.' )
			{
				completed = false;
				continue;
			}

			first = first == 'T' ? second : first;
			second = second == 'T' ? first : second;
			third = third == 'T' ? first : third;
			fourth = fourth == 'T' ? first : fourth;

			if( ( first == second ) && ( first == third ) && ( first == fourth ) )
			{
				return first;
			}
		}
//vertical
		for( int i = 0; i < 4; ++i )
		{
			char first = tokens[0][i].c;
			if( first == '.' )
			{
				completed = false;
				continue;
			}

			char second = tokens[1][i].c;
			if( second == '.' )
			{
				completed = false;
				continue;
			}

			char third = tokens[2][i].c;
			if( third == '.' )
			{
				completed = false;
				continue;
			}

			char fourth = tokens[3][i].c;
			if( fourth == '.' )
			{
				completed = false;
				continue;
			}

			first = first == 'T' ? second : first;
			second = second == 'T' ? first : second;
			third = third == 'T' ? first : third;
			fourth = fourth == 'T' ? first : fourth;

			if( ( first == second ) && ( first == third ) && ( first == fourth ) )
			{
				return first;
			}
		}

		//topleft to bottomright
		for( int i = 0; i < 1; ++ i )
		{
			char first = tokens[0][0].c;
			if( first == '.' )
			{
				completed = false;
				continue;
			}

			char second = tokens[1][1].c;
			if( second == '.' )
			{
				completed = false;
				continue;
			}

			char third = tokens[2][2].c;
			if( third == '.' )
			{
				completed = false;
				continue;
			}

			char fourth = tokens[3][3].c;
			if( fourth == '.' )
			{
				completed = false;
				continue;
			}

			first = first == 'T' ? second : first;
			second = second == 'T' ? first : second;
			third = third == 'T' ? first : third;
			fourth = fourth == 'T' ? first : fourth;

			if( ( first == second ) && ( first == third ) && ( first == fourth ) )
			{
				return first;
			}
		}

		//topright to bottomleft
		for( int i = 0; i < 1; ++ i )
		{
			char first = tokens[0][3].c;
			if( first == '.' )
			{
				completed = false;
				continue;
			}

			char second = tokens[1][2].c;
			if( second == '.' )
			{
				completed = false;
				continue;
			}

			char third = tokens[2][1].c;
			if( third == '.' )
			{
				completed = false;
				continue;
			}

			char fourth = tokens[3][0].c;
			if( fourth == '.' )
			{
				completed = false;
				continue;
			}

			first = first == 'T' ? second : first;
			second = second == 'T' ? first : second;
			third = third == 'T' ? first : third;
			fourth = fourth == 'T' ? first : fourth;

			if( ( first == second ) && ( first == third ) && ( first == fourth ) )
			{
				return first;
			}
		}

		if( completed )
			return 'D';
    	return 'F';
    }

    string getStatus()
    {
    	char result = getResult();
        switch( result )
        {
		case 'O':
			return "O won";
		case 'X':
			return "X won";
		case 'D':
			return "Draw";
		default:
			return "Game has not completed";
        }
    }
};

int main()
{
    FILE* inFp = fopen( "./in.txt", "r" );
    FILE* outFp = fopen( "./out.txt", "w" );
    char fileBuffer[256];

    BoardData boardData;

    fgets( fileBuffer, 255, inFp );
    int numCase = atoi( fileBuffer );

	for( int j = 1; j <= numCase; ++j )
	{
		for( int i = 0; i < 4; ++i )
		{
			fgets( fileBuffer, 255, inFp );
			boardData.addTokenLine( fileBuffer, i );
		}

		printf( "Case #%d: %s\n", j, boardData.getStatus().c_str() );
		fprintf( outFp, "Case #%d: %s\n", j, boardData.getStatus().c_str() );
		fgets( fileBuffer, 255, inFp );
	}

    fclose( inFp );
    fclose( outFp );
    return 0;
}
