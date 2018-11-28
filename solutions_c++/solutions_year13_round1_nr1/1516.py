#include <iostream>
#include <cstdio>
#include <cstring>
#define Pi 3.1415927
using namespace std;

int main()
{
    //freopen("a.in","r",stdin);
    //freopen("a.out","w",stdout);
    int testcase;
    scanf("%d",&testcase);
    for(int z=1;z<=testcase;z++)
    {
        long long r,t;
        scanf("%lld %lld",&r,&t);
        long long sum=0;
        long long cnt=0;
        while((sum+2*r+1)<=t)
        {
            sum=sum+2*r+1;
            r+=2;
            cnt++;
        }
        printf("Case #%d: %lld\n",z,cnt);
    }
    return 0;
}
