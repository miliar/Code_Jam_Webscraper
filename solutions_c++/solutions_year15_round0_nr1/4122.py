#include <cstdio>
const int maxn = 1000 + 10;
char ss[maxn];
int s[maxn];

int cal_inv(int *s, int i) {
	int d = 0;
	if(i < 1) return 0;
	else d = cal_inv(s, i-1);
	if(i <= s[i] + d) return d;
	else return i-s[i];
}
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T, cnt = 1;
	scanf("%d", &T);
	while(T--) {
		int S;
		scanf("%d %s", &S, ss);

		s[0] = 0;
		for(int i = 1; i <= S; i++)
			s[i] = ss[i-1] - '0' + s[i-1];
		
		int ans = cal_inv(s, S);
		printf("Case #%d: %d\n", cnt++, ans);
	}
	return 0;
}