#include<stdio.h>
int t, tt;
int k, c, s;
long long kpow[150], sum;
int main() {
	//freopen("d.in", "r", stdin);
	//freopen("d.out", "w", stdout);
	int i, j;
	scanf("%d", &t);
	for (tt=1;tt<=t;tt++) {
		scanf("%d%d%d", &k, &c, &s);
		printf("Case #%d: ", tt);
		kpow[0] = 1;
		for (i=1;i<c;i++) {
			kpow[i] = kpow[i-1] * (long long)k;
		}
		for (i=0;i<k;i++) {
			sum = 0;
			for (j=0;j<c;j++) {
				sum += kpow[j]*(long long)i;
			}
			printf("%lld ", sum+1);
		}
		printf("\n");
	}
	return 0;
}
