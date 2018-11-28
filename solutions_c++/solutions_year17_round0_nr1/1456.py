#include <bits/stdc++.h>
#define ll long long
#define mk make_pair
#define remove rrr
using namespace std;

const int N = 1e5 + 5;

char s[N];
int n, k, ans, a[N];

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T, cas = 0;
	scanf("%d", &T);
	while (T--) {
		scanf("%s", s + 1);
		scanf("%d", &k);
		ans = 0;
		n = strlen(s + 1);
		for (int i = 1; i <= n; i++) a[i] = 0;
		for (int i = 1; i <= n - k + 1; i++) {
			a[i] += a[i - 1];
			if ((a[i] & 1) && s[i] == '+') a[i]++, a[i + k]--, ans++;
			else if ((a[i] % 2 == 0) && s[i] == '-') a[i]++, a[i + k]--, ans++;
		}
		bool ok = 1;
		for (int i = n - k + 2; i <= n; i++) {
			a[i] += a[i - 1];
			if ((a[i] & 1) && s[i] == '+') ok = 0;
			if ((a[i] % 2 == 0) && s[i] == '-') ok = 0;
		}
		if (ok) printf("Case #%d: %d\n", ++cas, ans);
		else printf("Case #%d: IMPOSSIBLE\n", ++cas);
	}
}


