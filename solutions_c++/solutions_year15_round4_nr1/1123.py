#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <cmath>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <deque>
#include <cstring>
#include <memory.h>
#include <bitset>
#include <time.h>
#define sf(x) scanf("%d", &x)
#define sff(x) scanf("%lf", &x)
#define sfc(x) scanf(" %c", &x)
#define pf(x) printf("%d ", x)
#define pff(x) printf("%lf", x)
#define pfc(x) printf("%c", x)
#define pfs(x) printf("%s", x)
#define sfl(x) scanf("%I64d", &x)
#define sfl2(x,y) scanf("%I64d %I64d", &x,&y)
#define ENDL printf("\n")
#define INF 2147483647
#define pf2(x,y) printf("%d %d ", x,y)
#define sf2(x,y) scanf("%d %d", &x,&y)
#define pb(x) push_back(x)
#define ppb() pop_back()
#define mp(x,y) make_pair(x,y)
#define sf3(x,y,z) scanf("%d %d %d", &x,&y,&z)
#define print(x) puts(#x)
#define error(x) cerr<<#x<<' '<<x<<'\n'


using namespace std;

typedef long long ll; 
typedef unsigned int uint;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<double, double> pdd;
typedef vector<int> vec;



int n,m;

char p[102][102];
int res;
int h[102][2];
int v[102][2];


int main()
{



    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    /**/
    
    int T;
    sf(T);
    for(int t=1; t<=T; t++)
    {
    	sf2(n,m);
    	res=0;
    	memset(h,0,sizeof(h));
    	memset(v,0,sizeof(v));
    	for(int i=1; i<=n; i++)
    	{
    		v[i][0]=INF;
    	}
    	for(int j=1; j<=m; j++)
    	{
    		h[j][0]=INF;
    	}
    	for(int i=1; i<=n; i++)
    	{
    		for(int j=1; j<=m; j++)
    		{
    			sfc(p[i][j]);
    		}
    	}
    	for(int i=1; i<=n; i++)
    	{
    		for(int j=1; j<=m; j++)
    		{
    			if(p[i][j]!='.')
    			{
    				h[j][0]=min(h[j][0],i);
    				h[j][1]=max(h[j][1],i);
    				v[i][0]=min(v[i][0],j);
    				v[i][1]=max(v[i][1],j);
    			}
    		}
    	}
    	for(int i=1; i<=n; i++)
    	{
    		for(int j=1; j<=m; j++)
    		{
    			if(p[i][j]=='<')
    			{
    				if(v[i][0]>=j)
    				{
    					if(v[i][1]>j||h[j][0]<i||h[j][1]>i)
    					{
    						res++;
    					}
    					else
    					{
    						goto asd;
    					}
    				}
    			}
    			else if(p[i][j]=='>')
    			{
    				if(v[i][1]<=j)
    				{
    					if(v[i][0]<j||h[j][0]<i||h[j][1]>i)
    					{
    						res++;
    					}
    					else
    					{
    						goto asd;
    					}
    				}
    			}
    			else if(p[i][j]=='^')
    			{
    				if(h[j][0]>=i)
    				{
    					if(v[i][1]>j||v[i][0]<j||h[j][1]>i)
    					{
    						res++;
    					}
    					else
    					{
    						goto asd;
    					}
    				}
    			}
    			else if(p[i][j]=='v')
    			{
    				if(h[j][1]<=i)
    				{
    					if(v[i][1]>j||v[i][0]<j||h[j][0]<i)
    					{
    						res++;
    					}
    					else
    					{
    						goto asd;
    					}
    				}
    			}
    		}
    	}
    	printf("Case #%d: %d\n",t,res);
    	continue;
asd:	printf("Case #%d: IMPOSSIBLE\n",t);
    }
    
    return 0;
}





