#include <bits/stdc++.h>
#define nnu 1000000
using namespace std;
long long vect[20],x[20],k,i,j,l,n,a,nr,numar,nrt,ok,aa[nnu],p[nnu],nn,ookk;
long long valid(long long k)
{
    if(x[1]==1)return 0;
    if(k==n&&x[k]==1)return 0;
    return 1;
}
long long putere(long long x, long long y)
{
    long long p;
    p=1;
    while(y>0)
    {
        if(y%2==1)p=p*x;
        x=x*x;
        y=y/2;
    }
    return p;
}
int main()
{
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    nn=0;
    nn++;
    aa[nn]=2;
    for(i=3;i<=nnu;i=i+2)
    {
        if(p[i]==0)
        {
            nn++;
            aa[nn]=i;
            for(j=i+i;j<=nnu;j=j+i)
                p[j]=1;
        }
    }
    scanf("%lld",&nrt);
    scanf("%lld%lld",&n,&j);
    printf("Case #1:");
    k=1;x[k]=0;
    while(k>0)
    {
        ok=0;
        while(ok==0&&k<=n&&x[k]<2)
        {
            x[k]++;
            if(valid(k))ok=1;
        }
        if(ok==1)
        {
            if(k==n)
            {
                for(i=1;i<=nr;i++)
                    vect[i]=0;
                nr=0;
                for(l=2;l<=10;l++)
                {
                    a=0;
                    for(i=1;i<=n;i++)
                    {
                       if(x[i]==2) a=a+putere(l,n-i);
                    }
                    ookk=0;
                    for(i=1;i<=nn;i++)
                    {
                        if(a%aa[i]==0&&a!=aa[i])
                        {
                            ookk=1;
                            nr++;
                            vect[nr]=aa[i];
                            break;
                        }
                    }
                    if(ookk==0)
                    {
                        for(i=1000001;i*i<a;i=i+2);
                        {
                            if(a%i==0)
                            {
                                nr++;
                                vect[nr]=i;
                                break;
                            }
                        }
                    }
                }
                if(nr==9)
                {
                    printf("\n");
                    for(i=1;i<=n;i++)
                        printf("%lld",x[i]-1);
                        printf(" ");
                    for(i=1;i<=nr;i++)
                        printf("%lld ",vect[i]);
                    numar++;
                    if(numar==j)break;
                }
            }
            else {k++;x[k]=0;}
        }
        else k--;
    }
return 0;
}
