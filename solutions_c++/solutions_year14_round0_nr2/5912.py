#include <fstream>
#include <vector>
#include <iostream>
#include <stdio.h>

using namespace std;

ifstream in;
//ofstream out;
FILE *out;

int numFarms;
//double numCookies;
double C, F, X;
double payoffTime;

double getNumCookies( double time )
{
	return 0;
};

double getIncome( int nFarms )
{
	return 2 + ( ( double ) nFarms ) * F;
};

int main( int argc, char **argv )
{
	in.open( "B_in.txt" );
	//out.open( "B_out.txt" );
	out = fopen( "B_out.txt", "w" );
	
	if ( !in.is_open() )
	{
		cout << "Error: input file not found!" << endl;
		return -1;
	}
	
	if ( out == NULL )
	{
		cout << "Error: output file could not be opened!" << endl;
		in.close();
		return -1;
	}
	
	int nTests;
	in >> nTests;
	
	
	for ( int i = 0; i < nTests; ++i )
	{
		numFarms = 0;
		//numCookies = 0;
		in >> C;
		in >> F;
		in >> X;
		payoffTime = C / F;
		double currentTime = 0.0;
		
		while ( true )
		{
			// advance to next time we have enough for a farm
			currentTime += C / getIncome( numFarms );
			// now we have F cookies.
			
			double timeFarm = X / getIncome( numFarms + 1 );
			double timeNoFarm = (X - C) / getIncome( numFarms );
			
			if ( timeFarm > timeNoFarm )
			{
				// then we escape!
				//out << "Case #" << i + 1 << ": " << timeNoFarm + currentTime << endl;
				fprintf( out, "Case #%d: %0.7f\n", i + 1, timeNoFarm + currentTime );
				break;
			}
			else
			{
				// Buy another farm, continue accruing cookies
				numFarms++;
			}
		}
		
	}
	
	in.close();
	fclose( out );
	return 0;
};