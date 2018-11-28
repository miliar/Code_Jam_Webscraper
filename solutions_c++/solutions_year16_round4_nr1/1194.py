#include <cstdio>

using namespace std;

int v[10010],bate[3][3],sol[10010],n,gasit;

int pune(int poz)
{
    while(poz%2 && poz>1)
    {
        if(v[poz]==v[poz-1]) return 0;
        v[poz/2]=bate[v[poz-1]][v[poz]];
        poz/=2;
    }
    return 1;
}

void back(int poz,int p,int r,int s)
{
    if(gasit) return;
    if(poz==(1<<n)+1)
    {
        for(int i=(1<<(n+1))-(1<<n);i<(1<<(n+1));i++)
            sol[i-((1<<(n+1))-(1<<n))+1]=v[i];
        gasit=1;
    }
    else
    {
        int a=(1<<(n+1))-1-((1<<n)-poz);
        if(p>0)
        {
            v[a]=0;
            if(pune(a)) back(poz+1,p-1,r,s);
        }
        if(r>0)
        {
            v[a]=1;
            if(pune(a)) back(poz+1,p,r-1,s);
        }
        if(s>0)
        {
            v[a]=2;
            if(pune(a)) back(poz+1,p,r,s-1);
        }
    }
}

int main()
{
    freopen("file.in", "r", stdin);
    freopen("file.out", "w", stdout);
    int test;
    bate[0][1]=0;
    bate[0][2]=2;
    bate[1][0]=0;
    bate[1][2]=1;
    bate[2][0]=2;
    bate[2][1]=1;
    scanf("%d",&test);
    for(int t=1;t<=test;t++)
    {
        int r,p,s;
        scanf("%d%d%d%d",&n,&r,&p,&s);
        gasit=0;
        back(1,p,r,s);
        if(gasit)
        {
            printf("Case #%d: ",t);
            for(int i=1;i<=(1<<n);i++)
                if(sol[i]==0) printf("P");
                else if(sol[i]==1) printf("R");
                else printf("S");
            printf("\n");
        }
        else printf("Case #%d: IMPOSSIBLE\n",t);
    }
    return 0;
}
