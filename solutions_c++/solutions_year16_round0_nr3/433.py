// C CZM2.0
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

map<INT64, INT64> add_weight;

INT64 get_weight(int b, INT64 xorv)
{
    map<INT64, INT64>::iterator it = add_weight.find(xorv * 100 + b);
    if (it != add_weight.end())
    {
        return it->second;
    }
    INT64 ret = 0;
    INT64 t = xorv;
    INT64 w = 1;
    INT64 lw = 1;
    while (t)
    {
        if (t & 1)
        {
            ret -= (t & 1) * w;
            lw = w;
        }
        t >>= 1;
        w = w * b;
    }
    ret += 2 * lw;
    add_weight[xorv * 100 + b] = ret;
    return ret;
}

int dig[100];
int pri[11];
INT64 val[11];

void to_dig(INT64 d)
{
    int cnt = 0;
    while (d)
    {
        dig[cnt++] = d & 1;
        d >>= 1;
    }
}

void pre_val(int N)
{
    for (int b = 2; b <= 10; b++)
    {
        val[b] = 0;
        for (int k = N - 1; k >= 0; k--)
        {
            val[b] = (val[b] * b + dig[k]);
        }
    }
}

void add_val(INT64 xorv)
{
    for (int b = 2; b <= 10; b++)
    {
        val[b] += get_weight(b, xorv);
    }
}

bool divisor(INT64 sum, int b)
{
    for (INT64 i = 2; i * i <= sum; i++)
    {
        if (sum % i == 0)
        {
            pri[b] = i;
            return true;
        }
    }
    return false;
}

bool judge()
{
    for (int b = 2; b <= 10; b++)
    {
        if (!divisor(val[b], b))
        {
            return false;
        }
    }
    return true;
}

const static int maxDiv = 3;

int divi[11][maxDiv] = {
        {}, // 0
        {}, // 1
        {3, 5, 7}, // 2
        {2, 5, 7}, // 3
        {3, 5, 7}, // 4
        {2, 3, 7}, // 5
        {7, 5, 11}, // 6
        {2, 3, 5}, // 7
        {3, 5, 17}, // 8
        {2, 7}, // 9
        {3, 7, 11} // 10
    };
int rem[11][maxDiv];

void pre_rem(int N)
{
    for (int b = 2; b <= 10; b++)
    {
        for (int di = 0; di < maxDiv; di++)
        {
            if (!divi[b][di]) break;
            rem[b][di] = 0;
            for (int k = N - 1; k >= 0; k--)
            {
                rem[b][di] = (rem[b][di] * b + dig[k]) % divi[b][di];
            }
        }
    }
}

bool judge_rem()
{
    for (int b = 2; b <= 10; b++)
    {
        bool flag = false;
        for (int di = 0; di < maxDiv; di++)
        {
            if (!divi[b][di]) break;
            if (!rem[b][di])
            {
                flag = true;
                pri[b] = divi[b][di];
                break;
            }
        }
        if (!flag)
        {
            return false;
        }
    }
    return true;
}

void add_rem(INT64 xorv)
{
    for (int b = 2; b <= 10; b++)
    {
        for (int di = 0; di < maxDiv; di++)
        {
            if (!divi[b][di]) break;
            rem[b][di] = ((INT64)rem[b][di] + get_weight(b, xorv)) % divi[b][di];
        }
    }
}

void print_rem()
{
    for (int b = 2; b <= 10; b++)
    {
        for (int di = 0; di < maxDiv; di++)
        {
            if (!divi[b][di]) continue;
            printf("(%d, %d, %d)\n", b, divi[b][di], rem[b][di]);
        }
    }
}

int main()
{
    int T;
    int cas = 1;
    scanf("%d", &T);
    while (T--)
    {
        int N, J;
        scanf("%d%d", &N, &J);
        printf("Case #%d:\n", cas++);
        if (N > 13)
        {
            INT64 sta = (1LL << (N - 1)) | 1;
            INT64 end = 1LL << N;
            INT64 d = sta;
            INT64 p = d;
            to_dig(d);
            pre_rem(N);
            while (d < end && J)
            {
                if (judge_rem())
                {
                    to_dig(d);
                    for (int k = N - 1; k >= 0; k--)
                    {
                        printf("%d", dig[k]);
                    }
                    for (int b = 2; b <= 10; b++)
                    {
                        printf(" %d", pri[b]);
                    }
                    puts("");
                    J--;
                }
                d += 2;
                add_rem(p ^ d);
                p = d;
            }
        }
        else
        {
            INT64 sta = (1LL << (N - 1)) | 1;
            INT64 end = 1LL << N;
            INT64 d = sta;
            INT64 p = d;
            to_dig(d);
            pre_val(N);
            while (d < end && J)
            {
                if (judge())
                {
                    to_dig(d);
                    for (int k = N - 1; k >= 0; k--)
                    {
                        printf("%d", dig[k]);
                    }
                    for (int b = 2; b <= 10; b++)
                    {
                        printf(" %d", pri[b]);
                    }
                    puts("");
                    J--;
                }
                d += 2;
                add_val(p ^ d);
                p = d;
            }
        }
    }
    return 0;
}
