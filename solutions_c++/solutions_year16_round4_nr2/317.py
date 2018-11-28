#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <iomanip>
#include <iostream>
#include <queue>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

#define INF 1000000000
#define FOR(i, a, b) for(int i=int(a); i<int(b); i++)
#define FORC(cont, it) for(decltype((cont).begin()) it = (cont).begin(); it != (cont).end(); it++)
#define pb push_back

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;

#define maxN 200

double p[maxN], dp[maxN][maxN], a[maxN];

double solve(int n, int k) {
	if (k < 0) return 0;
	if (n < 0) return !k;
	if (dp[n][k] != -1.) return dp[n][k];
	return dp[n][k] = (1. - a[n])*solve(n - 1, k) + (a[n])*solve(n - 1, k - 1);
}

int main() {
	int T, caso=1, N, K;
	cin >> T;
	cout << fixed << setprecision(12);
	while (T--) {
		cin >> N >> K;
		FOR(i, 0, N) cin >> p[i];
		sort(p, p + N);
		double ans = 0;
		FOR(i, 0, K+1) {
			int tk = 0;
			FOR(j, 0, i) a[tk++] = p[j];
			FOR(j, 0, K - i) a[tk++] = p[N - j - 1];
			FOR(j, 0, tk) FOR(k, 0, K) dp[j][k] = -1;
			ans=max(ans, solve(tk - 1, K / 2));
		}
		cout << "Case #" << caso++ << ": " << ans << endl;
	}
	return 0;
}
