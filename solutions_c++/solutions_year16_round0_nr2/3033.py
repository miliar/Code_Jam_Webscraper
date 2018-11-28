// ProblemB.cpp : Defines the entry point for the console application.
//

#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
#include <string>
#include <fstream>

using namespace std;

typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef pair<int, int> pii;

int min_flip(string s, int n, char happy, char unhappy)
{
	if (n==0)
	{
		if (s[n] == happy)
			return 0;
		else
			return 1;
	}

	if (s[n] == happy)
		return min_flip(s, n - 1, happy, unhappy);
	else
		return 1 + min_flip(s, n - 1, unhappy, happy);
}

int main()
{
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");

	int item_count = 0;
	fin >> item_count;

	for (int i = 0; i < item_count; i++)
	{
		string s;
		fin >> s;
		fout << "Case #" << i + 1 << ": " << min_flip(s, s.size() - 1, '+', '-') << endl;
	}

    return 0;
}

