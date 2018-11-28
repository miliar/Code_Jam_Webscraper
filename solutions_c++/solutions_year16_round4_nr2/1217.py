#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

double p[16],q[16];
int pos[16];
double mp,tp;
int n,k;

void DFS(int s,int c,double x)
{
    if(s==k)
    {
        if(c==k/2)
        {
            tp=tp+x;
        }
        return;
    }
    DFS(s+1,c,x*q[pos[s]]);
    DFS(s+1,c+1,x*p[pos[s]]);
}

void DFS(int s,int c)
{
    if(c==k)
    {
        tp=0;
        DFS(0,0,1);
        mp=max(mp,tp);
        return;
    }
    if(s>c+n-k)
    {
        return;
    }
    DFS(s+1,c);
    pos[c]=s;
    DFS(s+1,c+1);
    pos[c]=-1;
}

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int c,t,i;
    scanf("%d",&t);
    for(c=0;c<t;c++)
    {
        memset(pos,-1,sizeof(pos));
        scanf("%d %d",&n,&k);
        for(i=0;i<n;i++)
        {
            scanf("%lf",&p[i]);
            q[i]=1.0-p[i];
        }
        mp=0;
        DFS(0,0);
        printf("Case #%d: %.8f\n",c+1,mp);
    }
    return 0;
}
