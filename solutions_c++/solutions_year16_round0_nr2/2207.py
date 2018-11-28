#include <bits/stdc++.h>

using namespace std;

int T;

char s[200];

int main() {
	freopen("B-large.in","r",stdin);
	freopen("ans1.txt","w",stdout);

	scanf("%d", &T);

	int cas = 0;
	while(T--) {
		printf("Case #%d: ", ++cas);

		scanf("%s", s);

		int n = strlen(s);
		while(n > 0 && s[n - 1] == '+') n--;
		if(n == 0) {
		    printf("0\n");
		    continue;
		}

		int ans = 0, pr = s[0];
		for(int i = 0; i < n; i++) {
			if(s[i] != pr) {
				ans++;
				pr = s[i];
			}
		}
		ans++;
		printf("%d\n", ans);
	}
}
