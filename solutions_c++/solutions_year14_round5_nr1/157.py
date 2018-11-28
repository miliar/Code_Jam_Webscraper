#include<cstdio>

__int64 a[1000000];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int tc,tcn;
	scanf("%d",&tcn);
	for(tc=1;tc<=tcn;tc++)
	{
		__int64 L,R,mid;
		__int64 i,j,n,p,q,r,s,tot=0;
		__int64 ll,rr,mm;
		scanf("%I64d%I64d%I64d%I64d%I64d",&n,&p,&q,&r,&s);
		for(i=0;i<n;i++)tot+=a[i]=(i*p+q)%r+s;
		L=1;R=tot;
		while(L<R)
		{
			mid=(L+R)/2;
			ll=0;
			for(i=0;i<n&&ll<=mid;i++)ll+=a[i];
			ll-=a[--i];
			rr=0;
			for(j=n-1;j>=i&&rr<=mid;j--)rr+=a[j];
			rr-=a[++j];
			mm=0;
			for(;i<=j;i++)mm+=a[i];
			if(mm<=mid)R=mid;
			else L=mid+1;
		}
		printf("Case #%d: %.10Lf\n",tc,((long double)(tot-L))/tot);
	}
	return 0;
}