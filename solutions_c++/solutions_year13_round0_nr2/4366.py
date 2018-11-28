#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#define DBLE 1e-8
#define PI 3.1415926535898
#define INF 1000000000
#define MAXN 110
#define MP(x,y) (make_pair((x),(y)))
#define FI first
#define SE second
using namespace std;
int num[MAXN][MAXN];
bool ty[MAXN][MAXN];
int main()
{
//    freopen("J:\\MyDocument\\Code\\input.txt","r",stdin);
//    freopen("J:\\MyDocument\\Code\\output.txt","w",stdout);
    int ncase,n,m;
    bool f1,f2;
    scanf("%d",&ncase);
    for(int h=1;h<=ncase;++h)
    {
        f1=1;
        memset(ty,0,sizeof(ty));
        scanf("%d%d",&n,&m);
        for(int i=0;i<n;++i)
            for(int j=0;j<m;++j)
                scanf("%d",&num[i][j]);
        for(int i=0;i<n;++i)
        {
            int nn=-INF;
            for(int j=0;j<m;++j)
                nn=max(nn,num[i][j]);
            for(int j=0;j<m;++j)
                if(nn<=num[i][j])
                    ty[i][j]=1;
        }
        for(int j=0;j<m;++j)
        {
            int nn=-INF;
            for(int i=0;i<n;++i)
                nn=max(nn,num[i][j]);
            for(int i=0;i<n;++i)
                if(nn<=num[i][j])
                    ty[i][j]=1;
        }
        for(int i=0;i<n;++i)
            for(int j=0;j<m;++j)
                f1&=ty[i][j];
        printf("Case #%d: %s\n",h,f1?"YES":"NO");
    }
    return 0;
}

