#include<iostream>
#include<fstream>
#include <cstdio>
#include <cmath>
#include <climits>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>
#include <map>

using namespace std;

string pattern(int n, int p, int r, int s)
{
	if (n == 1)
	{
		if (r == 2 || s == 2 || p == 2)
		{
			return "IMPOSSIBLE";
		}
		else
		{
			if (r == 0) return "PS";
			else if (s == 0) return "PR";
			else return "RS";
		}
	}

	int countR1 = r/2;
	int countR2 = r/2;
	if (r%2)
	{
		if (p%2) countR2++;
		else countR1++;
	}

	return pattern(n - 1, p/2 + p%2, countR1, s/2) + pattern(n - 1, p/2, countR2, s/2 + s%2);
}

int main() {
	bool outputToFile = false;
	string inputFile = "1.in";
	string outputFile = "1.out";

	/* Merging input/output streams with filestreams */
	streambuf *coutbuff;
	ofstream out;
	streambuf *cinbuff;
	ifstream in;

	if(outputToFile)
	{
		out.open(outputFile);
		coutbuff = out.rdbuf();

		in.open(inputFile);
		cinbuff = in.rdbuf();
	}
	else
	{
		coutbuff = cout.rdbuf();
		cinbuff = cin.rdbuf();
	}
	
	ostream fout(coutbuff);
	istream fin(cinbuff);

	/* Merging ends */

    long long int testCases;
	fin >> testCases;

	long long int tc = 0;
    while (++tc <= testCases)
    {
		fout << "Case #" << tc << ": ";
		
		int n, r, p, s;
		fin >> n >> r >> p >> s;

		int total = pow(2, n);
		int mAll = total/3 + 1;
		int nAll = total/3;
		if ((p >= nAll && p <= mAll) && (r >= nAll && r <= mAll) && (s >= nAll && s <= mAll))
		{
			fout << pattern(n, p , r, s);
		}
		else
		{
			fout << "IMPOSSIBLE";
		}

		fout << endl;
    }

	if(outputToFile)
	{
		out.close();
		in.close();
	}
    
    return 0;
}
