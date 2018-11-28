#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
	int i, j;
	int t, n;
	long long total, needed;
	string s;
	ifstream fin("A-large.in");
	fin >> t;
	for(i=0; i<t; i++)
	{
		fin >> n >> s;
		total = 0;
		needed = 0;
		for(j=0; j<=n; j++)
		{
			int c = s[j]-'0';
			if(c==0)
				continue;
			if(j>total)
			{
				needed += j-total;
				total += j-total;
			}
			total += c;
		}
		cout<< "Case #" << i+1 << ": " << needed << "\n";
	}
	return 0;
}