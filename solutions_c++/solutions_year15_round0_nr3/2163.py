#include <functional>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <numeric>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <string>
#include <vector>
#include <bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <list>
#include <set>
#include <map>
#include <complex>
using namespace std;

#define FOR(i, a, b) for(int i = a, __up = b; i < __up; ++i)
#define REP(n) FOR(i, 0, n)
#define CLR(a) memset(a, 0, sizeof a)

typedef complex<double> point;

// S E N W
int dx[]={1,0,-1,0};
int dy[]={0,1,0,-1};

int T;
#define X 10010
string sl;
char ctoi[256];

#define i 2
#define j 3
#define k 4
char mult[][5] = {
	{0, 0, 0, 0, 0},
	{0, 1, i, j, k},
	{0, i, -1, k, -j},
	{0, j, -k, -1, i},
	{0, k, j, -i, -1},
};
#undef i
#undef j
#undef k

int ll, x;
bool solve() {
	cin >> ll >> x;
	cin >> sl;
	string s;
	REP(x) s+=sl;
	int i = 0, j, n = j = ll*x, r, l = r = 1;
	
	for (; i<n; ++i) {
		s[i] = ctoi[s[i]];
	}
	
	for (i = 0; i<n; ++i) {
		if (l > 0) l = mult[l][s[i]];
		else l = -mult[-l][s[i]];
		if (l == ctoi['i']) break;
	}
	if (i == n) return 0;

	for (--j; j>=0; --j) {
		if (r > 0) r = mult[s[j]][r];
		else r = -mult[s[j]][-r];
		if (r == ctoi['k']) break;
	}
	if (j == 0) return 0;

	l = 1;
	for (++i; i<j; ++i) {
		if (l > 0) l = mult[l][s[i]];
		else l = -mult[-l][s[i]];
	}
	if (l == ctoi['j']) return 1;
	return 0;
}

int main()
{
	ctoi['1'] = 1;
	ctoi['i'] = 2;
	ctoi['j'] = 3;
	ctoi['k'] = 4;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		printf("Case #%d: %s\n", t, (solve() == 1 ? "YES" : "NO"));
	}

	return 0;
}
