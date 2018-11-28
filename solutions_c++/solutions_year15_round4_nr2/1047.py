#pragma comment(linker, "/STACK:102400000,102400000")
#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <vector>
#include <cassert>
#include <map>
#include <cmath>
#include <queue>
#include <stack>
#include <set>
#define  RD(x)      scanf("%d", &x)
#define  REP(i, n)  for (int i=0; i<int(n); ++i)
#define  FOR(i, n)  for (int i=1; i<=int(n); ++i)
#define  pii        pair<int, int>
#define  piL        pair<int, long long>
#define  mp         make_pair
#define  pb         push_back
#define  whatis(x)  cout << #x << ": " << x << endl;
int dx[4] = {0, -1, 0, 1};
int dy[4] = {1, 0, -1, 0};

using namespace std;
#define  N   123
#define  eps 1e-8
#define  pi  acos(-1.0)
#define  inf 0XFFFFFFFll
#define  mod 1000000007ll
#define  LL  long long
#define  ULL unsigned long long

pair<LL, LL> s[N];

LL get(double x) {
	return x * 10000 + eps;
}
int Main() {

//	freopen("bc.txt", "r", stdin);
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	ios_base::sync_with_stdio(0);

	int T = 0;
	cin >> T;

	FOR(_T, T) {

		int n;
		cin >> n;
		double _Y;
		double _X;
		cin >> _Y >> _X;
		LL Y = get(_Y);
		LL X = get(_X);
		LL sum = 0, psum = 0;
		FOR(i, n) {
			double a, b;
			cin >> b >> a;

			s[i] = mp(get(a), get(b));

			psum += s[i].first * s[i].second;
			sum += s[i].second;
		}

		sort(s + 1, s + n + 1);

		printf("Case #%d: ", _T);

		if (X < s[1].first || X > s[n].first) {
			puts("IMPOSSIBLE");
			continue;
		}

		double ans = 0.0;
		if (psum > X * sum) {
			for (int i = n; i > 0; i--) {
				LL tsum = sum - s[i].second;
				LL tpsum = psum - s[i].first * s[i].second;
				if (tpsum / tsum <= X) {
					double r = 1.0 * (X * tsum - tpsum) / (s[i].first * s[i].second - X * s[i].second);
					ans = r * s[i].second + tsum;
					psum = tpsum +  r * s[i].first * s[i].second;
					break;
				} else {
					sum = tsum;
					psum = tpsum;
				}
			}

		} else if (psum < X * sum) {
			FOR(i, n) {
				LL tsum = sum - s[i].second;
				LL tpsum = psum - s[i].first * s[i].second;
				if (tpsum / tsum >= X) {
					double r = 1.0 * (X * tsum - tpsum) / (s[i].first * s[i].second - X * s[i].second);
					ans = r * s[i].second + tsum;
					psum = tpsum +  r * s[i].first * s[i].second;
					break;
				} else {
					sum = tsum;
					psum = tpsum;
				}
			}
		} else {
			ans = sum;
		}
		ans = 1.0 * Y / ans;
		printf("%.10f\n", ans);





	}


	return 0;
}

int main() {
	return Main();
}
