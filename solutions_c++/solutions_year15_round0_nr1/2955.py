#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <cstdlib>
using namespace std;

int a[1001], cur;
char s[1001];
int n, T, ans;

int main() {
	//freopen("A-large.in", "r", stdin);
	//freopen("1.out", "w", stdout);
	scanf("%d", &T);
	for (int tt = 1; tt <= T; ++tt) {
		memset(s, 0, sizeof(s));
		scanf("%d", &n);
		scanf("%s", s);
		cur = 0;
		ans = 0;
		for (int i = 0; i <= n; ++i)
			if (cur < i) {
				ans += i - cur;
				cur = i + s[i] - '0';
			}
			else
				cur += s[i] - '0';
		printf("Case #%d: %d\n", tt, ans);
	}
	return 0;
}
