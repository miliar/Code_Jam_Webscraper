#include<iostream>
#include<cstdio>
#include<cstdlib>
using namespace std;
#define LL long long
#define MAX 1000000
int complete(LL x[])
{
    for(int i=0;i<10;i++)
    {
        if(x[i]==0)
            return 0;
    }
    return 1;
}
int main()
{
    LL t,n,l,p,i,k,m,d,flag;
    LL x[10];
    p=0;n=0;
    scanf("%lld",&p);
	t=0;
    while(t<p)
    {
        ++t;flag=0;
        scanf("%lld",&n);m=0;k=0;
        for(i=0;i<10;i++)
        x[i]=0;
        if(n==0)
        {
            printf("Case #%d: INSOMNIA\n",t);
            flag=1;
        }
        if(flag==0)
        {   while(!complete(x))
            {
                m=m+n;
                k=m;
                while(k!=0)
                {
                    d=k%10;
                    x[d]=1;
                    k=k/10;
                }
                //printf("%d %d\n",m,n);
            }
            printf("Case #%lld: %lld\n",t,m);
        }
    }
    return 0;
}
