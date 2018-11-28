#include <stdio.h>
#include <algorithm>
using namespace std;

const int N=1111;
int tc,n;
double a[N],b[N];

int d_war()
{
	int i,l,r,pt;
	pt=0;
	l=0; r=n-1;
	for(i=0;i<n;++i)
	{
		if(a[i]<b[l]) --r;
		else ++l,++pt;
	}
	return pt;
}

int war()
{
	int i,j,pt;
	pt=0;
	j=0;
	for(i=0;i<n;++i)
	{
		for(;j<n&&b[j]<a[i];++j);
		if(j<n) ++j;
		else ++pt;
	}
	return pt;
}

int main()
{
	int o,i;
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	for(scanf("%d",&tc),o=1;o<=tc;++o)
	{
		scanf("%d",&n);
		for(i=0;i<n;++i)
			scanf("%lf",&a[i]);
		for(i=0;i<n;++i)
			scanf("%lf",&b[i]);
		sort(a,a+n);
		sort(b,b+n);
		printf("Case #%d: %d %d\n",o,d_war(),war());	
	}
	return 0;
}