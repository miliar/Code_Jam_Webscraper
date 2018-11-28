# include <cstdio>
# include <cstring>

using namespace std;

int n, l;
char c[1200];
int a[1200];
int b[1200];

int main() {
	int T, cas = 0; scanf("%d", &T);
	while(T--) {
		printf("Case #%d: ", ++cas);
		scanf("%s%d", c, &n);
		l = strlen(c);
		for(int i = 0; i < l; ++i) a[i] = (c[i] == '+'), b[i] = 0;
		int ans = 0;
		for(int i = 0; i <= l - n; ++i) {
			if((a[i] ^ b[i]) == 0) 
				b[i] ^= 1, b[i + n] ^= 1, ans += 1;
			b[i + 1] ^= b[i];
		}
		bool flag = true;
		for(int i = l - n + 1; i < l; ++i) {
			if((a[i] ^ b[i]) == 0) flag = false;
			b[i + 1] ^= b[i];
		}
		if(flag) printf("%d\n", ans);
		else puts("IMPOSSIBLE");
	}
	return 0;
}

