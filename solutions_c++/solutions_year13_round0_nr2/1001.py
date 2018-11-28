#include <set>
#include <cmath>
#include <stack>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <numeric>
#include <vector>
#include <ctime>
#include <queue>
#include <list>
#include <map>
#define pi acos(-1)
#define INF 0x7fffffff
#define clr(x)  memset(x,0,sizeof(x));
#define clrto(x,siz,y)  for(int xx=0;xx<=siz;xx++)  x[xx]=y;
#define clrset(x,siz)  for(int xx=0;xx<=siz;xx++)  x[xx]=xx;
#define clr_1(x) memset(x,-1,sizeof(x));
#define clrvec(x,siz) for(int xx=0;x<=siz;xx++)  x[xx].clear();
#define fop   freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
#define myprogram By_135678942570
#define clrcpy(x,siz,y)  for(int xx=0;xx<siz;xx++)  x[xx]=y[xx];
#define pb push_back
using namespace std;
int main()
{
    int t,cas=0;
    fop;
    scanf("%d",&t);
    while(t--)
    {
    	int n,m;
    	int maxn1[102]={0};
    	int maxn2[102]={0};
    	scanf("%d%d",&n,&m);
    	int mp[102][102]={0};
    	for(int i=1;i<=n;i++)
    		for(int j=1;j<=m;j++)
    		{
    			scanf("%d",&mp[i][j]);
    			maxn1[i]=max(maxn1[i],mp[i][j]);
    			maxn2[j]=max(maxn2[j],mp[i][j]);
    		}
    	int flag=1;
    	for(int i=1;i<=n;i++)
    		for(int j=1;j<=m;j++)
    			if(maxn1[i]>mp[i][j]&&maxn2[j]>mp[i][j])
    			{
    				flag=0;
    				break;
    			}
    	printf("Case #%d: %s\n",++cas,flag?"YES":"NO");
    }
    return 0;
}
