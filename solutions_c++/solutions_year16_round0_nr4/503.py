// D CZM1.0
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

#define __DEBUG__
#ifdef __DEBUG__
//#define _DP(fmt, arg...) printf("[%s %s %d] " fmt, __FILE__, __FUNCTION__, __LINE__, ##arg)
#define _DP(fmt, arg...) printf("[%d] " fmt, __LINE__, ##arg)
#else
#define _DP(fmt, arg...)
#endif

INT64 calc(int K, int C, int p)
{
    INT64 ret = p;
    int c = min(K, C);
    for (int i = 1; i < c; i++)
    {
        if (p + i >= K)
        {
            ret = ret * K + K - 1;
            break;
        }
        else
        {
            ret = ret * K + p + i;
        }
    }
    return ret;
}

int main()
{
    int T;
    int cas = 1;
    scanf("%d", &T);
    while (T--)
    {
        int K, C, S;
        scanf("%d%d%d", &K, &C, &S);
        if (C * S < K)
        {
            printf("Case #%d: IMPOSSIBLE\n", cas++);
        }
        else
        {
            printf("Case #%d:", cas++);
            for (int i = 0; i < K; i += C)
            {
                printf(" %lld", calc(K, C, i) + 1);
            }
            puts("");
        }
    }
    return 0;
}
