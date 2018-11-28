#include <iostream>
#include <fstream>
#include <math.h>
#include <stdlib.h>

using namespace std;

int main( int argc, char* argv[] )
{
	ifstream filereader;
	filereader.open( "A-large.in" );
	char output[64];

	ofstream filewriter;
	filewriter.open( "problem_a_result.txt" );

	unsigned int testcases = 0;
	unsigned int currentcase = 0;

	if( filereader.is_open() )
	{
		filereader.getline( output, 64 );
		testcases = atoi( output );

		for( currentcase = 1; currentcase <= testcases; ++ currentcase )
		{
			unsigned int answer, temp, total, s;

			filereader.getline( output, 64, ' ' );
			s = atoi( output );

			temp = 0;
			total = 0;
			answer = 0;
			for( unsigned int i = 0; i <= s; ++i )
			{
				char p;
				filereader.get(p);
				temp = p - '0';
				total += temp;

				if (total < i + 1)
				{
					++answer;
					++total;
				}
			}

			filewriter << "Case #" << currentcase << ": ";
			filewriter << answer;
			filewriter << endl;
		}
	}
	filereader.close();
	filewriter.close();

	return 0;
}