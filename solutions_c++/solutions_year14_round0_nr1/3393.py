#include <iostream>
#include <fstream>
#include <math.h>
#include <stdlib.h>

using namespace std;

bool doesCardMatch( unsigned int card_to_search, unsigned int card1, unsigned int card2, unsigned int card3, unsigned int card4 )
{
	return card_to_search == card1 || card_to_search == card2 || card_to_search == card3 || card_to_search == card4;
}

int main( int argc, char* argv[] )
{
	ifstream filereader;
	filereader.open( "A-small-attempt0.in" );
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
			unsigned int answer, temp, fitting_cards = 0, card = 0;
			unsigned int cards[4];

			filereader.getline( output, 64 );
			answer = atoi( output );

			for( unsigned int row = 1; row <= 4; ++row )
			{
				if( row == answer )
				{
					filereader.getline( output, 64, ' ' );
					cards[0] = atoi( output );
					filereader.getline( output, 64, ' ' );
					cards[1] = atoi( output );
					filereader.getline( output, 64, ' ' );
					cards[2] = atoi( output );
					filereader.getline( output, 64 );
					cards[3] = atoi( output );
				}
				else
				{
					filereader.getline( output, 64 );
				}
			}

			filereader.getline( output, 64 );
			answer = atoi( output );

			for( unsigned int row = 1; row <= 4; ++row )
			{
				if( row == answer )
				{
					filereader.getline( output, 64, ' ' );
					temp = atoi( output );
					if( doesCardMatch( temp, cards[0], cards[1], cards[2], cards[3] ) )
					{
						++fitting_cards;
						card = temp;
					}

					filereader.getline( output, 64, ' ' );
					temp = atoi( output );
					if( doesCardMatch( temp, cards[0], cards[1], cards[2], cards[3] ) )
					{
						++fitting_cards;
						card = temp;
					}

					filereader.getline( output, 64, ' ' );
					temp = atoi( output );
					if( doesCardMatch( temp, cards[0], cards[1], cards[2], cards[3] ) )
					{
						++fitting_cards;
						card = temp;
					}

					filereader.getline( output, 64 );
					temp = atoi( output );
					if( doesCardMatch( temp, cards[0], cards[1], cards[2], cards[3] ) )
					{
						++fitting_cards;
						card = temp;
					}
				}
				else
				{
					filereader.getline( output, 64 );
				}
			}

			filewriter << "Case #" << currentcase << ": ";
			switch( fitting_cards )
			{
			case 0:
				filewriter << "Volunteer cheated!";
				break;
			case 1:
				filewriter << card;
				break;
			default:
				filewriter << "Bad magician!";
				break;
			}
			filewriter << endl;
		}
	}
	filereader.close();
	filewriter.close();

	return 0;
}