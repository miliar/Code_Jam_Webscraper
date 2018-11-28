#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>

#define pause cout << " press ansy key to continue...",  cin >> chh
#define file_r(x) freopen(x,  "r",  stdin)
#define file_w(x) freopen(x,  "w",  stdout)
#define lowbit(x) ((x) & (-x))
#define repit(i, c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define rep(i, n) for (int i = 0; i < (n); i++)
#define repe(i, u) for (int i = head[u]; i != -1; i = nxt[i])
#define repd(i, n) for (int i = (n - 1); i >= 0; i--)
#define FOR(i, n, m) for (int i = (n); i <= (m); i++)
#define FORD(i, n, m) for (int i = (n); i >= (m); i--)
#define pb push_back
#define X first
#define Y second
#define mp make_pair
#define lb lower_bound
#define ub upper_bound
#define SZ(c) (c).size()
#define ALL(c) (c).begin(), (c).end()
#define sqr(r) ((r) * (r))
#define dis(x1, y1, x2, y2) (((x1) - (x2)) * ((x1) - (x2)) + ((y1) - (y2)) * ((y1) - (y2)))

#define bug(x) cout << #x" = " << x << endl
#define bug2(x, y) cout << #x" = " << x << " " << #y" = " << y << endl
#define bug3(x, y, z) cout << #x" = " << x << " " << #y" = " << y << " " << #z" = " << z << endl
#define bug4(x, y, z, w) cout << #x" = " << x << " " << #y" = " << y << " " << #z" = " << z << " " << #w" = " << w << endl

#define in(n) scanf("%d", &n)
#define in2(n, m) scanf("%d %d", &n, &m)
#define in3(x, y, z) scanf("%d %d %d", &x, &y, &z)

using namespace std;
int chh;

typedef vector<int> vi;
typedef set<int> si;
typedef map<int, int> mii;
typedef pair<int, int> pii;
typedef pair<int, pii> pi3;
typedef vector< pair<int, int> > vpii;
typedef long long LL;

int T, n;
set<double> q1, q2, q3, q4;

int main() {
	double x, y;
	int s1, s2, s3, s4, p, cas = 0;
	scanf("%d", &T);
	while (T--) {
		scanf("%d", &n);
		q1.clear(), q2.clear(), q3.clear(), q4.clear();
		rep (i, n) {
			scanf("%lf", &x);
			q1.insert(x), q3.insert(x);
		}
		rep (i, n) {
			scanf("%lf", &x);
			q2.insert(x), q4.insert(x);
		}
		s1 = s2 = 0;
		printf("Case #%d: ", ++cas);
		rep (i, n) {
			x = *q1.begin();
			y = *q2.begin();
			if (x > y) {
				s1++;
				q1.erase(x), q2.erase(y);
			} else {
				s2++, y = *q2.rbegin();
				q1.erase(x), q2.erase(y);
			}
		}
		s3 = s4 = 0;
		rep (i, n) {
			x = *q3.begin();
			y = *q4.begin();
			set<double> :: iterator it = q4.lower_bound(x);
			if (it == q4.end()) {
				s3++;
				q3.erase(x), q4.erase(y);
			} else {
				s4++;
				q3.erase(x), q4.erase(it);
			}
		}
		printf("%d %d\n", s1, s3);
	}
    return 0;
}
