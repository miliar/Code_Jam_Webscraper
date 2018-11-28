#include <cstdio>
#include <vector>
#include <cmath>
#include <iostream>
#include <algorithm>
using namespace std;
#define LL long long
#define FOR(i,a,b) for(LL i=a; i<=b; i++)
#define REP(i,n) FOR(i,0,n-1)
#define ss(n) scanf("%lld",&n)
int main()
{
    //freopen("C-large-1.in","r",stdin);
    //freopen("fair2.out","w",stdout);
    LL tc, a, b, ans, cnt = 1;
    ss(tc);
    LL palin_sq[40]={1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001,
    1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521,
    400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004,
    1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201,
     1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004, 100000020000001
};
    while(tc--)
    {
        ss(a); ss(b);
        ans = 0;
        for(int i=0; i<40; i++)
        {
            if(palin_sq[i]>=a && palin_sq[i]<=b) ans += 1;
            else if(palin_sq[i] > b) break;
        }
        printf("Case #%lld: %lld\n",cnt,ans);
        cnt += 1;
    }
return 0;
}
