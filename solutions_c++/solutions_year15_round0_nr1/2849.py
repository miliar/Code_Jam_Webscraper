#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>

using namespace std;

ifstream fin;
ofstream fout;

void solve(int);

int main()
{
	fin = ifstream("st.in");
	fout = ofstream("st.out");

	int T;
	fin >> T;
	for (int i = 0; i < T; i++)
	{
		solve(i+1);
	}
}

void solve(int caseNum)
{
	int SMax;
	fin >> SMax;
	string shyness;
	fin >> shyness;

	int num = 0, i = 0, max_diff = 0;
	for (auto it = shyness.begin(); it != shyness.end(); it++)
	{
		int n = (*it) - 48;
		if (num < i)
		{
			max_diff = max(max_diff, i - num);
		}
		num += n;
		i++;
	}
	fout << "Case #" << caseNum << ": " << max_diff << '\n';
}