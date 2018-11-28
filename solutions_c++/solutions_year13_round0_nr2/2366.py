#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;
int t,n,m,g[105][105],x[105],y[105];
int main()
{
    freopen("in2","r",stdin);
    freopen("out2","w",stdout);
    scanf("%d",&t);
    for(int I=1;I<=t;++I)
    {
        scanf("%d%d",&n,&m);
        memset(x,0,sizeof(x)); memset(y,0,sizeof(y));
        for(int i=0;i<n;++i)
            for(int j=0;j<m;++j)
            {
                scanf("%d",&g[i][j]);
                x[i]=max(x[i],g[i][j]);
                y[j]=max(y[j],g[i][j]);
            }
        bool f=1;
        for(int i=0;i<n;++i)
            for(int j=0;j<m;++j) if(g[i][j]<min(x[i],y[j])) {f=0; break;}
        printf("Case #%d: %s\n",I,f?"YES":"NO");
    }
    return 0;
}
