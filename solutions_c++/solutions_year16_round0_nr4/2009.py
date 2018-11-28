#include <bits/stdc++.h>

using namespace std;

ifstream fin("D.in");
ofstream fout("output.txt");

// #define fin cin
// #define fout cout

long long int k, c, s;

long long int HorPos(long long int a, long long int b)
{
	long long int x = 0;
	for (int i = 0; i < c; ++i)
	{
		x *= k;
		x += a;
		a = min(a + 1, b);
	}
	return x;
}

int main(int argc, char const *argv[])
{
	ios::sync_with_stdio(false);
	int t;
	fin>>t;
	int u = 0;
	while(u++ < t)
	{
		fin >> k >> c >> s;
		vector<long long int> ans;
		for (int i = 0; i < k; i += c)
		{
			ans.push_back(HorPos(i, k - 1));
		}
		fout << "Case #" << u << ": ";
		if (ans.size() > s) fout << "IMPOSSIBLE";
		else
		{
			for (int i = 0; i < ans.size(); ++i)
			{
				fout << ans[i] + 1 << " ";
			}
		}
		fout << endl;
	}
	return 0;
}
