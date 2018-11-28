#include<cstdio>
#include<algorithm>
using namespace std;

double a[1005],b[1005];

int cal(int n,double* a,double* b)
{
	int i=n-1,j=n-1,s=0;
	while(j>=0)
	{
		if(a[i]>b[j])
			s++,i--;
		j--;
	}
	return s;
}

int main()
{
//	freopen("E:/in.txt","r",stdin);
//	freopen("E:/out.txt","w",stdout);
	int T,t,n,i;
	for(scanf("%d",&T),t=1;t<=T;t++)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%lf",&a[i]);
		for(i=0;i<n;i++)
			scanf("%lf",&b[i]);
		sort(a,a+n);
		sort(b,b+n);
		printf("Case #%d: %d %d\n",t,cal(n,a,b),n-cal(n,b,a));
	}
	return 0;
}
