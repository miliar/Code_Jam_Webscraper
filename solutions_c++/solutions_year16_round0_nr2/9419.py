#include<bits/stdc++.h>
using namespace std;
#define  mp make_pair
#define  pb push_back
#define fi first
#define se second
#define inf 99999999LL
#define  M 1000000007
#define PI 3.1415926535897932
typedef long long int ll;
char ch[105];
int a[104];
int check()
{
	int i;
	int len=strlen(ch);
	for(i=0;i<len;i++)
		if(a[i]!=1)
			return 0;
		return 1;
}
int func(void)
{
	int steps=0,n=strlen(ch),i,j,st=0,en=n-1,fl=0;
	while(1)
	{
		if(check())
			return steps;
		else
		{
			int k=n-1;
			while(a[k]==1)
				k--;
			st=k;
			k=0;
			int hara=0;
			while(a[k]==1&&k<st)
			{
				a[k]=0;
				k++;
				hara=1;
			}
			if(hara)
			{
				steps++;
				continue;
			}
			for(i=0;i<=st;i++)
			{
				a[i]=a[i]^1;
			}
			reverse(a,a+st+1);
			steps++;
		}
	}
}
int madher=1;
int main()
{
	int i,j,t;
	scanf("%d",&t);

	while(t--)
	{
		memset(a,0,sizeof(a));
		scanf("%s",ch);
		int len=strlen(ch);
		for(i=0;i<len;i++)
		{
			if(ch[i]=='+')
				a[i]=1;
			else
				a[i]=0;
		}
		int ans=func();
		printf("Case #%d: %d\n",madher++,ans);

	}
	return 0;
}