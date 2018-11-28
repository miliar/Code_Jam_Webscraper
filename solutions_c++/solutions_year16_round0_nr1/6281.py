#include<iostream>
#include<vector>
#include<fstream>
using namespace std;

int main()
{
	int testCases;
	int startingNum;
	int startingNumCopy;
	vector<int> nums;
	vector<int> numsCopy;
	int flag = 1;
	int counter = 0;
	ofstream outfile( "output.txt" );
	ifstream infile( "A-small-attempt0.in" );

	infile >> testCases;

	for( int i = 0; i < 10; i++ ) // set up vector
	{
		nums.push_back( 0 );
	}

	for( int i = 0; i < testCases; i++ ) // number of test cases
	{
		infile >> startingNum;
		startingNumCopy = startingNum;
		numsCopy = nums;
		counter = 0;
		if( startingNum == 0 )
			outfile << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
		else
		{
			while( flag != 0 )
			{
				counter++;
				flag = 0;
				startingNumCopy = startingNum * counter;
				while( startingNumCopy != 0 )
				{
					numsCopy[ startingNumCopy % 10 ]++;
					startingNumCopy /= 10;
				} // end while
				for( int i = 0; i < 10; i++ )
				{
					if( numsCopy[ i ] < 1 )
						flag = 1;
				} // end for
				if( flag == 0 )
					outfile << "Case #" << i + 1 << ": " << counter * startingNum << endl;
			}	// end while
		}	// end else
		flag = 1;
	}	// end for
	outfile.close();
	infile.close();
	return 0;
}