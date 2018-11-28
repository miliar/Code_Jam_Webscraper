#include<iostream>
#include<vector>
#include<string.h>
#include<stdio.h>
#include<math.h>
using namespace std;
int n;
vector<long int> prime;
void sieve(long int x)
{
    bool m[x+1];
    memset(m,true,sizeof(m));
    long int i,j;
    for(i=2;i*i<x;i++)
    {
        if(m[i]==true)
        {
            for(j=i*2;j<x;j+=i)
                m[j]=false;
        }
    }
    for(i=2;i<x;i++)
    {
        if(m[i]==true)
        {
            prime.push_back(i);
        }
    }
    return ;
}
int divisor(long long x)
{
    int k;
    {
        for(int i=0;(i<prime.size())&&(prime[i]<x);i++)
        {
            k=x%prime[i];
           // printf("%d ",prime[i]);
            if(k==0)
                return prime[i];
        }
    }
    return 0;
}
bool check(int x)
{
    int i,c=0;
    for(i=0;i<n;i++)
    {
        if(((x>>i)&1)==1)
            c++;
    }
    if(c%3==0)
        return true;
    return false;
}
long long getint(int x,int b)
{
    long long k=0,c=1,i;
    for(i=0;i<n;i++)
    {
        k+=((x>>i)&1)*c;
        c*=b;
    }
    return k;
}
int main()
{
    long int k;
    k=floor(sqrt(1110710958665))+1;
    sieve(k);
    int m,c,t,j;
    int d[11];
    long long int a,i;
    scanf("%d",&t);
    for(c=1;c<=t;c++)
    {
        scanf("%d %d",&n,&j);
        printf("Case #%d:\n",c);
        m=1;
        m|=(1<<(n-1));
        while(j>0)
        {
            m+=2;
          //  memset(d,0,sizeof(d));
            if(check(m))
                d[2]=divisor(m);
            else
                continue;
            if(d[2]==0||d[2]==m)
                continue;
            for(i=3;i<10;i++)
            {
             //   printf("*");
                a=getint(m,i);
              //  printf("-");
            //    if(i==6)
              //      printf("%lld ",a);
                d[i]=divisor(a);
                if(d[i]==0)
                    break;
            }
          //  printf("\n");
            if(d[i]==0&&i<10)
                continue;
            d[10]=3;
            for(i=(n-1);i>=0;i--)
                printf("%d",((m>>i)&1));
            for(i=2;i<=10;i++)
                printf(" %d",d[i]);
            printf("\n");
            j--;
        }
    }
    return 0;
}
