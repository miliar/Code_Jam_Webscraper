#include<cstdio>
long long CP;
long long cpow (int b,int p)
{
    if (p==0)
        return 1;
    long long d=cpow(b,p/2);
    if (p%2==1)
        return d*d*b;
    return d*d;
}
long long findans1 (int n,long long p)
{
    if (p==1)
        return 0;
    if (p==CP)
        return CP-1;
    long long a=1,ma=CP/2,b=0,mb=2;
    while (a+ma<=p)
    {
        a += ma;
        ma /= 2;
        b += mb;
        mb *= 2;
    }
    return b;
}
long long findans2 (int n,long long p)
{
    if (p==1)
        return 0;
    if (p==CP)
        return CP-1;
    long long a=1,b=0,mb=CP/2;
    while (2*a<=p)
    {
        a *= 2;
        b += mb;
        mb /= 2;
    }
    return b;
}
int main()
{
    freopen("B-large (1).in","r",stdin);
    freopen("B-large (1).out.txt","w",stdout);
    int T,tt,n;
    long long p;
    scanf("%d",&T);
    for (tt=1;tt<=T;tt++)
    {
        scanf("%d %I64d",&n,&p);
        CP = cpow(2,n);
        printf("Case #%d: %I64d %I64d\n",tt,findans1(n,p),findans2(n,p));
    }
    return 0;
}
