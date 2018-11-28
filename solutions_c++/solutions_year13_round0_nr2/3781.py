#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>
#include <queue>
#include <cstdio>
#include <set>
#include <map>
#include <cstdlib>
#include <cstring>
#include <stack>
#include <cassert>
#include <limits.h>

typedef unsigned long long ULL;
typedef long long LL;

#define MIN(a,b) (a<b?a:b)
#define MAX(a,b) (a>b?a:b)
#define ABS(a) ((a>0)?a:-a)

#define SZ(a) ((int)a.size())
#define PB(a) push_back(a)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define REP(i,n) FOR(i,0,(int)(n-1))
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define printv(v) REP(i,SZ(v))printf("%d ",v[i]);
#define mp(a,b) make_pair(a,b)
#define PII pair<int,int>
#define MOD 1000000007
using namespace std;
int rowmax[123],colmax[123];
int ar[120][120];
int main()
{
    freopen("a1.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,n,m,ctr=0;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d %d",&n,&m);
        for(int i=0;i<max(n,m);i++)
        {
            rowmax[i]=INT_MIN;
            colmax[i]=INT_MIN;
        }
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                scanf("%d",&ar[i][j]);

                if(ar[i][j]>rowmax[i])
                {
                    rowmax[i]=ar[i][j];
                }
                if(ar[i][j]>colmax[j])
                {
                    colmax[j]=ar[i][j];
                }
            }
        }
        int f=0;
        for(int i=0;i<n && f!=1;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(ar[i][j]<rowmax[i] && ar[i][j]<colmax[j])
                {
                    f=1;
                    break;
                }
            }
        }
        ctr++;
        printf("Case #%d: ",ctr);
        if(f==1)
        printf("NO\n");
        else printf("YES\n");
    }
    return 0;
}
