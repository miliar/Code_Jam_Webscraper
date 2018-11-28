#include <iostream>
#include <fstream>
#include <math.h>
#include <stdlib.h>
#include <string>

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

		unsigned int start, current;
		bool done;
		std::string number, answer;
		bool test[10];

		for( currentcase = 1; currentcase <= testcases; ++ currentcase )
		{
			done = false;
			for (unsigned int i = 0; i < 10; ++i)
				test[i] = false;

			filereader.getline( output, 64 );
			number = output;
			start = std::stoi( number );
			current = start;

			if( start != 0 )
			{
				while( !done )
				{
					for( const auto &it : number )
					{
						test[it - '0'] = true;
					}

					done = true;
					for( unsigned int i = 0; i < 10; ++i )
						if( test[i] == false )
							done = false;

					if( done )
					{
						answer = number;
					}
					else
					{
						current += start;
						number = std::to_string( current );
					}
				}
			}
			else
			{
				answer = "INSOMNIA";
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