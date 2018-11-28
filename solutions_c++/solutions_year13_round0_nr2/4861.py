// round0.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>
#include <unordered_set>

using namespace std;

void parse(vector<vector<int>>& v, int N, int M)
{
	unordered_set<int> zerorow, zerocol;
	for (int i = 0; i < N; i++)
	{
		bool iszero = true;
		int val = v[i][0];
		for (int j = 1; j < M; j++)
		{
			if (v[i][j] != val)
			{
				iszero = false;
				break;
			}
		}
		if (iszero) zerorow.insert(i);
	}
	for (int j = 0; j < M; j++)
	{
		bool iszero = true;
		int val = v[0][j];
		for (int i = 1; i < N; i++)
		{
			if (v[i][j] != val)
			{
				iszero = false;
				break;
			}
		}
		if (iszero) zerocol.insert(j);
	}
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			if (zerorow.count(i) == 1 || zerocol.count(j) == 1)
				v[i][j] = 0;
		}
	}
}

string lawnmower(vector<vector<int>>& v)
{
	int N = v.size();
	int M = v[0].size();

	vector<vector<int>> v1(v);
	parse(v1, N, M);

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			if (v1[i][j] == 0) continue;
			bool flag1 = false, flag2 = false;
			int val = v[i][j];
			for (int k = 0; k < M; k++)
			{
				if (v[i][k] == val || (v1[i][k] == 0 && v[i][k] < val))
				{}
				else
				{
					flag1 = true;
					break;
				}
			}
			for (int k = 0; k < N; k++)
			{
				if (v[k][j] == val || (v1[k][j] == 0 && v[k][j] < val))
				{}
				else
				{
					flag2 = true;
					break;
				}
			}
			if (flag1 && flag2)
				return "NO";
		}
	}
	return "YES";
}

vector<int> parse_line(string line, int n)
{
	int p = 0, lp = 0;
	vector<int> v1;
	for (int k = 0; k < n; k++)
	{
		p = line.find(' ', lp);
		if (p == string::npos) p = line.length();
		v1.push_back(atoi(line.substr(lp, p-lp).c_str()));
		lp = p + 1;
	}
	return v1;
}

int main(int argc, char* argv[])
{
	ifstream in("B-small-attempt2.in");
	ofstream out("output.txt");
	string line;

	getline(in, line);
	int T = atoi(line.c_str());
	for (int i = 0; i < T; i++)
	{
		getline(in, line);
		int pos = line.find(' ');
		int N = atoi(line.substr(0, pos).c_str());
		int M = atoi(line.substr(pos+1).c_str());
		vector<vector<int>> v;
		for (int j = 0; j < N; j++)
		{
			getline(in, line);
			vector<int> v1 = parse_line(line, M);;
			v.push_back(v1);
		}
		out << "Case #" << i+1 << ": " << lawnmower(v) << endl;
	}
	return 0;
}