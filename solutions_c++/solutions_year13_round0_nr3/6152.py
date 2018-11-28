#include<cstdio>
using namespace std;
int sum[1001];
int ispalin(int x)
{
	char s[10];
	int i=0,l;
	while(x)
	{
		s[i]=x%10+48;
		x=x/10;
		i++;
	}
	s[i]=0;
	l=i;
	for(i=0;s[i]!=0;i++)
	{	
		if(s[i]!=s[l-i-1])
		{
			return 0;
		}
	}
	return 1;
}
void solve()
{
	int i;
	for(i=1;i*i<=1000;i++)
	{
		if(ispalin(i)&&ispalin(i*i))
		{
			sum[i*i]=1;
		}
	}
	for(i=1;i<=1000;i++)
	{
		sum[i]=sum[i-1]+sum[i];
	}
}
int main()
{
	int t,T,a,b,ans;
	solve();
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		scanf("%d%d",&a,&b);
		ans=sum[b]-sum[a-1];
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
