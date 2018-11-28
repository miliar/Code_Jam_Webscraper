#include <iostream>
#include <stdio.h>
using namespace std;
bool is(long long x)
{
    int num[20];
    int len=0;
    while(x)
    {
        num[len++]=x%10;
        x/=10;
    }
    for(int i=0;i<len-i-1;i++)
    {
        if(num[i]!=num[len-i-1])return false;
    }
    return true;
}
long long data[100];
int main()
{
    freopen("C-large-1.in","r",stdin);
    //freopen("out.txt","w",stdout);
    //freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    //cout << is(123454321) << endl;
    int cnt=0;
    for(long long i=1;i<=10000000;i++)
    {
        if(is(i) && is (i*i))
        {
            data[cnt++]=i*i;
            //cout << i*i << endl;
        }
    }
//    for(int i=0;i<cnt;i++)
//    {
//        cout << data[i] << endl;
//    }
    //cout << cnt << endl;
    int cas;
    scanf("%d",&cas);
    for(int ci=1;ci<=cas;ci++)
    {
        long long a,b;
        scanf("%lld%lld",&a,&b);
        //cout << a << ' ' << b << endl;
        int ans=0;
        for(int i=0;i<cnt;i++)
        {
            if(data[i]>=a && data[i]<=b) ans++;
            if(data[i]>b) break;
        }
        printf("Case #%d: %d\n",ci,ans);
    }
}
