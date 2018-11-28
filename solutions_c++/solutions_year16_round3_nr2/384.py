#include <bits/stdc++.h>
using namespace std;
typedef long long ull;
const int maxn=60;
ull p2[maxn];
bool mat[maxn][maxn];
void solve()
{
    int n;
    ull m;
    scanf("%d%lld",&n,&m);
    memset(mat,0,sizeof(mat));
    for(int i=0;i<n-1;i++)
        for(int j=i+1;j<n-1;j++)
            mat[i][j]=1;
    for(int i=n-2;i>=0;i--)
        if(m>=p2[i])
        {
            mat[i][n-1]=1;
            m-=p2[i];
        }
    if(m)    printf("IMPOSSIBLE\n");
    else     printf("POSSIBLE\n");
    if(m==0)
    {
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
                if(mat[i][j])    printf("1");
                else    printf("0");
            printf("\n");
        }
    }
}
int main()
{
    int T;
    scanf("%d",&T);
    p2[0]=p2[1]=1;
    for(int i=2;i<maxn;i++)
        p2[i]=p2[i-1]*2;
    for(int i=1;i<=T;i++)
    {
        printf("Case #%d: ",i);
        solve();
    }
    return 0;
}
