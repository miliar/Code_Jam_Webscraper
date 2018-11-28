#include<cstdio>
#include<iostream>
#include<cmath>
#include<cstring>
#include<cstdlib>
#include<string>
#include<sstream>
#include<vector>
#include<map>
#include<set>
#include<bitset>
#include<algorithm>
#include<cassert>
#include<ctime>
#include<queue>
using namespace std;

#define rep(i,n) for(int i = 0; i < (int)n; i++)
#define FOR(i,n,m) for(int i = (int)n; i <= (int)m; i++)
#define FOD(i,n,m) for(int i = (int)n; i >= (int)m; i--)
#define EACH(i,v) for(__typeof((v).begin()) i = (v).begin(); i != (v).end(); i++)

typedef long long i64;
typedef pair<int, int> PI;

#define sz(v) ((i64)(v).size())
#define all(v) (v).begin(),(v).end()
#define bit(n) (1LL<<(i64)(n))

#define PB push_back
#define MP make_pair
#define X first
#define Y second

const int INF = 1e9;
const double Pi = acos(-1.0);
const double eps = 1e-5;

template<class T> void fmax(T &a, const T &b) { if (a < b) a = b; }
template<class T> void fmin(T &a, const T &b) { if (a > b) a = b; }
template<class T> T sqr(const T &a) { return a * a; }

const int N = 44;

int n, m, ans;
long long sum, M, a[N], B;

bool ok(long long m) {
	long long s = 0;
	FOR(i, 1, n) if (a[i] < m) s += m - a[i];
	return s <= B;
}
double calc(long long l) {
	if (!ok(l)) return 0.0;
		double ans = 0;
		long long sum = 0;
		int w = 0;
		vector<long long> z;
		FOR(i, 1, n) if (a[i] <= l) w++, sum += l - a[i], z.PB(l - a[i]);
		sort(z.begin(), z.end());
		FOR(q, 0, min(w - 1LL, B - sum)) {
			double tmp = 0;
			long long cost = q + sum;
			int r = w - q;
			FOR(i, q, w - 1) tmp += z[i] * 36.0 / r;
			ans = max(ans, tmp - cost);
		}
		return ans;
}

int main() {
	int CNT;
	cin >> CNT;
	FOR(cnt, 1, CNT) {
		cin >> B >> n;
		sum = 0; M = 0;
		FOR(i, 1, n) cin >> a[i], M = max(M, a[i]);
		FOR(i, n + 1, 37) a[i] = 0;
		n = 37;
		long long l = 1, r = M;
		double ans = 0;
		while (l + 10 <= r) {
			long long m = (1 + l +r ) / 2;
			if (ok(m)) l = m;
			else r = m - 1;
		}
		for(long long i = max(l - 100, 0LL); i <= r + 100; i++) 
			if (ok(i)) ans = max(ans, calc(i));
		printf("Case #%d: %.10f\n", cnt, ans);
//		cout << "Case #" << cnt << ": " << ans << endl;
	}
}
