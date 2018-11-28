#include<cstdio>
#include<cstring>
#include<cmath>
#include<iostream>
#include<algorithm>
#include<set>
#include<map>
#include<stack>
#include<vector>
#include<queue>
#include<string>
#include<sstream>
#define eps 1e-9
#define FOR(i,j,k) for(int i=j;i<=k;i++)
#define MAXN 1005
#define MAXM 40005
#define INF 0x3fffffff
using namespace std;
typedef long long LL;
int i,j,k,n,m,x,y,T,ans,big,cas,num,len;
bool flag;
char s[2000];
int cur;
int main()
{
		//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	scanf("%d",&T);
	while (T--)
	{
		scanf("%d",&n);
		scanf("%s",s);
		cur=0;
		ans=0;
		while (s[n]=='0' && n>0) n--; 
		for (i=0;i<=n;i++)
		{
			if (cur<i)
			{
				ans+=i-cur;
				cur=i;
			}
			
			cur+=s[i]-'0';
		}
		printf("Case #%d: %d\n",++cas,ans);
	}
	return 0;
}
