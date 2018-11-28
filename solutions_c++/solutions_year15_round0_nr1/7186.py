#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

int main()
{
	ifstream infile( "A-large.in", ios::in );
	ofstream outfile( "A-output.out", ios::out );
	int T; 
	infile >> T;
	for (int t = 1; t <= T; t++)
	{
		int smax, sum = 0, fr = 0;
		char s[10005];
		infile >> smax >> s;
		for (int i = 0; i <= smax; i++)
		{
			if (fr >= i)
			{
				fr = fr + s[i] - '0';
			}
			else
			{
				sum = sum + i - fr;
				fr = s[i] - '0' + i;
			}
		}
		outfile << "Case #"  << t << ": " << sum << endl;
	}
	return 0;
} 
