#include <iostream>
#include <fstream>
#include <stdio.h>
#include <algorithm>

using namespace std;

ifstream fin("file2.in");
ofstream fout("file2.out");

long long T, a, b, c;
long long sol;

int main()
{
	fin >> T;
	
	for (int t=1; t<=T; t++)
	{
		sol = 0;
		fin >> a >> b >> c;
		
		for (long long i=0; i<a; i++)
			for (long long j=0; j<b; j++)
				if ((i&j)<c)
					sol++;
		
		fout << "Case #" << t << ": " << sol << "\n";
	}
	
	return 0;
}
