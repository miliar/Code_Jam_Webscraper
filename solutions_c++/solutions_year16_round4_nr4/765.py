#include <cstdio>
#include <algorithm>

using namespace std;

int aux[10][10],v1[10],vaz[10],n,bun;
char sir[10][10];

void back(int poz)
{
    if(!bun) return;
    if(poz==n) return;
    int s=0;
    for(int i=0;i<n;i++)
        if(!vaz[i] && aux[v1[poz]][i]) s++;
    if(!s)
    {
        bun=0;
        return;
    }
    for(int i=0;i<n;i++)
        if(!vaz[i] && aux[v1[poz]][i])
        {
            vaz[i]=1;
            back(poz+1);
            vaz[i]=0;
        }
}

int main()
{
    freopen("file.in", "r", stdin);
    freopen("file.out", "w", stdout);
    int test;
    scanf("%d",&test);
    for(int t=1;t<=test;t++)
    {
        scanf("%d",&n);
        for(int i=0;i<n;i++)
            scanf("\n%s",sir[i]);
        int lim=1<<(n*n),sol=1000000000;
        for(int mask=0;mask<lim;mask++)
        {
            int nr=0,ok=1;
            for(int i=0;i<n;i++)
                for(int j=0;j<n;j++)
                    if(mask&(1<<(n*i+j)))
                    {
                        if(sir[i][j]=='1') ok=0;
                        else {nr++;aux[i][j]=1;}
                    }
                    else aux[i][j]=sir[i][j]-'0';
            if(!ok) continue;
            if(nr>=sol) continue;
            for(int i=0;i<n;i++) v1[i]=i;
            do
            {
                bun=1;
                back(0);
                if(!bun) {ok=0;break;}
            }while(next_permutation(v1,v1+n));
            if(ok) sol=min(sol,nr);
        }
        printf("Case #%d: %d\n",t,sol);
    }
    return 0;
}
