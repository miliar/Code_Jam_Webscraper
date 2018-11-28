#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
const double pi=3.14159265;
long long R,t;

bool Cal(long long n,long long R,long long t){
    t-=(2*n*n + 2*n);
    long long ans=2*R*n-3*n;
    if(ans <= t)
        return true;
    return false;
}

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("test.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cas=1;cas<=T;++cas){
        scanf("%lld %lld",&R,&t);
        long long l=0,r=20000000;
        while(l<=r){
            long long mid=(l+r)/2;
            if(Cal(mid,R,t))
                l=mid+1;
            else
                r=mid-1;
        }
        printf("Case #%d: %lld\n",cas,r);
    }
    return 0;
}
