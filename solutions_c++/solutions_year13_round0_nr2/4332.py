#include<cstdlib>
#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<set>
#include<map>
#include<list>
#include<queue>
#include<vector>
#define LL long long
#define inf 0x7fffffff
#define E 1e-9
#define M 100
#define N 150
using namespace std;
int m,n,t;
int ma[N][N];
int dx[4]= {-1,0,1,0};
int dy[4]= {0,1,0,-1};
int flag;
int main()
{
#ifndef ONLINE_JUDGE
    freopen("ex.in","r",stdin);
    freopen("ex.out","w",stdout);
#endif
    scanf("%d%*c",&t);
    int ncase=0;
    while(t--)
    {
        scanf("%d%d",&n,&m);
        for (int i=0; i<n; ++i )
            for(int j=0; j<m; ++j)
                scanf("%d",&ma[i][j]);
        flag=1;
        for (int i=0; i<n; ++i )
        {
            int maxv=0;
            for(int j=0; j<m; ++j)
            maxv=max(maxv,ma[i][j]);
            for(int j=0; j<m; ++j)
            {
                if(ma[i][j]<maxv)
                {
                    for(int k=0;k<n;++k)
                    if(ma[k][j]>ma[i][j])
                    flag=0;
                }
            }
        }
        printf("Case #%d: ",++ncase);
        if(flag)
            printf("YES\n");
        else
            printf("NO\n");
    }
    return 0;
}
