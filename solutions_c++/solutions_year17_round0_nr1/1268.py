#include <bits/stdc++.h>

using namespace std;

int Test, ans, K, len;
char s[1010];

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &Test);
	for (int tt = 1; tt <= Test; tt++){
		scanf("%s%d", s, &K);
		len = strlen(s);
		ans = 0;
		for (int i = 0; i + K <= len; i++)
			if (s[i] == '-'){
				++ans;
				for (int j = 0; j < K; j++)
					if (s[i + j] == '-') s[i + j] = '+';
					else s[i + j] = '-';
			}
		bool flag = 1;
		for (int i = 0; i < len; i++)
			if (s[i] == '-')
				flag = 0;
		printf("Case #%d: ", tt);
		if (flag) printf("%d\n", ans);
		else printf("IMPOSSIBLE\n");
	}
}