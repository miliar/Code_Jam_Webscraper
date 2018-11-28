#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <assert.h>
#include <set>
using namespace std;

#define FOR(i,n) for (int i = 0; i < n; i++)
#define abs(x) ((x)<0?(-(x)):(x))
#define REP(i,v) for (unsigned i = 0; i < v.size(); i++)
#define RL(i,v) for (unsigned i = 0; i < v.length(); i++)
typedef long long ll;

const double INF = 1e99;

double dp[1<<20];
int n;

double f(int mask)
{
	if (mask == ((1 << n) - 1)) return 0;
	if (dp[mask] != -1) return dp[mask];
	double res = 0;
	FOR(i, n) {
		int j = i;
		int k = 0;
		while (mask & (1 << j)) {
			j = (j + 1) % n;
			k++;
		}
		res += n - k + f(mask | (1<<j));
	}
	dp[mask] = res / (double) n;
	return dp[mask];
}

void solve(void)
{
	char s[250];
	scanf("%s", s);
	n = (int) strlen(s);
	int mask = 0;
	FOR(i, n) if (s[i] == 'X') mask |= (1 << i);
	//
	FOR(i, 1<<20) dp[i] = -1;
	printf("%.10lf\n", f(mask));
	//
	
}

int main(void)
{
//   	freopen("/home/vesko/gcj/d.in", "rt", stdin);
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		printf("Case #%d: ", tc);
		solve();
	}
	return 0;
}

