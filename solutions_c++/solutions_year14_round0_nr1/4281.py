#define G2014_A 1
#if G2014_A == 1

#if 1
	#define GIN "A-small-attempt0.in" 
	#define GOUT "A-small-attempt0.out"
#endif

#if 0
	#define GIN "input.txt" 
	#define GOUT "output.txt"
#endif

#if 0
	#define GIN "D-large.in" 
	#define GOUT "D-large.out"
#endif

#define myfile(B) ("E:\\CodeJam\\A\\"##B)

#include <SDKDDKVer.h>
#include <stdio.h>
#include <tchar.h>
#include <cstdio>
#include <stdio.h>
#include <stdlib.h>
#include <map>
#include <set>
#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <fstream>
using namespace std;

ifstream g_infile;
ofstream g_outfile;
#define read(x) {g_infile >> x;}
#define readline(x) {std::getline(g_infile, x);}
#define write(x) {g_outfile << x;}
#define result_head(x) {g_outfile << "Case #"; g_outfile << x;  g_outfile << ": ";}
#define result_endl() {g_outfile << std::endl;}

void alg()
{
	int t, T, i, n, N, temp, crlf;
	string skip;
	vector<int> first, second;

	read(T);
	for (t = 1; t <= T; ++t)
	{
		first.clear(); second.clear();

		read(N); 
		for (n = 1; n <= 4; ++n)
		{
			if (n == N) 
			{
				for (i = 0; i < 4; i++)
				{
					read(temp);
					first.push_back(temp);
				}				
			}
			else
			{
				read(crlf);
				readline(skip);
			}
		}

		read(N);
		for (n = 1; n <= 4; ++n)
		{
			if (n == N)
			{
				for (i = 0; i < 4; ++i)
				{
					read(temp);
					second.push_back(temp);
				}				
			}
			else
			{
				read(crlf);
				readline(skip);
			}
		}

		vector<int> intersection;
		sort(first.begin(), first.end());
		sort(second.begin(), second.end());
		set_intersection(first.begin(), first.end(), second.begin(), second.end(), back_inserter(intersection));

		int len = intersection.size();
		result_head(t);
		switch(len)
		{
		case 0:
			write("Volunteer cheated!");
			break;
		case 1:
			write(intersection[0]);
			break;
		default:
			write("Bad magician!");
			break;
		}
		result_endl();
	}
}



int main(int argc, _TCHAR* argv[])
{
	g_infile.open(myfile(GIN), ifstream::in);
	g_outfile.open(myfile(GOUT), ifstream::out);

	alg();

	g_outfile.close();
	g_infile.close();
	return 0;
}

#endif