#include<iostream>
#include<vector>
#include<string>
#include<fstream>
using namespace std;

int main()
{
	int testCases;
	ofstream outfile( "output.txt" );
	ifstream infile( "A-small-attempt0.in" );
	string pancakes;
	int flag = 1;
	int flipFlag = 0;
	int counter = 0;
	unsigned k = 0;
	

	infile >> testCases;

	for( int i = 0; i < testCases; i++ )
	{
		flag = 1;
		flipFlag = 0;
		infile >> pancakes;	// retrieve string
		cout << "Case #" << i + 1 << ": " << pancakes << endl;
		while( flag != 0 )
		{
			flag = 0;
			flipFlag = 0;
			while( pancakes[ k ] != '+' && k < pancakes.size() )
			{
				pancakes[ k ] = '+';	// flip first pancakes
				flipFlag = 1;
				k++;
			}
			k = 0;
			if( flipFlag == 1 )
				counter++;
			flipFlag = 0;
			for( unsigned j = 0; j < pancakes.size(); j++ )
			{
				if( pancakes[ j ] == '-' )
					flag = 1;
			}

			if( flag == 1 )
			{
				while( pancakes[ k ] != '-' && k < pancakes.size() )
				{
					pancakes[ k ] = '-';
					flipFlag = 1;
					k++;
				}
				k = 0;
				if( flipFlag == 1 )
					counter++;
				flipFlag = 0;
				for( unsigned j = 0; j < pancakes.size(); j++ )
				{
					if( pancakes[ j ] == '-' )
						flag = 1;
				}
			} 
		}
		outfile << "Case #" << i + 1 << ": " << counter << endl;
		counter = 0;
	} // end for
	infile.close();
	outfile.close();
	return 0;
}