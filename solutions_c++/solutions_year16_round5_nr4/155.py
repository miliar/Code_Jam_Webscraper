#include <bits/stdc++.h>

using namespace std;

int T, N, L;
char s[110][60], t[60];

int main() {
	freopen("D-small-attempt1.in", "r", stdin);
	freopen("D.out", "w", stdout);
	scanf("%d", &T);
	for(int cas = 1; cas <= T; cas ++) {
		scanf("%d%d", &N, &L);
		for(int i = 0; i < N; i ++) {
			scanf("%s", s[i]);
		}
		scanf("%s", t);
		bool ok = 1;
		for(int i = 0; i < N; i ++) {
			if(!strcmp(s[i], t)) ok = 0;
		}
		printf("Case #%d: ", cas);
		if(ok) {
			for(int i = 0; i < L-1; i ++)
				printf("?0");
			printf("? ");
			if(L != 1) {
				for(int i = 0; i < L-1; i ++)
					printf("1");
			} else {
				printf("0");
			}
			printf("\n");
		} else {
			printf("IMPOSSIBLE\n");
		}
	}
	return 0;
}
