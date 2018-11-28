#include <iostream>
#include <fstream>
#include <math.h>
#include <stdlib.h>
#include <vector>
#include <list>
#include <algorithm>

using namespace std;

#define SMALL_DIFFERENCE 0.00000001;

double getChosenBlockByKen( double chosenByNaomi, std::list<double> &ken )
{
	std::list<double>::iterator iter = ken.begin();
	while( iter != ken.end() && *iter < chosenByNaomi )
	{
		++iter;
	}

	if( iter == ken.end() )
		iter = ken.begin();

	double chosenByKen = *iter;
	ken.remove( chosenByKen );
	return chosenByKen;
}

unsigned int calcuteDeceitfullWarWins( unsigned int blocks, std::list<double> naomi, std::list<double> ken )
{
	unsigned int wins = 0;
	double chosenByNaomi, declaredByNaomi, chosenByKen, temp;

	for( unsigned int i = 0; i < blocks; ++i )
	{
		chosenByNaomi = naomi.front();
		naomi.remove( chosenByNaomi );

		if( chosenByNaomi < ken.front() )
		{
			declaredByNaomi = ken.back() - SMALL_DIFFERENCE;
		}
		else
		{
			declaredByNaomi = ken.back() + SMALL_DIFFERENCE;
		}

		chosenByKen = getChosenBlockByKen( declaredByNaomi, ken );

		if( chosenByNaomi > chosenByKen )
			++wins;
	}

	return wins;
}

unsigned int calcuteWarWins( unsigned int blocks, std::list<double> naomi, std::list<double> ken )
{
	unsigned int wins = 0;
	double chosenByNaomi, chosenByKen;

	for( unsigned int i = 0; i < blocks; ++i )
	{
		chosenByNaomi = naomi.back();
		naomi.remove( chosenByNaomi );

		chosenByKen = getChosenBlockByKen( chosenByNaomi, ken );

		if( chosenByNaomi > chosenByKen )
			++wins;
	}

	return wins;
}

int main( int argc, char* argv[] )
{
	ifstream filereader;
	filereader.open( "D-large.in" );
	char output[64];

	ofstream filewriter;
	filewriter.open( "problem_d_large_result.txt" );

	unsigned int testcases = 0;
	unsigned int currentcase = 0;

	if( filereader.is_open() )
	{
		filereader.getline( output, 64 );
		testcases = atoi( output );

		for( currentcase = 1; currentcase <= testcases; ++ currentcase )
		{
			unsigned int blocks = 0;
			std::list<double> naomi;
			std::list<double> ken;
			unsigned int wins_dw = 0, wins_w = 0;
			
			filereader.getline( output, 64 );
			blocks = atoi( output );

			for( unsigned int i = 0; i < blocks; ++i )
			{
				if( i + 1 == blocks )
					filereader.getline( output, 64 );
				else
					filereader.getline( output, 64, ' ' );

				naomi.push_back( atof( output ) );
			}

			for( unsigned int i = 0; i < blocks; ++i )
			{
				if( i + 1 == blocks )
					filereader.getline( output, 64 );
				else
					filereader.getline( output, 64, ' ' );

				ken.push_back( atof( output ) );
			}

			naomi.sort();
			ken.sort();

			wins_dw = calcuteDeceitfullWarWins( blocks, naomi, ken );
			wins_w = calcuteWarWins( blocks, naomi, ken );

			filewriter << "Case #" << currentcase << ": " << wins_dw << " " << wins_w << endl;
		}
	}
	filereader.close();
	filewriter.close();

	return 0;
}