#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:167772160000")
#include <iostream>
#include <fstream>
#include <cstdio>
#include <stdio.h>
#include <cstdlib>
#include <stdlib.h>
#include <string>
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
#include <functional>
#include <climits>
#include <cstring>
typedef long long ll;
typedef std::pair<ll, ll> pll;
typedef std::pair<int, int> pii;
//typedef std::pair<long double,long double> pdd;
#define forn(N)          for(int i = 0; i<(int)N; i++)
#define fornj(N)         for(int j = 0; j<(int)N; j++)
#define fornk(N)         for(int k = 0; k<(int)N; k++)
#define forn1(N)          for(int i = 1; i<=(int)N; i++)
#define fornj1(N)         for(int j = 1; j<=(int)N; j++)
#define fornk1(N)         for(int k = 1; k<=(int)N; k++)
#define PI 3.1415926535897932384626433
#define v vector
#define ll long long
#define print(n) printf("%d ", (n));
#define printll(n) printf("%I64d", (n));
#define printline() printf("\n");
#define read(n) scanf("%d", &n);
#define read2(n, m) scanf("%d%d", &n, &m);
#define readll(n) scanf("%I64d", &n);
#define mp make_pair
using namespace std;

const ll mod = 1000000007;


bool mood[21000];
int best[21000][21000];

inline int con(int a, int b) {
	if (mood[a] == mood[b])return 10;
	else return 5;

}

int main()
{
#if defined(_DEBUG) || defined(_RELEASE)
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#else
	//(File".in", "r", stdin); freopen(File".out", "w", stdout);
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#endif
	int T; cin >> T;
	fornk1(T) {
		string s; cin >> s;
		int n = s.length();
		forn(n)if (s[i] == 'C')mood[i] = 1;
		else mood[i] = 0;
		for (int len = 1; len < n; len+=2)for (int beg = 0; beg + len < n; beg++) {

			int en = beg + len;
			if (len > 1)best[beg][en] = con(beg, en) + best[beg + 1][en - 1];
			else best[beg][en] = con(beg, en);
			for (int i = beg + 1; i < en; i += 2)best[beg][en] = max(best[beg][en], best[beg][i]+ best[i + 1][en]);


		}
		cout << "Case #" << k << ": " << best[0][n - 1] << endl;

	}



	return 0;

}
