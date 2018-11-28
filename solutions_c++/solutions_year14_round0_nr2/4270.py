#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <unordered_set>
#include <map>
#include <fstream>

using namespace std;

double T, C, F, X;
int main()
{
	string filename = "B-large";
	ifstream fin(filename + ".in");
	FILE *fout = fopen((filename + ".out").c_str(), "w");

	fin >> T;
	for(int t = 1; t <= T; t++)
	{
		fin >> C >> F >> X;
		double c = 0, ti = 0, s = 2;
		while(c < X)
		{
			double wait = (X - c) / s;
			double buy = (C - c) / s + X / (s + F); 
			if(buy < wait)
			{
				ti += (C - c) / s;
				c = 0;
				s += F;
			} 
			else
			{
				ti += wait;
				c = X;
			}
		}
		fprintf(fout, "Case #%d: %.7f\n", t, ti);
	}

	fin.close();
	fclose(fout);
 	return 0;
}