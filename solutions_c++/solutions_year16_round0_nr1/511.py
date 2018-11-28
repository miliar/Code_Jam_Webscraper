// A CZM1.0
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<string>
#include<vector>
#include<stack>
#include<queue>
#include<map>
#include<algorithm>
using namespace std;

#define oo 1000000000
#define eps 1e-8
#define PI acos(-1.0)
const static int maxN = 1000;
typedef long long INT64;
typedef INT64 LL;

//#pragma comment(linker, "/STACK:1024000000,1024000000")

//#define __DEBUG__
#ifdef __DEBUG__
//#define _DP(fmt, arg...) printf("[%s %s %d] " fmt, __FILE__, __FUNCTION__, __LINE__, ##arg)
#define _DP(fmt, arg...) printf("[%d] " fmt, __LINE__, ##arg)
#else
#define _DP(fmt, arg...)
#endif

bool vis[10];

int calc(int n)
{
    if (!n) return -1;
    int cnt = 0;
    memset(vis, 0, sizeof(vis));
    for (int i = 1; i < 10000; i++)
    {
        int m = n * i;
        while (m)
        {
            cnt += !vis[m % 10];
            vis[m % 10] = true;
            m /= 10;
        }
        if (cnt == 10)
        {
            return n * i;
        }
    }
    return -1;
}

int main()
{
    int T;
    int cas = 1;
    scanf("%d", &T);
    while (T--)
    {
        int N;
        scanf("%d", &N);
        int ans = calc(N);
        if (ans == -1)
        {
            printf("Case #%d: INSOMNIA\n", cas++);
        }
        else
        {
            printf("Case #%d: %d\n", cas++, ans);
        }
    }
    return 0;
}
