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

#define MAXN 1000010
#define MAX_C 1000000000
ull N;

ull dp[MAXN];

ull getd(ull in) {
	ull ret = 1;
	ull dig = 0;
	ull tmp = in;
	for (; tmp != 0;) {
		dig ++;
		tmp = tmp / 10;
	}

	dig /= 2;
	while(dig--) {
		ret *= 10;
	}

	return ret;
}

ull rev(ull in) {
	ull ret = 0;
	ull tmp = in;
	for (; tmp != 0;) {
		ret = ret * 10;
		ret = ret + tmp % 10;
		tmp = tmp / 10;
	}
	return ret;
}

ull geth(ull in) {
	ull ret = 0;
	ull tmp = in;
	for (; tmp != 0;) {
		ret = tmp % 10;
		tmp = tmp / 10;
	}
	return ret;
}

ull DP(ull in) {

	if (in > 1000010) {
		return MAX_C;
	}
	if(in < 10) {
		dp[in] = in;
		return dp[in];
	}
	if(dp[in] != 0) return dp[in];

	if (in%10 != 0 && in > rev(in)) {
		dp[in] = min(DP(in - 1), DP(rev(in))) + 1;
	}
	else {
		dp[in] = DP(in - 1) + 1;
	}
	//printf("%llu = %llu\n", in, dp[in]);
	return dp[in];
}

void cal(ull in) {

}

void solve() {
	//cout << rev(12345600) << endl;

	ull ans = 0;
	ull tmp = N;

	while(true) {
		//printf("==> [%llu] %llu h=%llu s=%llu\n", ans, tmp, h, s);

		if (tmp < 10) {
			printf("%llu\n", ans + tmp);
			break;
		}

		ull r = rev(tmp) ;
		if (tmp <= r || (tmp % getd(tmp)) != 1 || tmp % 10 == 0) {
			tmp--;
			ans++;
		}
		else {
			tmp = r;
			ans++;
		}
	}
	fflush(stdout);
}

int main() {
	int cases;
	int caseid = 1;

	//dp[1] = 1;

	freopen("input", "r", stdin);
	//freopen("output", "w", stdout);
	scanf("%d", &cases);
	while (cases--) {
		printf("Case #%d: ", caseid++);
		scanf("%llu", &N);
		solve();
		//printf("%llu\n", DP(N));
	}
	return 0;
}

