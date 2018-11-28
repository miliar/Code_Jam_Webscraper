#include<stdio.h>
#include<algorithm>
using namespace std;
int caz;

int l[1010],c[1010];
int v[1010][1010];
int nr[1010][1010];
int T;

int N,M;

int same()
{
    for(int i=1;i<=N;++i)
        for(int j=1;j<=M;++j)
        {
            if(v[i][j]!=nr[i][j])
                return 0;
        }
    return 1;
}


void make()
{
int ret;
    for(int i=1;i<=N;++i)
    {
        ret=-1;
        for(int j=1;j<=M;++j)
        {
            ret=max(ret,v[i][j]);
        }
        l[i]=ret;
    }
for(int i=1;i<=M;++i)
    {
        ret=-1;
        for(int j=1;j<=N;++j)
        {
            ret=max(ret,v[j][i]);
        }
        c[i]=ret;
    }
    for(int i=1;i<=N;++i)
    {

        for(int j=1;j<=M;++j)
        {
            nr[i][j]=min(nr[i][j],l[i]);
        }
    }
for(int i=1;i<=M;++i)
    {
        for(int j=1;j<=N;++j)
        {
            nr[j][i]=min(nr[j][i],c[i]);
        }
    }
    if(same())
        printf("Case #%d: YES\n",caz);
    else printf("Case #%d: NO\n",caz);
}
void init()
{
    for(int i=1;i<=100;++i)
        for(int j=1;j<=100;++j)
        {
            c[i]=-1;
            l[i]=-1;
            nr[i][j]=101;
        }
}
int main()
{
freopen("b.in","r",stdin);
freopen("b.out","w",stdout);
scanf("%d",&T);
while(T--)
{
++caz;
init();
scanf("%d%d",&N,&M);

for(int i=1;i<=N;++i)
    for(int j=1;j<=M;++j)
    {
        scanf("%d",&v[i][j]);
    }

make();
}

return 0;
}
