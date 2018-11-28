#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<iostream>
#include<vector>
using namespace std;
typedef long long lld;
#define X first
#define Y second
#define mp make_pair
#define pb push_back
int n,L;
lld s[1010];
lld need[1010];
char str[100010];
lld in()
{
	lld tmp=0;
	scanf("%s",str);
	lld bit=1;
	for(int i=0;i<L;i++)
	{
		if(str[i] == '1')
			tmp+=bit;
		bit*=2;
	}
	return tmp;
}
int ones(lld x)
{
	int tmp=0;
	while(x)
	{
		tmp+=x&1;
		x/=2;
	}
	return tmp;
}
lld val[1010];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int cas;
	scanf("%d",&cas);
	for(int cc=1;cc<=cas;cc++)
	{
		scanf("%d %d",&n,&L);
		for(int i=0;i<n;i++)
			s[i]=in();
		for(int i=0;i<n;i++)
			need[i]=in();
		sort(need,need+n);
		int ans=10086;
		for(int t=0;t<n;t++)
		{
			lld change=s[0]^need[t];
			for(int i=0;i<n;i++)
				val[i]=s[i]^change;
			sort(val,val+n);
			bool flag=true;
			for(int i=0;i<n;i++)
				if(val[i] != need[i])
					flag=false;
			if(flag)
				ans=min(ans,ones(change));
		}
		printf("Case #%d: ",cc);
		if(ans == 10086)
			printf("NOT POSSIBLE\n");
		else
			printf("%d\n",ans);
	}
	return 0;
}
/*
3
3 2
01 11 10
11 00 10
2 3
101 111
010 001
2 2
01 10
10 01

 */
