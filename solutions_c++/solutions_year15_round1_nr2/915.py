#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <queue>
#include <cmath>
#include <vector>
#include <string>
#include <iomanip>
#define Mod (1000000007LL)
#define eps (1e-12)
#define Pi (acos(-1.0))
using namespace std;

int ans;
int b;
long long n;
long long m[1100];
long long tmp;
long long L,R,mid;
long long check(long long x)
{
    long long f=0;
    for(int i=0;i<b;i++)
    f+=x/m[i]+1LL;
    return f;
}
int main()
{
    freopen("B-large (1).in","r",stdin);
    freopen("B-large (1).out","w",stdout);
    int T,cas=0;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d%lld",&b,&n);
        for(int i=0;i<b;i++)
        scanf("%lld",&m[i]);
        if(n<=b)
        {
            ans=n;
        }else
        {
            L=0;R = n*m[0];
            while(L+1LL<R)
            {
                mid = (L+R)/2LL;
                tmp = check(mid);
                if(tmp<n) L=mid;
                else R=mid;
            }
            tmp = check(R)-n;
            for(int i=b-1;i>=0;i--)
            {
                if(R%m[i]) continue;
                else
                {
                    tmp--;
                    if(tmp<0) {ans=i+1;break;}
                }

            }
        }
        printf("Case #%d: %d\n",++cas,ans);
    }
    return 0;
}
