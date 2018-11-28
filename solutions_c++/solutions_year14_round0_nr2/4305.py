#define G2014_B 1
#if G2014_B == 1

#if 0
	#define GIN "B-small-attempt0.in" 
	#define GOUT "B-small-attempt0.out"
#endif

#if 0
	#define GIN "input.txt" 
	#define GOUT "output.txt"
#endif

#if 1
	#define GIN "B-large.in" 
	#define GOUT "B-large.out"
#endif

#define myfile(B) ("E:\\CodeJam\\B\\"##B)

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
#include <iomanip>
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
	int t, T;
	double C, F, X, speed;
	double Target, Time;

	read(T);

	for (t = 1; t <= T; ++t)
	{
		read(C); read(F); read(X);

		Target = X; Time = 0; speed = 2;

		while (true)
		{
			double time1 = Target / speed;		
			double time2 = C / speed + Target / (speed + F);

			if (time1 <= time2)
			{
				Time += time1;
				break;
			}
			else
			{
				Time += C / speed;
				speed  += F;
			}
		}


		result_head(t);
		g_outfile << fixed << setprecision(8) << Time;
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