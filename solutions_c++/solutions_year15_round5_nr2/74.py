#include <iostream>
#include <ctime>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <vector>

using namespace std;

typedef long long LL;
typedef pair<int, int> PII;
typedef vector<int> VI;

#define REP(i, n) for(int i(0); (i)<(int)(n); i++)
#define FOR(i, a, b) for (int i(a); i <= int(b); i++)
#define ALL(x) x.begin(),x.end()
#define PB push_back
#define MP make_pair

const int N = 1005;
int n, k, S[N], a[N], b[N];

void solve() {

	scanf("%d%d", &n, &k);
	REP(i, n - k + 1) scanf("%d", &S[i]);
	memset(a, 0, sizeof(a));
	memset(b, 0, sizeof(b));
	for (int i = n - k - 1; i >= 0; i--) {
		int l = i;
		int r = i + k;
		int d = S[i + 1] - S[i];
		a[l] = max(a[l], a[r] + d);
		b[l] = min(b[l], b[r] + d);
	}
	int len = 0;
	REP(i, k) len = max(len, a[i] - b[i]);
	int u = 0;
	while (a[u] - b[u] != len) u++;

	int b1 = 0, b2 = 0;
	REP(i, k) {
		b1 -= b[i] - b[u];
		b2 -= a[i] - a[u];
	}
	int ans = len;
	if (b2 - b1 <= k * 2) {
		int flag = false;
		for (int i = b1; i <= b2; i++){
			if ((k + (S[0] - i) % k) % k == 0)
				flag = true;
		}
		if (!flag) ans++;
	}

	static int caseCnt = 0;
	cerr << caseCnt << endl;
	printf("Case #%d: %d\n", ++caseCnt, ans);
}

int main() {
	int T = 1;
	scanf("%d", &T);
	while (T--) solve();
	return 0;
}

