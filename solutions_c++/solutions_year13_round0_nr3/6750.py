#include <stdio.h>
#include <cmath>

const int N=10000010;
int q[N];
int a[100];

int f(long long n)
{
	long long m=n*n;
	int p=0;
	while (m>0){
		a[p++]=m%10;
		m/=10;
	}

	for (int i=0; i<=p/2; i++)
		if (a[i]!=a[p-1-i])
			return 0;

	return 1;
}

int getnum(long long n)
{
	int m=sqrt(n+0.5);
	return q[m];
}

int main()
{
	int T, t;
	long long a, b;
	for (long long i=0; i<N; i++) q[i]=f(i);
	for (int i=1; i<N; i++) q[i]+=q[i-1];
	
	freopen("1.txt", "r", stdin);
	freopen("2.out", "w", stdout);
	scanf("%d", &T);
	for (t=1; t<=T; t++)
	{
		scanf("%lld%lld", &a, &b);
		printf("Case #%d: %d\n", t, getnum(b)-getnum(a-1));
	}

	return 0;
}