#include <iostream>
#include <fstream>
#include <math.h>
#include <stdlib.h>
#include <string>

using namespace std;

int main( int argc, char* argv[] )
{
	ifstream filereader;
	filereader.open( "B-large.in" );
	char output[128];

	ofstream filewriter;
	filewriter.open( "problem_b_result.txt" );

	unsigned int testcases = 0;
	unsigned int currentcase = 0;

	if( filereader.is_open() )
	{
		filereader.getline( output, 128 );
		testcases = atoi( output );

		unsigned int start, answer;
		bool done;
		std::string sequence;

		for( currentcase = 1; currentcase <= testcases; ++currentcase )
		{
			filereader.getline( output, 128 );
			sequence = output;
			char previous = ' ';
			answer = 0;

			for( const auto &it : sequence )
			{
				if( it != previous )
				{
					if( previous != ' ' )
						++answer;
					previous = it;
				}
			}

			if( previous == '-' )
				++answer;

			filewriter << "Case #" << currentcase << ": ";
			filewriter << answer;
			filewriter << endl;
		}
	}
	filereader.close();
	filewriter.close();

	return 0;
}