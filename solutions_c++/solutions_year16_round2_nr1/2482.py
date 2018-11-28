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

char dig[10][10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int alp_dig[26];
int alp_cnt[26];
int alp_step[26];
bool vis[10];
int step_cnt;

void pre()
{
    int cnt = 0;
    for (int i = 0; i < 10; i++)
    {
        int len = strlen(dig[i]);
        for (int j = 0; j < len; j++)
        {
            alp_cnt[dig[i][j] - 'A']++;
            cnt++;
        }
    }
    step_cnt = 1;
    while (cnt)
    {
        for (char c = 'A'; c <= 'Z'; c++)
        {
            if (alp_cnt[c - 'A'] == 1)
            {
                for (int i = 0; i < 10; i++)
                {
                    if (vis[i]) continue;
                    bool flag = false;
                    int len = strlen(dig[i]);
                    for (int j = 0; j < len; j++)
                    {
                        if (dig[i][j] == c)
                        {
                            alp_dig[c - 'A'] = i;
                            alp_step[c - 'A'] = step_cnt;
                            flag = true;
                            break;
                        }
                    }
                    if (flag)
                    {
                        vis[i] = true;
                        for (int j = 0; j < len; j++)
                        {
                            alp_cnt[dig[i][j] - 'A']--;
                            cnt--;
                        }
                    }
                }
            }
        }
        for (char c = 'A'; c <= 'Z'; c++)
        {
            if (alp_step[c - 'A'] == step_cnt)
            _DP("%c %d %d\n", c, alp_cnt[c - 'A'], alp_dig[c - 'A']);
        }
        _DP("%d\n", cnt);
        step_cnt++;
    }
}

char s[100000];
int res[10];
int sum[26];

int main()
{
    pre();
    int T;
    int cas = 1;
    scanf("%d", &T);
    while (T--)
    {
        scanf("%s", s);
        memset(sum, 0, sizeof(sum));
        memset(res, 0, sizeof(res));
        memset(vis, 0, sizeof(vis));
        for (int i = strlen(s) - 1; i >= 0; i--)
        {
            sum[s[i] - 'A']++;
        }
        for (int p = 1; p < step_cnt; p++)
        {
            for (char c = 'A'; c <= 'Z'; c++)
            {
                if (alp_step[c - 'A'] == p && !vis[ alp_dig[c - 'A'] ])
                {
                    _DP("oo %c %d %d\n", c, alp_dig[c - 'A'], sum[c - 'A']);
                    int i = alp_dig[c - 'A'];
                    vis[i] = true;
                    int num = sum[c - 'A'];
                    int len = strlen(dig[i]);
                    for (int j = 0; j < len; j++)
                    {
                        sum[dig[i][j] - 'A'] -= num;
                    }
                    res[ alp_dig[c - 'A'] ] = num;
                }
            }
        }
        printf("Case #%d: ", cas++);
        for (int i = 0; i < 10; i++)
        {
            for (int j = 0; j < res[i]; j++)
            {
                printf("%d", i);
            }
        }
        puts("");
    }
    return 0;
}
