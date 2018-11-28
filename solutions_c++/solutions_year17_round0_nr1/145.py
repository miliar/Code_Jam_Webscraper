#include <bits/stdc++.h>
using namespace std;

int t_,n,T;
int m, ans;
char s[101000];

int main() {
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	for (scanf("%d\n",&T); T; T--) {
		scanf("%s %d\n",s + 1, &m);
		ans = 0;
		n = strlen(s + 1);
		for (int i = 1; i + m - 1 <= n; i++) {
			if (s[i] == '+') continue;
			for (int j = 0; j < m; j++)
				s[i + j] = s[i + j] == '+' ? '-' : '+';
			ans++;
		}
		bool flag = true;
		for (int i = max(1, n - m + 2); i <= n; i++)
			if (s[i] == '-') flag = false;
		printf("Case #%d: ",++t_);
		if (flag) printf("%d\n",ans);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}
