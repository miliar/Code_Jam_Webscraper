#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main()
{
	ifstream infile( "A-small-attempt9.in", ios::in );
	ofstream outfile( "A-output.out", ios::out );
	int t;
	infile >> t;
	for ( int i = 1; i <= t; i++ )
	{
		int Smax;
		string s;
		infile >> Smax >> s;
		int count = 0, add = 0;
		for ( int j = 0; j <= Smax; j++ )
		{
			if ( count >= j )
			{
				count += s[ j ] - '0';
			}
			else
			{
				add += j - count;
				count += s[ j ] - '0' + j - count;
			}
		}
		outfile << "Case #" << i << ": " << add << endl;
	}
	return 0;
}
