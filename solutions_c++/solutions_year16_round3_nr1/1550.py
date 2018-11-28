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

int P[100];

int main()
{
    int T;
    int cas = 1;
    scanf("%d", &T);
    while (T--)
    {
        int sum = 0;
        int N;
        int max1, max2;
        int maxp1, maxp2;
        scanf("%d", &N);
        for (int i = 0; i < N; i++)
        {
            scanf("%d", &P[i]);
            sum += P[i];
        }
        printf("Case #%d:", cas++);
        while (sum > 0)
        {
            max1 = max2 = 0;
            for (int i = 0; i < N; i++)
            {
                if (P[i] > max1)
                {
                    max2 = max1;
                    maxp2 = maxp1;
                    max1 = P[i];
                    maxp1 = i;
                }
                else if (P[i] > max2)
                {
                    max2 = P[i];
                    maxp2 = i;
                }
            }
            printf(" %c", maxp1 + 'A');
            sum--;
            P[maxp1]--;
            if (sum != 2)
            {
                printf("%c", maxp2 + 'A');
                sum--;
                P[maxp2]--;
            }
        }
        puts("");
    }
    return 0;
}
