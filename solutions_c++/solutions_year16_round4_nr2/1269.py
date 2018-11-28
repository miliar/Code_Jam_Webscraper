#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

const int MaxN = 20;

int n,k;
double res,p[MaxN],f[MaxN][MaxN];
bool use[MaxN];

void Calc()
{
    int i,j,l;
    f[0][0] = 1.0;
    for (i=1,j=0; i<=n; i++)
        if(use[i])
        {
            j++;
            for(l=0;l+l<=k;l++)
                f[j][l] = f[j-1][l]*(1-p[i])+f[j-1][l-1]*p[i];
        }
    if(f[k][k/2]>res) res=f[k][k/2];
    return;
}

void DFS(int x,int y)
{
    if(y==k) {Calc(); return;}
    if(x+k==n+y+1)
    {
        use[x] = true;
        DFS(x+1,y+1);
        use[x] = false;
        return;
    }
    else
    {
        use[x] = true;
        DFS(x+1,y+1);
        use[x] = false;
        DFS(x+1,y);
        return;
    }
}

int main()
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    
    int T,idx;
    scanf("%d",&T);
    for (idx=1; idx<=T; idx++)
    {
        scanf("%d%d",&n,&k); res = 0.0;
        for (int i=1; i<=n; i++)
            scanf("%lf",p+i);
        DFS(1,0);
        printf("Case #%d: %.9lf\n",idx,res);
    }
    
    return 0;
}
