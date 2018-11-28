#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<string>
#include<iomanip>
#include<vector>
#include<set>
#include<map>
#include<queue>

using namespace std;
typedef long long LL;
typedef unsigned long long ULL;

#define rep(i,k,n) for(int i=(k);i<=(n);i++)
#define rep0(i,n) for(int i=0;i<(n);i++)
#define red(i,k,n) for(int i=(k);i>=(n);i--)
#define sqr(x) ((x)*(x))
#define clr(x,y) memset((x),(y),sizeof(x))
#define pb push_back
#define mod 1000000007

char s[1010],ans[1010];
bool b[1010];

int main()
{
	int T;
	scanf("%d",&T);
	rep(ii,1,T)
	{
		scanf("%s",s);
		int len=strlen(s);
		int le=0,ri=len-1;
		char mc=0;
		clr(b,0);
		for(int i=0;i<len;i++)
		{
			mc=max(mc,s[i]);
			if(s[i]==mc)b[i]=1;
		}
		int k=len-1;
		while(le<=ri && k>=0)
		{
			if(b[k])ans[le++]=s[k];
			else ans[ri--]=s[k];
			k--;
		}
		ans[len]=0;
		printf("Case #%d: %s\n",ii,ans);
	}
	
	return 0;
}
