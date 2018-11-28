#include<stdio.h>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<string.h>
#include<iostream>
#include<stdlib.h>
#include<math.h>
#include<algorithm>
#define eps 1e-7
using namespace std;

int gcd(int a,int b) { return b==0?a:gcd(b,a%b); }
int Min(int a,int b) { return a<b?a:b; }

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int cas,i,ccass=1,n;
	char ch[1005];
	scanf("%d",&cas);
	while(cas--)
	{
		printf("Case #%d: ",ccass++);
		scanf("%d",&n); getchar();
		n=n+1;
		int res=0;
		int pre=0;
		gets(ch);
		for(i=0;i<n;i++)
		{
			int t=ch[i]-'0';
			if(t==0) continue;
			if(pre>=i) pre+=t;
			else {
				res+=(i-pre);
				pre+=(i-pre+t);
			}
		}
		printf("%d\n",res);
	}
	return 0;
}