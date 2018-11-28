#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <fstream>
using namespace std;

ifstream fin("A.in");
ofstream fout("A.out");

int main()
{
	int testcases;
	fin >> testcases;
	for (int testcase = 1; testcase <= testcases; ++testcase)
	{
		int smax = 0, ans = 0, c = 0, l;
		string shystr = "";
		fin >> smax >> shystr;
		for (int i = 0; i <= smax; ++i)
		{
			if (shystr[i] > '0')
			{
				l = shystr[i] - '0';
				if (c + ans < i){
					ans = i - c;
				}
				c += l;
			}
		}
		fout << "Case #" << testcase << ": " << ans << endl;
	}
	return 0;
}