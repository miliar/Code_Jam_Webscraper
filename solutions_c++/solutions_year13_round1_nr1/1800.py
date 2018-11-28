#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

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
			int r, t, rings;
			filereader.getline( output, 64, ' ' );
			r = atoi( output );
			
			filereader.getline( output, 64 );
			t = atoi( output );
			rings = 0;

			while( t > 0 )
			{
				int whitearea = r * r;
				++r;
				int blackarea = ( r * r ) - whitearea;
				++r;
				if( blackarea <= t )
				{
					++rings;
				}
				t -= blackarea;
			}
			
			filewriter << "Case #" << currentcase << ": " << rings << endl;
		}
	}
	filereader.close();
	filewriter.close();

	return 0;
}