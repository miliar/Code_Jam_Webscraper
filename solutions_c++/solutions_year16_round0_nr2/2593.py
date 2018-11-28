/*
ID: dixtosa1
PROG: milk2
LANG: C++11
*/
#pragma comment(linker, "/STACK:16777216")
#include <iostream>
#include <fstream>
#include <cstdio>
#include <stdio.h>
#include <cstdlib>
#include <stdlib.h>
#include <string>
//#include <string.h>
#include <list>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <map>
#include <vector>
#include <iomanip>
#include <queue>
#include <deque>
#include <set>
#include <stack>
#include <sstream>
#include <assert.h>
#include <functional> //std::greater<int>
//#include <tuple>

//#include "Biginteger.cpp"
//#include "sqrt.cpp"
//#include "tree.cpp"
//#include "funcs.cpp"

typedef long long ll;
typedef std::pair<ll, ll> pii;
#define ALL(x)           (x).begin(), (x).end()
#define forn(N)          for(long long i = 0; i < (long long)N; i++)
#define fornj(N)         for(long long j = 0; j < (long long)N; j++)
#define fornk(N)         for(long long k = 0; k < (long long)N; k++)
#define foreach(c,itr)   for(auto itr=(c).begin();itr!=(c).end();itr++)
#define PI 3.1415926535897932384626433
#define LINF (1LL<<60)
#define INF (1<<30)
#define awesome vector<int> A(N); forn(N) scanf("%d", &A[i]);
#define v vector
#define File "Patterns"
using namespace std;


int solve(string s, int index, int ans = 0)
{
	while (index >= 0 && s[index] == '+') index--;

	if (index < 0) return ans;


	int lastNegatives = index;
	while (lastNegatives >= 0 && s[lastNegatives] == '-') lastNegatives--;

	if (lastNegatives < 0) return ans + 1;
	else
	{

		int firstPositives = 0;
		while (firstPositives <= index && s[firstPositives] == '+')
		{
			s[firstPositives] = '-';
			firstPositives++;
		}
		if (firstPositives > 0) ans++;
		else
		{
			for (int i = 0; i <= index / 2; i++)
			{
				swap(s[i], s[index - i]);
				s[i] = s[i] == '-' ? '+' : '-';
				if(index - i != i) s[index - i] = s[index - i] == '-' ? '+' : '-';
			}
			ans++;
		}

		return solve(s, index, ans);
	}
}

int main()
{
#if defined(_DEBUG) || defined(_RELEASE)
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#else
	//freopen(File".in", "r", stdin); freopen(File".out", "w", stdout);
#endif

	int T; cin >> T;
	for (int test = 1; test <= T; test++)
	{
		string s; cin >> s;
		cout << "Case #"<<test<<": " << solve(s, s.length() - 1) << endl;
	}

	//printf("\n\ntime-%.3lf", clock()*1e-3);
	return 0;
}