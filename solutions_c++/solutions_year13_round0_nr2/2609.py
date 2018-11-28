#include <stdio.h>

using namespace std;


int main()
{
	long long tc,t,i,j,x,y;
	int a[100][100],r[100],c[100];
	scanf("%lld\n",&t);
	for (tc=0;tc<t;++tc)
	{
		scanf("%lld %lld",&x,&y);
		for (i=0;i<x;++i) for (j=0;j<y;++j) scanf("%d",a[i]+j);
		for (i=0;i<x;++i) r[i]=0;
		for (i=0;i<y;++i) c[i]=0;
		for (i=0;i<x;++i) for (j=0;j<y;++j)
		{
			if (a[i][j]>r[i]) r[i]=a[i][j];
			if (a[i][j]>c[j]) c[j]=a[i][j];
		}
		int rr=1;
		for (i=0;i<x;++i) for (j=0;j<y;++j)
		{
			if (a[i][j]<r[i] && a[i][j]<c[j]) rr=0;
		}
		printf("Case #%lld: %s\n",tc+1,rr?"YES":"NO");
	}
	return 0;
}
