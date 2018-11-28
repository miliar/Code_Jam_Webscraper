#include<bits/stdc++.h>
using namespace std;
int cnt,a[10];
int func(int n)
{
	int temp;
	while(n)
	{
		temp=n%10;
		n/=10;
		if(!a[temp])
		{
			a[temp]=1;cnt++;if(cnt==10) return 0;
		}
	}
	return 1;
}
int main()
{
	int t,cs,n,m;
	scanf("%d",&t);
	for(cs=1;cs<=t;cs++)
	{
		scanf("%d",&n);
		if(!n)
		{
			printf("Case #%d: INSOMNIA\n",cs);continue;
		}
		m=n;memset(a,0,sizeof(a));cnt=0;
		while(func(n))
		{
			n+=m;
		}
		printf("Case #%d: %d\n",cs,n);
	}
}
