#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <cstring>
#include <deque>
using namespace std;
//-----------------------------------------------------------
#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) int(a.size() - 1)
#define all(a) a.begin(), a.end()
#define seta(a,x) memset (a, x, sizeof (a))
#define I (int)
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const ull inf64 = ((ull) 1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;

#define bit(i) ((ull)1 << i)
//-----------------------------------------------------------

#define MAXP 1010
int D;
int p[ MAXP ];

void solve()
{
	int ans = INT_MAX;
	int maxp = 0;
	for(int i = 0; i < D; i++) {
		maxp = max(maxp, p[i]);
	}

	// the maximum height
	for(int h = 1; h <= maxp; h++) {
		int move = 0;
		for (int i = 0; i < D; i++) {
			if (p[i] <= h) continue;

			move += (int)ceil((double)p[i] / (double)h) - 1;
			//printf("h=%d %d needs %d moves\n", h, p[i], (int)ceil((double)p[i] / (double)h) - 1);
		}
		move += h;
		ans = min(ans, move);

		//printf("h=%d ==> %d\n", h, move);
	}


	printf("%d\n", ans);

	fflush(stdout);
}

int main() {
	int cases;
	int caseid = 1;

	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
	scanf("%d", &cases);
	while(cases--) {
		printf("Case #%d: ", caseid++);
		scanf("%d", &D);
		for(int i = 0; i < D; i++) {
			scanf("%d", &p[ i ]);
		}
		solve();
	}
	return 0;
}

