#include <bits/stdc++.h>
using namespace std;
char s[1100];
int n, m;
int main()
{
	int T;
	scanf("%d", &T);
	for(int cas = 1; cas <= T; ++cas) {
		scanf("%s %d", s, &m);
		int ans = 0;
		n = strlen(s);
		for(int i = 0; i < n; ++i) {
			s[i] = s[i] == '+';
		}
		for(int i = 0; i <= n - m; ++i) {
			if(s[i] == 0) {
				for(int j = 0; j < m; ++j)
					s[i + j] = !s[i + j];
				++ans;
			}
		}
		for(int i = n - m; i < n; ++i) {
			if(!s[i])
				ans = -1;
		}
		if(ans == -1)
			printf("Case #%d: IMPOSSIBLE\n", cas);
		else
			printf("Case #%d: %d\n", cas, ans);
	}
	return 0;
}
