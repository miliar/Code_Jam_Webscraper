#define G2014_D 1
#if G2014_D == 1

#if 0
	#define GIN "D-small-attempt0.in" 
	#define GOUT "D-small-attempt0.out"
#endif

#if 0
	#define GIN "input.txt" 
	#define GOUT "output.txt"
#endif

#if 1
	#define GIN "D-large.in" 
	#define GOUT "D-large.out"
#endif

#define myfile(B) ("E:\\CodeJam\\D\\"##B)

#include <SDKDDKVer.h>
#include <stdio.h>
#include <tchar.h>
#include <cstdio>
#include <stdio.h>
#include <stdlib.h>
#include <map>
#include <set>
#include <vector>
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
using namespace std;

ifstream g_infile;
ofstream g_outfile;
#define read(x) {g_infile >> x;}
#define readline(x) {std::getline(g_infile, x);}
#define write(x) {g_outfile << x;}
#define result_head(x) {g_outfile << "Case #"; g_outfile << x;  g_outfile << ": ";}
#define result_endl() {g_outfile << std::endl;}

bool compare(double i, double j) { return (i < j); }

void alg()
{
	int T, N, t, i, j;
	double temp;
	int y, z;
	vector<double> Naomi;
	vector<double> Ken;

	read(T);
	for (t = 1; t <= T; ++t)
	{
		Naomi.clear();
		Ken.clear();
		y = 0;
		z = 0;
	
		read(N);
		for (j = 0;  j < N; ++j)
		{
			read(temp);
			Naomi.push_back(temp);
		}
		for (j = 0; j < N; ++j)
		{
			read(temp);
			Ken.push_back(temp);
		}
		
		sort(Naomi.begin(), Naomi.end(), compare);
		sort(Ken.begin(), Ken.end(), compare);

		i = 0; j = 0;
		while (i < N && j < N)
		{
			if (Ken[j] < Naomi[i])
			{
				j++;
			}
			else
			{
				z++;
				i++; 
				j++;
			}
		}

		i = 0; j = 0;
		while (i < N && j < N)
		{
			if (Naomi[i] < Ken[j])
			{
				i++;
			}
			else
			{
				y++;
				i++;
				j++;
			}
		}

		result_head(t);
		write(y); write(' '); write(N - z);
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