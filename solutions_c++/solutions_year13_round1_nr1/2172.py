#include <cstdio>
#include <cmath>
#include <iostream>
using namespace std;
#define LL long long
#define FOR(i,a,b) for(LL i=a; i<=b; i++)
#define ss(n) scanf("%lld",&n)
int main()
{
    //freopen("new2.in","r",stdin);
    //freopen("new2.out","w",stdout);
    LL tc, r, t, outer, inner, sum, check, count, k = 0;
    ss(tc);
    while(tc--)
    {
        k++;
        ss(r); ss(t);
        outer = r + 1; inner = r;
        sum = 0; check = 0; count = 0;
        while(1)
        {
         check += (outer*outer) - (inner*inner);
         if(check <= t)
         sum = check;
         else break;
         count++;
         outer += 2; inner += 2;
        }
        printf("Case #%lld: %lld\n",k,count);
    }
return 0;
}
