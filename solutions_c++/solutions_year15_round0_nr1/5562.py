#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
#define sz(v) (int)v.size()
#define all(c) (c).begin(),(c).end()

char tmp[1234];

int main ( ) {
	freopen("1", "r", stdin);
	freopen("2", "w", stdout);
	int tc, t = 0, n;
	scanf("%d", &tc);
	while (tc--) {
		scanf("%d %s", &n, tmp);
		vector<int> v(n + 1);
		for (int i = 0; i <= n; i++)
			v[i] = (tmp[i] - '0');
		int ans = 0;
		for (int i = 1; i <= n; i++) {
			if (i > v[i - 1] + ans) ans += i - (v[i - 1] + ans);
			v[i] += v[i - 1];
		}
		printf("Case #%d: %d\n", ++t, ans);
	}
}
