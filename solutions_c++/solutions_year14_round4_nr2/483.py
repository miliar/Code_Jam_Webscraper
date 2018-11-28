#include<cstdio>
#include<cstring>
#include<algorithm>
const int maxn=100010;

int n,a[maxn];
int main()
{
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		scanf("%d",&n);
		for(int i=1;i<=n;i++)scanf("%d",a+i);
		int ans=0;
		for(int i=n;i>1;i--)
		{
			int mn=1;
			for(int j=2;j<=i;j++) 
				if(a[mn]>a[j])  mn=j;
			ans+=std::min(mn-1,i-mn);
			for(int j=mn;j<i;j++) a[j]=a[j+1];
		}
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
