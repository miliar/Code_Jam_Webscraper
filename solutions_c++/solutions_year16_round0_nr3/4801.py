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
ll dis[12];
ll trans(ll s,int base)
{
    ll ans = 0;
    for(int i = 0; i < 16; i++)
    {
        if(s%2 == 1)
            ans += (ll)pow(base*1.0,i);
        s >>= 1;
    }
    return ans;
}

bool isprime(ll x,int b)
{
    for(ll i = 2; i <= (ll)sqrt(x*1.0); i++)
    {
        if(x%i == 0)
        {
            dis[b] = i;
            return 0;
        }
    }
    return 1;
}
int main()
{
    freopen("D:c.in","r",stdin);
    freopen("D:c.out","w",stdout);
    int t,cas;
    Ri(t);
    for(cas = 1; cas <= t; cas++)
    {
        int n,j;
        scanf("%d %d",&n,&j);
        printf("Case #1:\n");
        int num = 0;
        ll s = 1<<15;
        s++;
        while(num<j)
        {
            CLR(dis,0);
            for(int base = 2; base <= 10; base++)
            {
                ll a = trans(s,base);
                if(isprime(a,base))
                    break;
            }
            if(dis[10]!=0)
            {
                char s2[20];
                itoa(s,s2,2);
                printf("%s",s2);
                num++;
                for(int i = 2; i <= 10; i++)
                    printf(" %I64d",dis[i]);
                printf("\n");
            }
            s += 2;
        }

    }
    return 0;
}
