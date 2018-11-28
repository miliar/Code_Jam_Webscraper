#include<cstdio>
#include<cmath>
#include<cctype>
#include<cstring>
#include<string>
#include<queue>
#include<algorithm>
#include<iostream>
#include<cstdlib>
#include<vector>
#include<stack>
#define FOR(a,b,c) for(a=b;a<c;a++)
#define FORD(a,b,c) for(a=b;a>c;a--)
using namespace std;
int main()
{
	int n,t,tc,i,ans,x,k,j;
	char a[1001];
	scanf("%d",&tc);
	FOR(t,0,tc)
	{
		ans=0;
		x=0;
		scanf("%d ",&n);
		FOR(i,0,n+1)
		{
			scanf("%c",&a[0]);
			if ((x<i)&&(a[0]!='0'))
			{
				ans+=i-x;
				x+=i-x;	
			}
			x+=a[0]-48;
		}
		printf("Case #%d: %d\n",t+1,ans);
	}
}














