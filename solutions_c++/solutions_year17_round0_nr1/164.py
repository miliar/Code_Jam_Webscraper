#include <bits/stdc++.h>

using namespace std;

int T, k, n;

char ch[11111];

int main()
{
	scanf("%d", &T);
	for(int TT = 1; TT <= T; TT++) {
		printf("Case #%d: ", TT);
		scanf("%s%d", ch, &k), n = strlen(ch);
		int ans = 0;
		for(int i = 0; i <= n - k; i++) if(ch[i] == '-') {
			for(int j = i; j < i + k; j++) ch[j] = ch[j] == '-' ? '+' : '-';
			ans++;
		}
		for(int i = n - k + 1; i < n; i++) if(ch[i] == '-') ans = -1;
		if(ans == -1) puts("IMPOSSIBLE"); else printf("%d\n", ans);
	}
	return 0;
}
