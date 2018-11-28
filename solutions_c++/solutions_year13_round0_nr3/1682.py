#include <cstdio>
#include <cstring>
#include <cmath>

long long int a[10000];

int main()
{
	int nn = 0;
	for(long long int i = 1; i <= 99999999; ++i)
	{
		char p[64];
		sprintf(p, "%lld", i);
		int n = strlen(p);
		long long k;
		for(int j = 0; j < n; ++j)
			if(p[j] != p[n-1-j]) goto aaa;
		k = i * i;
		sprintf(p, "%lld", k);
		n = strlen(p);
		for(int j = 0; j < n; ++j)
			if(p[j] != p[n-1-j]) goto aaa;
		a[nn++] = k;
		aaa:;
	}
	int ti = 0;
	int tn;
	scanf("%d",&tn);
	while(tn--)
	{
		long long int A, B;
		int t = 0;
		scanf("%lld %lld", &A, &B);
		for(int i = 0; i < nn; ++i)
			if(a[i] >= A && a[i] <= B) t++;
		printf("Case #%d: %d\n", ++ti, t);
	}
}
