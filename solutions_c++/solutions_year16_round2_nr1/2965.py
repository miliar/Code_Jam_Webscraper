#define _CRT_SECURE_NO_WARNINGS
#include <fstream>
#include <map>
#include <iostream>
#include <utility>
#include <set>
#include <algorithm>
#include <bitset>
#include <queue>
#include <functional>
#include <assert.h>
#include <ctime>
#include <utility>
#include <stack>
#define SI(i) scanf("%d ", &i)
#define SII(i,j) scanf("%d%d", &i, &j)
#define SIII(i,j, k) scanf("%d%d%d", &i, &j, &k)
#define SF(i) scanf("%lf", &i)
#define SFF(i,j) scanf("%lf%lf", &i, &j)
#define SFFF(i,j, k) scanf("%lf%lf%lf", &i, &j, &k)
#define SL(i) scanf("%I64d", &i)
#define SLL(i,j) scanf("%I64d%I64d", &i, &j)
#define SLLL(i,j, k) scanf("%I64d%I64d%I64d", &i, &j, &k)
#define SS(i) scanf("%s\n", i)
#define SSS(i,j) scanf("%s %s", i, j)
#define SC(i) scanf("%c ", &i)
#define SCC(i,j) scanf("%c %c\n", &i, &j)

#define PI(i) printf("%d ", i)
#define PI2(i) printf("%d", i)
#define PII(i,j) printf("%d %d ", i, j)
#define PL(i) printf("%I64d ", i)
#define PLL(i,j) printf("%I64d %I64d ", i, j)
#define PS(i) printf("%s", i)
#define PSS(i,j) printf("%s %s ", i, j)
#define PC(i) printf("%c", i)
#define PCC(i,j) printf("%c %c ", i, j)
#define PN printf("\n")
#define forin(i, k, n) for(int i = (k); i < (n); ++i)
#define forin2(i, k, n) for(int i = (k); i <= (n); ++i)
#define rforin(i, k, n) for(int i = (k); i > (n); --i)
#define mp make_pair
#define rep(i) i  < 'a' ? 'A' : 'a'
typedef unsigned long long ull;
#define pi pair<ull, ull>
using namespace std;
int main() {
#ifdef _DEBUG
	freopen("1.in", "rt", stdin);
	freopen("1.out", "wt", stdout);
#endif
	int t;
	SI(t);
	for (int tt = 1; tt <= t; ++tt)
	{
		printf("Case #%d: ", tt);
		int res[700], tm[26], ind = 0;
		forin(i, 0, 700)
			res[i] = 0;
		forin(i, 0, 26)
			tm[i] = 0;
		char s[2001];
		SS(s);
		for (int i = strlen(s) - 1; i >= 0; --i)
			++tm[s[i] - 'A'];
		while (tm['Z' - 'A'])
		{
			res[ind++] = 0;
			--tm['Z' - 'A'];
			--tm['E' - 'A'];
			--tm['R' - 'A'];
			--tm['O' - 'A'];
		}
		while (tm['W' - 'A'])
		{
			res[ind++] = 2;
			--tm['T' - 'A'];
			--tm['W' - 'A'];
			--tm['O' - 'A'];
		}
		while (tm['U' - 'A'])
		{
			res[ind++] = 4;
			--tm['F' - 'A'];
			--tm['O' - 'A'];
			--tm['U' - 'A'];
			--tm['R' - 'A'];
		}
		while (tm['X' - 'A'])
		{
			res[ind++] = 6;
			--tm['S' - 'A'];
			--tm['I' - 'A'];
			--tm['X' - 'A'];
		}
		while (tm['G' - 'A'])
		{
			res[ind++] = 8;
			--tm['E' - 'A'];
			--tm['I' - 'A'];
			--tm['G' - 'A'];
			--tm['H' - 'A'];
			--tm['T' - 'A'];
		}
		while (tm['F' - 'A'])
		{
			res[ind++] = 5;
			--tm['F' - 'A'];
			--tm['I' - 'A'];
			--tm['V' - 'A'];
			--tm['E' - 'A'];
		}
		while (tm['O' - 'A'])
		{
			res[ind++] = 1;
			--tm['O' - 'A'];
			--tm['N' - 'A'];
			--tm['E' - 'A'];
		}
		while (tm['R' - 'A'])
		{
			res[ind++] = 3;
			--tm['T' - 'A'];
			--tm['H' - 'A'];
			--tm['R' - 'A'];
			--tm['E' - 'A'];
			--tm['E' - 'A'];
		}
		while (tm['V' - 'A'])
		{
			res[ind++] = 7;
			--tm['S' - 'A'];
			--tm['E' - 'A'];
			--tm['V' - 'A'];
			--tm['E' - 'A'];
			--tm['N' - 'A'];
		}
		while (tm['I' - 'A'])
		{
			res[ind++] = 9;
			--tm['N' - 'A'];
			--tm['I' - 'A'];
			--tm['N' - 'A'];
			--tm['E' - 'A'];
		}
		sort(res, res + ind);
		forin(i, 0, 26)
			assert(tm[i] == 0);
		forin(i, 0, ind)
			PI2(res[i]);
		PN;
	}

	return 0;
}