#include <bits/stdc++.h>

using namespace std;

ifstream fin("B.in");
ofstream fout("output.out");

// #define fin cin
// #define fout cout

int main(int argc, char const *argv[])
{
	ios::sync_with_stdio(false);
	int t;
	fin >> t;
	int u = 0;
	while (u++ < t)
	{
		string s;
		fin >> s;
		s.push_back('+');
		int x = 0;
		for (int i = 1; i < s.size(); ++i)
		{
			if (s[i] != s[i - 1]) x++;
		}
		fout << "Case #" << u << ": " << x << endl;
	}
	return 0;
}