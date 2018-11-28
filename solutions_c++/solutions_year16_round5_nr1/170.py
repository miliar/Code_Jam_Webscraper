#include <bits/stdc++.h>
#define inf 0x3f3f3f3f
#define Inf 0x3FFFFFFFFFFFFFFFLL
#define rep(i, n) for (int i = 0; i < (n); ++i)
#define Rep(i, n) for (int i = 1; i <= (n); ++i)
#define FOR(i, c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define clr(x, a) memset(x, (a), sizeof x)
#define RD(x) scanf("%d", &x)
#define PB push_back
#define MP make_pair
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
int const N = 20020;
ll const mod = 1000000007LL;
char s[N], st[N];

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large-ans", "w", stdout);
	int T, ca = 1; scanf("%d", &T);
	while (T--) {
		scanf(" %s", s);
		int n = strlen(s);
		int ans = 0, top = 0;
		rep(i, n) {
			if (top > 0 && s[i] == st[top]) {
				ans += 10;
				--top;
			} else {
				st[++top] = s[i];
			}
		}
		ans += top / 2 * 5;
		printf("Case #%d: %d\n", ca++, ans);
	}
	return 0;
}

