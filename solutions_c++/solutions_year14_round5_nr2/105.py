#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
 
using namespace std;

typedef long long ll;
typedef unsigned long long ull;

#define FOR(i, a, b) for (auto i = (a); i < (b); i++)
#define FORD(i, a, b) for (auto i = (b)-1; i >= (a); i--)
#define FORE(it, x) for (auto it = (x).begin(); it != (x).end(); ++it)
#define ALL(x) (x).begin(), (x).end()

int n, p, q;
static int h[110], g[110], mins[110], ts[110], ds[110], was[110];
static int dpt[110][2000];
int dp(int k, int s) {
	if (s > 1500) cerr << "S";
	int& ret = dpt[k][s];
	if (ret == -1) {
		ret = dp(k+1, s+was[k]);
		if (s >= ds[k]) {
			ret = max(ret, g[k] + dp(k+1, s-ds[k]));
		}
	}
	return ret;
}

int main(void)
{
	int tn;
	cin >> tn;
	FOR (ti, 1, tn+1) {
		cin >> p >> q >> n;
		FOR (i, 0, n) cin >> h[i] >> g[i];
		FOR (i, 0, n) FOR (j, 0, 2000) dpt[i][j] = -1;
		FOR (j, 0, 2000) dpt[n][j] = 0;
		FOR (i, 0, n) {
			ts[i] = (h[i]-1)/q;
			mins[i] = (h[i] - ts[i]*q + p-1)/p;
			ds[i] = mins[i] - ts[i];
			was[i] = (h[i] + q-1)/q; 
		}
		cout << "Case #" << ti << ": " << dp(0, 1) << endl;
	}
	return 0;
}
