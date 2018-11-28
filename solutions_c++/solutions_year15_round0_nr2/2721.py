#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

ifstream fin;
ofstream fout;

void solve(int);

int main()
{
	fin = ifstream("IHoP.in");
	fout = ofstream("IHoP.out");

	int T;
	fin >> T;
	for (int i = 0; i < T; i++)
	{
		solve(i + 1);
	}
}

void solve(int _case_)
{
	int D, totalP = 0, maxP = 0;
	fin >> D;
	vector<int> P;
	for (int i = 0; i < D; i++)
	{
		int tP;
		fin >> tP;
		P.push_back(tP);
		totalP += tP;
		maxP = max(maxP, tP);
	}

	int min_time = maxP;

	for (int i = 1; i < maxP; i++)
	{
		int time = i;
		for (auto it = P.begin(); it != P.end(); it++)
		{
			if (*it > i)
			{
				time += (int)ceil((*it) / (float)i) - 1;
			}
		}
		min_time = min(min_time, time);
	}

	cout << "Case #" << _case_ << ": " << min_time << '\n';
	fout << "Case #" << _case_ << ": " << min_time << '\n';
}