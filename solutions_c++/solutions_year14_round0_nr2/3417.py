#include <iostream>
#include <fstream>
#include <math.h>
#include <stdlib.h>
#include <iomanip>

using namespace std;

bool doesCardMatch( unsigned int card_to_search, unsigned int card1, unsigned int card2, unsigned int card3, unsigned int card4 )
{
	return card_to_search == card1 || card_to_search == card2 || card_to_search == card3 || card_to_search == card4;
}

int main( int argc, char* argv[] )
{
	ifstream filereader;
	filereader.open( "B-large.in" );
	char output[64];

	ofstream filewriter;
	filewriter.open( "problem_b_large_result.txt" );

	unsigned int testcases = 0;
	unsigned int currentcase = 0;

	if( filereader.is_open() )
	{
		filereader.getline( output, 64 );
		testcases = atoi( output );

		for( currentcase = 1; currentcase <= testcases; ++ currentcase )
		{
			double c, f, x, rate, min_time, time;
			unsigned int farms = 0;

			filereader.getline( output, 64, ' ' );
			c = atof( output );
			filereader.getline( output, 64, ' ' );
			f = atof( output );
			filereader.getline( output, 64 );
			x = atof( output );

			min_time = DBL_MAX;
			time = DBL_MAX;

			while( time == min_time )
			{
				time = 0.0;
				rate = 2.0;

				for( unsigned int i = 0; i < farms; ++i )
				{
					time += c / rate;
					rate += f;
				}

				time += x / rate;
				if( time < min_time )
					min_time = time;

				++farms;
			}

			filewriter << "Case #" << currentcase << ": " << std::setprecision( 7 ) << std::fixed << min_time << endl;
		}
	}
	filereader.close();
	filewriter.close();

	return 0;
}