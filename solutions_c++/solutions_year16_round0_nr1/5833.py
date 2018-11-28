#include <iostream>
#include <cstdio>
#include <stack>
#include <cstring>
#include <queue>
#include <algorithm>
#include <cmath>
//#include <unordered_map>
//#define lson x<<1
//#define rson x<<1|1
//#define mid ((lt[x].l+lt[x].r)/2)
//#define ID(x, y) ((x)*m+(y))
//#define CHECK(x, y) ((x)>=0 && (x)<n && (y)>=0 && (y)<m)
using namespace std;
typedef long long LL;
typedef pair<int,int> PII;
const int INF=0x3f3f3f3f;
void Open()
{
    #ifndef ONLINE_JUDGE
        freopen("C:/Users/qingp/Downloads/A-large.in", "r",stdin);
        freopen("A-large.out","w",stdout);
    #endif // ONLINE_JUDGE
}
bool vis[11];
LL check(LL x)
{
    memset(vis, 0, sizeof(vis));
    LL num = 10;
    LL p = 1;
    LL tmp = 0;
    while(true)
    {
        if(p > 1000000) return -1;
        tmp = x*p;
        while(tmp)
        {
            if(vis[tmp%10] == 0) num--;
            vis[tmp%10] = 1;
            tmp /= 10;
            if(num == 0) return x*p;
        }
        p++;
    }
}
int main()
{
//    Open();
    LL T;
    scanf("%I64d", &T);
    LL cas = 0;
    while(T--)
    {
        cas++;
        LL x;
        scanf("%I64d", &x);
        if(x == 0) printf("Case #%I64d: INSOMNIA\n", cas);
        else printf("Case #%I64d: %I64d\n", cas, check(x));
    }
    return 0;
}
