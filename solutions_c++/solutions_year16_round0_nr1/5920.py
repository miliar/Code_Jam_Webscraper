#include <iostream>
/*每天在CF上刷B,C，D题各一道*/
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <vector>
#include <string>
#define INF 0x3f3f3f3f
#define eps 1e-8
#define SIZE (2000+10)
#define Ri(a) scanf("%d", &a)
#define Rl(a) scanf("%I64d", &a)
#define Rf(a) scanf("%lf", &a)
#define Rs(a) scanf("%s", a)
#define Pi(a) printf("%d\n", (a))
#define Pf(a) printf("%lf\n", (a))
#define Pl(a) printf("%I64d\n", (a))
#define Ps(a) printf("%s\n", (a))
#define CLR(a, b) memset(a, (b), sizeof(a))
#define INT_MAX 2147483647
#define LL_MAX 9223372036854775807
#define ll __int64
#define lson l, mid, rt<<1
#define rson mid+1, r, rt<<1|1
#define PI acos(-1.0)
const long long MOD = 1000000007;
using namespace std;
ll n;
int main()
{
  //  freopen("D:a.in","r",stdin);
   // freopen("D:a.out","w",stdout);
    int t,cas;
    Ri(t);
    for(cas = 1; cas <= t; cas++)
    {
        int vis[10];
        CLR(vis,0);
        Rl(n);
        if(n == 0)
        {
            printf("Case #%d: INSOMNIA\n",cas);
            continue;
        }
        int num = 0;
        ll nn = 0;
        while(num<10)
        {
            nn += n;
            ll now = nn;
            while(now>0)
            {
                if(vis[now%10] == 0)
                {
                    vis[now%10] = 1;
                    num++;
                }
                now /= 10;
            }
            if(nn+n<nn)
            {
                num = 0;
                break;
            }
        }
        if(num == 0)
            printf("Case #%d: INSOMNIA\n",cas);
        else
            printf("Case #%d: %I64d\n",cas,nn);
    }
    return 0;
}
