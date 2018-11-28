#include<bits/stdc++.h>
using namespace std;

char* tobitStr(int x, int bit) {
	char* s = new char[32];
	s[0] = '1';
	int p = 1;
	for(int i = 0; i < bit; i++) {
		s[p++] = x % 2 + '0';
		x /= 2;
	}
	s[p++] = '1';
	s[p] = 0;
	return s;
}

int main() {
	int T;
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	scanf("%d",&T);
	for(int tc = 1; tc <= T; tc++) {
		printf("Case #%d: \n", tc);
		int N,J;
		scanf("%d %d",&N,&J);
		int len = N / 2;
		for(int i = 0; i < J; i++) {
			char *s = tobitStr(i, len - 2);
			printf("%s%s ",s,s);
			for(int base = 2; base <= 10 ; base++) {
				long long ans = 0;
				for(int j = 0; j < strlen(s); j++) {
					ans = ans * base + s[j] - '0';
				}
				printf("%lld",ans);
				if(base < 10) printf(" ");
				else puts("");
			}
		}
	}
}



