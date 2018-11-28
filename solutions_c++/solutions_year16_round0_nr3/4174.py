#include<cstdio>
#include<cmath>

int t,n,j,co;
int b[35];
long long v[35];
long long prime(long long x)
{
    if(x%2==0)
    {
        return 2;
    }
    long long v=sqrt(x)+1;
    for(long long i=3;i<=v;i+=2)
    {
        if(((x/i)*i)==x)
        {
            return i;
        }
    }
    return -1;
}

void af()
{
    for(int i=2;i<=10;i++)
    {
        long long nr=1,tt=0;
        for(int j=n;j>=1;j--)
        {
            if(b[j]==1) tt+=nr;
            nr*=i;
        }
        v[i]=prime(tt);
        if(v[i]==-1)
        {
            return;
        }
    }
    for(int i=1;i<=n;i++)
    {
        printf("%d",b[i]);
    }
    for(int i=2;i<=10;i++)
    {
        printf(" %lld",v[i]);
    }
    printf("\n");
    co++;
    if(co==j)
    {
        return;
    }
}

void bk(int pos)
{
    if(pos==n)
    {
        af();
    }
    else
    {
        b[pos]=1;
        bk(pos+1);
        if(co==j)
        {
            return;
        }

        b[pos]=1;
        bk(pos+1);
        if(co==j)
        {
            return;
        }
    }
}

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);

    scanf("%d",&t);

    for(int i=1;i<=t;i++)
    {
        scanf("%d %d",&n,&j);
        co=0;
        b[1]=1;
        b[n]=1;

        printf("Case #%d:\n",i);

        bk(2);
    }
}
