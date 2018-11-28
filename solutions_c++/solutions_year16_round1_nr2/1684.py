// B CZM1.0
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
const static int maxN = 10000;
typedef __int64 INT64;
typedef INT64 LL;

//#pragma comment(linker, "/STACK:1024000000,1024000000")

//#define __DEBUG__
#ifdef __DEBUG__
//#define _DP(fmt, arg...) printf("[%s %s %d] " fmt, __FILE__, __FUNCTION__, __LINE__, ##arg)
#define _DP(fmt, arg...) printf("[%d] " fmt, __LINE__, ##arg)
#else
#define _DP(fmt, arg...)
#endif

int app[maxN];

int main()
{
    int T;
    int cas = 1;
    scanf("%d", &T);
    while (T--)
    {
        int N;
        scanf("%d", &N);
        memset(app, 0, sizeof(app));
        for (int i = 0; i < 2 * N - 1; i++)
        {
            for (int j = 0; j < N; j++)
            {
                int tmp;
                scanf("%d", &tmp);
                app[tmp]++;
            }
        }
        printf("Case #%d:", cas++);
        for (int i = 0; i < maxN; i++)
        {
            if (app[i] % 2)
            {
                printf(" %d", i);
            }
        }
        puts("");
    }
    return 0;
}
