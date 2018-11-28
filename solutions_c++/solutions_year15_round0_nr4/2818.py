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
	int x,r,c,i,j,n,t,tc;
	scanf("%d",&tc);
	FOR(t,0,tc)
	{
		scanf("%d %d %d",&x,&r,&c);
		printf("Case #%d: ",t+1);
		if (x==1) printf("GABRIEL");
		else if (x==2)
		{
			if (r%2==0||c%2==0) printf("GABRIEL");
			else printf("RICHARD");
		}
		else if (x==3)
		{
			if (((r<2||c<2)||(r==2&&c==2))||((r*c)%3!=0)) printf("RICHARD");
			else printf("GABRIEL");
		}
		else
		{
			if ((r<3||c<3)||(r*c)%4!=0) printf("RICHARD");
			else printf("GABRIEL");
		}
		printf("\n");
	}
}














