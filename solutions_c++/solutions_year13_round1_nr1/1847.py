#include <iostream>
#include <cstdio>
#include <cmath>
#define pi acos(-1)
using namespace std;
long long int r,t;
long long int process()
{
    long long int s=0,c=0,tmp=1;
    while(1)
    {
        s+=(2*r+tmp);
        if(s>t) break;
        c++;
        tmp+=4;
    }
    return c;
}
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int T,Case;
    scanf("%d",&T);
    Case=T;
    while(T--)
    {
        scanf("%lld%lld",&r,&t);
        printf("Case #%d: %lld\n",Case-T,process());
    }
    return 0;
}
