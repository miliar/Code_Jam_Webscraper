#include <iostream>
#include <fstream>
#include <string>
#include <set>
#define LL long long
#define MAXN 110
using namespace std;

int cakes[MAXN];

int calc( int n )
{
	int ret = 0;
	for (int i = 1; i < n; i++)
	{
		if (cakes[i] != cakes[i - 1]) ret++;
	}
	return ret;
}

int main()
{
	fstream fin("in.txt");
	fstream fout("out.txt");
	int T;
	fin >> T;
	for (int t = 1; t <= T; t++ )
	{
		string str;
		fin >> str;
		memset(cakes, 0, sizeof(cakes));

		int n = str.length();
		for (int i = 0; i < n; i++)
			cakes[i] = (str[i] == '+');

		int res = calc( n );
		if (cakes[n - 1] == 0) res++;

		fout << "Case #" << t << ": " << res << endl;
	}
	return 0;
}