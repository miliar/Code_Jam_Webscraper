/** jan25 **/
#include <bits/stdc++.h>
#define s1(n)						scanf("%d", &n)
#define s2(n, m)					scanf("%d%d", &n, &m)
#define mp 							make_pair
#define pb 							push_back
#define ms0(X) 						memset((X), 0, sizeof((X)))
#define ms1(X) 						memset((X), -1, sizeof((X)))
#define F 							first
#define S 							second
typedef long long ll;
using namespace std;
const int MOD = 1e9+7;
#define gc getchar_unlocked
#define si(x) scanf("%d", &x)
#define isd(x) (x >= '0' && x <= '9')


int main() {
	char c;
	int n, a, b, ans, t; si(t);
	for (int i = 1; i <= t; ++i) {
		ans = 0;
		si(n);
		c = gc();
		while (!isd(c)) c = gc();
		a = 0;
		for (int j = 0; j <= n; ++j) {
			b = c-'0';
			if (j > a) {
				ans += j-a;
				a += j-a;
			}
			a += b;
			c = gc();
		}
		printf("Case #%d: %d\n", i, ans);
	}
	/*
	4
4 11111
1 09
5 110011
0 1
*/
	
	return 0;
}
