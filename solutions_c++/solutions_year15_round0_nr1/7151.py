#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main()
{
	ifstream infile( "A-large.in", ios::in );
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
	infile.close();
	outfile.close(); 
	return 0;
}
