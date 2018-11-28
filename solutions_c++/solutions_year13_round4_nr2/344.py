#include <stdio.h>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <queue>
#include <math.h>
using namespace std;
#define N 100
int a[N];
int main()
{
	long long i, j, n, p, k, l, c, r;
	int ts, tst;
	for(scanf("%d", &tst), ts=1; ts<=tst; ts++)
	{
		printf("Case #%d: ", ts);
		scanf("%lld%lld", &n, &p);
		for(l=0, r=(1ll<<n)-1; l<r; )
		{
			c=(l+r+1)/2;
			for(j=c+1, k=0; (1ll<<k)<=j; k++); k--;
			for(j=0; k<n; j=j*2+1, k++);
			if((1ll<<n)-1-j<p) l=c;
			else r=c-1;
		}
		for(j=(1ll<<n)-p, k=0, i=0; i<n; a[i]=(j>>i)&1, k+=a[i], i++);
		for(i=n-1; i>=0 && a[i]; i--);
		k=min(k, n-i);
		printf("%lld %lld\n", r, (1ll<<n)-(1ll<<k));
	}
	return 0;
}