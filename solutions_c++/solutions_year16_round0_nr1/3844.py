#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sstream>
#include <iostream>
#include <math.h>
#include <time.h>
#include <unistd.h>
#include <algorithm>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <vector>
#include <set>
#include <string>

#ifndef ONLINE_JUDGE
	#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
#else
	#define DEBUG(x) do {} while(0);
#endif

#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define FOR(i, A, N) for(int (i) = (A); (i) < (N); (i)++)
#define REP(i, N) for(int (i) = 0; (i) < (N); (i)++)

using namespace std;
typedef long long ll;
inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }

int n,m;
int T;

void solve() {
	scanf("%d", &n);
	int seen = 0;
	for(ll mult = 1; mult <= 1000000; mult++) {
		ll cnum = n*mult;
		ll x = cnum;
		while(x > 0) {
			seen |= 1<<(x%10);
			x /= 10;
		}
		if(seen == (1<<10)-1) {
			printf("%lld", cnum);
			return;
		}
	}
	printf("INSOMNIA");

}

int main() {
	scanf("%d", &T);
	REP(testc, T) {
		printf("Case #%d: ", testc+1);
		solve();
		printf("\n");
	}
	return 0;
}
