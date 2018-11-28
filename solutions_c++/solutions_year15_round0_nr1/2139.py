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
typedef long long ll;

// S E N W
int dx[]={1,0,-1,0};
int dy[]={0,1,0,-1};

int T;
int smax;
#define N 1010
char s[N];

int solve() {
	cin >> smax;
	cin >> s;
	
	for (int si = 0; si <= smax; ++si) {
		s[si] -= '0';
	}

	int si = 1, st = s[0], inv = 0;
	for (; si <= smax; ++si) {
		if (st >= si) {
			st += s[si];
		} else {
			++inv;
			st += s[si] + 1;
		}
	}
	

	return inv;
}

int main()
{
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		printf("Case #%d: %d\n", t, solve());
	}

	return 0;
}
