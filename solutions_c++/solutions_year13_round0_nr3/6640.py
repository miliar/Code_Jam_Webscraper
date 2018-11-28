#include<iostream>
#include<cstdio>
#include<map>
#include<algorithm>
#include<sstream>
#include<string>
#include<cstring>
#include<cmath>
#include<queue>
#include<cstdlib>
#include<vector>
#define MAXLEN 10000000
#define INF 10000000000
#define WHITE 0
#define GRAY 1
#define BLACK 2

using namespace std;
bool palin(long long a)
{
    long long b=0;
    long long n=a;
    while(a>0)
    {
        b = b*10 + a%10;
        a = a/10;
    }
    return(n==b);
}
long long z[MAXLEN];
int main()
{
    z[0] = 0;

    int count = 0;
    int size = 0;
    for(int i=1;i<=MAXLEN;i++)
    {
        if(palin(i) && palin((long long)i*(long long)i))
        {
            z[size]=i*i;
            size++;
        }
    }
    int t;
    scanf("%d",&t);
    count = 1;
    while(t--)
    {
        long long a,b;
        //cout<<"enter\n";
        scanf("%lld%lld",&a,&b);
       // cout<<a<<" "<<b<<"\n";
        //cout<<a<<" "<<b<<"\n";
        int n=0;
       // cout<<z[a]<<" "<<z[b]<<"\n";
       for(int i=0;i<size;i++)
       {
           if(z[i]>=a && z[i]<=b)
           n++;
       }
        printf("Case #%d: %d\n",count,n);
        count++;
    }
    return 0;
}
