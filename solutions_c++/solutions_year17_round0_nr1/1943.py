#include <stdio.h>
#include <string.h>

char s[1002];
int k;

void solve() {
	scanf("%s %d", s, &k);
	int l = strlen(s);
	bool ok = 1;
	int ans = 0;
	for (int i = 0; i < l; i++) {
		if (s[i] == '-') {
			++ans;
			for (int j = 0; j < k; j++) {
				if (i + j < l) {
					if (s[i + j] == '-') s[i + j] = '+';
					else s[i + j] = '-';
				}
				else
					ok = 0;
			}
		}
	}
	if (ok) printf("%d\n", ans);
	else puts("IMPOSSIBLE");
}


int main() {
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int R=1; R<=T; R++){
		printf("Case #%d: ", R);
		solve();
	}

}