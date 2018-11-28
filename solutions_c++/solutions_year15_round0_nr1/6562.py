#include<stdio.h>
#include<string.h>
int main() {
	int a[1005],k,t,l,e, res,x=1;
	char b[1005];
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	for (scanf("%d\n", &t); t--; x++) {
		scanf("%d %s\n", &k, b);
		l = strlen(b);
		e = res = 0;
		for (int i = 0; i < l; i++) {
			if (e < i) {
				res += i - e;
				e = i;
			}
			e += b[i] - '0';
		}
		printf("Case #%d: %d\n", x, res);
	}
	return 0;
}