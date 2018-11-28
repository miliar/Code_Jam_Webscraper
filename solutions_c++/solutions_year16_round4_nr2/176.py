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
int n, K;
double p[300];
bool is[300];

double ret[300];
double prob() {
	
	forn(n)ret[i] = 0;
	ret[0] = 1;
	forn(n) {
		if (!is[i])continue;
		for (int j = n - 1; j > 0; j--)ret[j] = ret[j] * (1 - p[i]) + ret[j - 1] * p[i];
		ret[0] *= (1 - p[i]);

	}
	return ret[K / 2];

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
		 cin >> n >> K;
		
		forn(n)is[i] = 0;
		forn(n)cin >> p[i];
		forn(K)is[i] = 1;
		sort(is, is + n);
		double answer = prob();
		while (next_permutation(is, is + n))answer = max(answer, prob());
		cout << "Case #" << k << ": " << fixed << setprecision(10) << answer << endl;
	}

	return 0;

}
