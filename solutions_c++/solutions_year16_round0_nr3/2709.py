#include <stdio.h>
#include <string.h>
#include <math.h>
#include <iostream>
#include <algorithm>

using namespace std;

int t,n,l,ans,a[101];
long long s[101];

long long prime(long long x)
{   
    for(long long i=2;i<sqrt(x)+1;i++)
        if(i<x && x%i==0)
            return i;
    return 0;
}

long long trans(int b)
{
    long long r=0,k=1;
    for(int i=l;i>=1;i--,k*=b)
        r+=k*a[i];
    return r;
}

int main()
{
 //   freopen("input.txt","r",stdin);
  //  freopen("output.txt","w",stdout);
    bool flag;
    scanf("%d",&t);
    for(int cas=1;cas<=t;++cas)
    {
        scanf("%d%d",&l,&n);
        printf("Case #1:\n");
        for(int i=(1<<(l-1))+1;i<(1<<l) && n>0;i+=2)
        {
            int k=i;
            for(int j=l;j>=1;--j)
            {
                a[j]=k%2;
                k>>=1;
            }
            flag=0;
            for(int j=2;j<=10;j++)
                if((s[j]=prime(trans(j)))==0)
                {
                    flag=1;
                    break;
                }
            if(flag==0)
            {
                n--;
                for(int j=1;j<=l;j++)
                    printf("%d",a[j]);
                for(int j=2;j<=10;j++)
                    printf(" %lld",s[j]);
                printf("\n");
            }
        }
    }
    return 0;
}
