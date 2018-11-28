#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
using namespace std;
long long r;
bool ok(long long mid,long long t)
{
    long long sum=2*mid*mid;
    long long toadd=t-sum;
    if (toadd<0) return false;
    long long div=toadd/(2+2*r-3);
    return div>=mid;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int ii=1; ii<=T; ii++)
    {
        long long t;
        scanf("%I64d%I64d",&r,&t);
        long long L=0,R=2000000000LL;
        while (L+1<R)
        {
            long long mid=(L+R)/2;
            if (ok(mid,t)) L=mid;
            else R=mid;
        }
        printf("Case #%d: ",ii);
        if (ok(R,t)) printf("%I64d\n",R);
        else printf("%I64d\n",L);
    }
    return 0;
}

