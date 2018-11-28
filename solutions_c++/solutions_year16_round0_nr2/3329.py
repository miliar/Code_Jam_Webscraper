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

char s[10000];

int main()
{
	int T;
	scanf("%d",&T);
	rep(ii,1,T)
	{
		scanf("%s",s);
		printf("Case #%d: ",ii);
		int len=strlen(s);
		s[len]='+';
		int ans=0;
		for(int i=0;i<len;i++)
		{
			if(s[i]=='+' && s[i+1]=='-')ans++;
			else if(s[i]=='-' && s[i+1]=='+')ans++;
		}
		printf("%d\n",ans);
	}
	
	return 0;
}
