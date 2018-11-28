#include<cstdio>

bool ispalindrom (long long k) {
	long long l = k, p=0;
	while(l>0) {
		p = p*10 + l%10;
		l/=10;
	}
	return p == k;
}
int main() {
	int cs;
	scanf("%d", &cs);
	long long fair[100], a, b;
	int	fi=0;
	for(long long i=1; i*i <100000000000000;i++)
		if(ispalindrom(i) && ispalindrom(i*i))
			fair[fi++] = i*i;
	for(int c=1; c<=cs; c++) {
		printf("Case #%d: ", c);
		scanf("%lld %lld", &a, &b);
		int count = 0, c=0;
		while(fair[c] < a) c++;
		while(fair[c] <= b && c < fi) {
			count++;
			c++;
		}
		printf("%d\n", count);
	}
	return 0;
}
