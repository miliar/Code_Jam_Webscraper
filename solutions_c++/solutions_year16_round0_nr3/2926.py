#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;
long long n,Prim,M,cate,x[40],ras[40],baza[40][40],c[3051004];
bool p[34333340];
void bck(int k)
{
    if(k==0)
    {
        long long nr;
        for(int i=2;i<=10;i++)
        {
            nr=0LL;
            for(int j=0;j<n;j++)
                nr+=baza[i][j]*x[j];
            ras[i]=0;
            for(int d=1;d<=Prim;d++)
                if(nr%c[d]==0&&c[d]<n)
                {
                    ras[i]=c[d];
                    break;
                }
            if(ras[i]==0)return ;
        }
        cate++;
        printf("\n");
        for(int i=n-1;i>=0;i--)
            printf("%lld",x[i]);
        for(int i=2;i<=10;i++)
            printf(" %lld",ras[i]);
        /*printf("\n");
        for(int i=2;i<=10;i++)
        {
            nr=0LL;
            for(int j=0;j<=n;j++)
                nr+=baza[i][j]*x[j];
            printf("%lld\n",nr);
        }*/
        return;
    }
    if(cate<M)
    {
        x[k]=0;
        bck(k-1);
    }
    if(cate<M)
    {
        x[k]=1;
        bck(k-1);
    }
}
int main()
{
    freopen("input","r",stdin);
    freopen("output","w",stdout);
    int Q;
    Prim++;
    c[Prim]=2;
    for(long long i=3;i<=34333335;i+=2)
    {
        if(p[i]==0)
        {
            if(i<=5860)for(long long j=i*i;j<=34333335;j=j+i)
                p[j]=1;
            Prim++;
            c[Prim]=i;
        }
    }
    for(int i=2;i<=10;i++)
    {
        baza[i][0]=1;
        for(int j=1;j<=18;j++)
            baza[i][j]=baza[i][j-1]*i;
    }
    scanf("%d\n",&Q);
    for(int test=1;test<=Q;test++)
    {
        printf("Case #%d: ",test);

        scanf("%lld %lld",&n,&M);
        x[0]=1;
        x[n-1]=1;
        bck(n-2);
        printf("\n");
    }
    return 0;
}

