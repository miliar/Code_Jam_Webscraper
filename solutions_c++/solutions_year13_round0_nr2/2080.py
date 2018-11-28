#define filer() freopen("f.in","r",stdin)
#define filew() freopen("out.txt","w",stdout)
#include<iostream>
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<queue>
#include<stack>
#include<string>
#include<vector>
#include <map>
#define INF 1<<29
#define PI pair<int,int>

#define SET(a, x) memset((a), (x), sizeof(a))
#define pb push_back
#define i64 long long
#define EPS (1e-9)
using namespace std;
typedef vector<int> VI;
typedef vector<PI> vii;
//i64 INF=(i64)((i64)1<<(i64)59);

int N,M,grid[110][110];
int mxr[110];
int mxc[110];

int main()
{
    //filer();
    //filew();
    int T,cas=0;
    int i,j;
    scanf("%d",&T);
    while(T--)
    {
       scanf("%d%d",&N,&M);
       for(i=1;i<=N;i++)
       {
           for(j=1;j<=M;j++)scanf("%d",&grid[i][j]);
       }
       for(i=1;i<=N;i++)
       {
           mxr[i]=0;
           for(j=1;j<=M;j++)
           {
               mxr[i]=max(mxr[i],grid[i][j]);
           }
       }
       for(j=1;j<=M;j++)
       {
           mxc[j]=0;
           for(i=1;i<=N;i++)mxc[j]=max(mxc[j],grid[i][j]);
       }
       bool t=1;
       for(i=1;i<=N;i++)
       {
           for(j=1;j<=M;j++)
           {
               if(grid[i][j]>=mxr[i] || grid[i][j]>=mxc[j])continue;
               t=0;
               break;
           }
           if(!t)break;
       }
       if(t)printf("Case #%d: YES\n",++cas);
       else printf("Case #%d: NO\n",++cas);

    }

    return 0;
}
/*
Test Case:

*/

