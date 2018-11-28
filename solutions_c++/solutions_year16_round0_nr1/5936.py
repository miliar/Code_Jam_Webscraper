#include<stdio.h>
#include<string.h>
int t, tt;
int n, i, cnt, j, sw;
int m, chk[20];
int main() {
	//freopen("1.in", "r", stdin);
	//freopen("1.out", "w", stdout);
	
	scanf("%d", &t);
	for (tt=1;tt<=t;tt++) {
		scanf("%d", &n);
		
		if (n == 0) {
			printf("Case #%d: INSOMNIA\n", tt);
		}
		else {
			for (i=0;i<=9;i++) {
				chk[i] = 0;
			}
			for (i=1;;i++) {
				m = n*i;
				while (m) {
					chk[m%10] = 1;
					m/=10;
				}
				sw = 0;
				for (j=0;j<=9;j++) {
					if (chk[j] == 0) {
						sw = 1;
						break;
					}
				}
				if (sw == 0) {
					printf("Case #%d: %d\n", tt, n*i);
					break;
				}
			}
		}
	}
	return 0;
}
