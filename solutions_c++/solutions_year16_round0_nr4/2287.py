#include <cstdio>
#include <climits>

long long pow(int a,int b) {
	long long now = a;
	for (int i=1;i<b;i++) {
		now*=a;
	}
	return now;
}

int main () {
	int q;
	scanf("%d",&q);
	int k,c,s;
	for (int i=0;i<q;i++) {
		scanf("%d%d%d",&k,&c,&s);
		long long maxx = pow(k,c);
		long long cur = 1;
		long long intv =0;
		if (k>1) intv= (maxx-1)/(k-1);
		printf("Case #%d: ",i+1);
		for (int i=0;i<s;i++) {
			printf("%lld ",cur);
			cur+=intv;
		}
		printf("\n");
	}
	return 0;
}
