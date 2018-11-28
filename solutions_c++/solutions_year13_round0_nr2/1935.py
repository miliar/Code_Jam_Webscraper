/* ***************************
Author: Abhay Mangal (abhay26)
*************************** */
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <cstring>
#include <cassert>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
using namespace std;
 #define tr(container, it) \
	for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define maX(a,b) (a) > (b) ? (a) : (b)
#define pii pair< int, int >
#define pip pair< int, pii >
#define FOR(i,n) for(int i=0; i<(int)n ;i++)
#define pb push_back
//int dx[]= {-1,0,1,0};
//int dy[]= {0,1,0,-1};
int ar[105][105];
int grid[105][105];
int minR[105],maxR[105];
int minC[105],maxC[105];
int type[105][105];
int n,m;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out2.txt","w",stdout);
	int t;
	scanf("%d",&t);
	int cas=0;
	while(t--)
	{
        cas++;
        scanf("%d %d",&n,&m);
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                scanf("%d",&ar[i][j]);
                grid[i][j] = 100;
            }
        }
        while(1)
        {
            int f1=0;
            for(int i=0;i<n;i++)
            {
                int max1 = 0;
                for(int j=0;j<m;j++)
                {
                    max1 = max(max1,ar[i][j]);
                }
                for(int j=0;j<m;j++)
                {
                    if(grid[i][j] > max1)
                    {
                        grid[i][j] = max1;
                        f1=1;
                    }
                }
            }
            int f2=0;
            for(int j=0;j<m;j++)
            {
                int max1 = 0;
                for(int i=0;i<n;i++)
                {
                    max1 = max(max1,ar[i][j]);
                }
                for(int i=0;i<n;i++)
                {
                    if(grid[i][j] > max1)
                    {
                        grid[i][j] = max1;
                        f2=1;
                    }
                }
            }
            if(!f1 && !f2)
            break;
        }
        int flag = 0;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(ar[i][j]!=grid[i][j])
                {
                    flag = 1;
                    break;
                }
            }
            if(flag) break;
        }
        printf("Case #%d: ",cas);
        if(flag)
        {
            printf("NO\n");
        }
        else
            printf("YES\n");
	}
return 0;
}
