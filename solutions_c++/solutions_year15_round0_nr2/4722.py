#include<cstdio>
#include<cstring>
using namespace std;
int Q,n,t,i,j,s,rez,ma,k,x,v[1004];

void jum(int k);
void treime(int k);

int main()
{
    freopen("input","r",stdin);
    freopen("output","w",stdout);
    scanf("%d\n",&Q);
    while(t<Q)
    {
        t++;
        printf("Case #%d: ",t);
        scanf("%d ",&n);
        ma=0;
        for(i=1;i<=n;i++)
        {
            scanf("%d",&x);
            v[x]++;
            if(ma<x)ma=x;
        }
        rez=ma;
        s=0;
        jum(ma);
        treime(ma);
        printf("%d\n",rez);
        memset(v,0,sizeof(v));
    }
    return 0;
}

void jum(int k)
{
    if(k>1)
    {
        if(rez>k+s)rez=k+s;
        v[k/2]+=v[k];
        v[k/2+k%2]+=v[k];
        s+=v[k];
        jum(k-1);
        treime(k-1);
        s-=v[k];
        v[k/2]-=v[k];
        v[k/2+k%2]-=v[k];
    }
}
void treime(int k)
{
    if(k>1)
    {
        if(rez>k+s)rez=k+s;
        if(k%3==0)v[k/3]+=v[k]*3;
        else if(k%3==1){ v[k/3]+=v[k]*2; v[k/3+1]+=v[k]; }
        else if(k%3==2){ v[k/3]+=v[k]; v[k/3+1]+=v[k]*2; }
        s+=2*v[k];
        jum(k-1);
        treime(k-1);
        s-=2*v[k];
        if(k%3==0)v[k/3]-=v[k]*3;
        else if(k%3==1){ v[k/3]-=v[k]*2; v[k/3+1]-=v[k]; }
        else if(k%3==2){ v[k/3]-=v[k]; v[k/3+1]-=v[k]*2; }
    }
}
