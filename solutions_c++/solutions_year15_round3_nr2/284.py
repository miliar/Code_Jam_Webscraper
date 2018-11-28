#include <cassert>
#include <cstdio>
#include <ctime>
#include <cstdlib>
#include <climits>
#include <cstddef>
#include <cctype>
#include <cmath>
#include <cstring>
#include <fstream>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <iterator>
#include <numeric>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <vector>
#include <bitset>
#include <list>
#include <string>
#include <functional>
#include <utility>
using namespace std;
typedef long long llint;
int const N = 100;
int nk, l, s;
char keys[N + 10];
char word[N + 10];
int fail[N + 10];
int dp[N + 1][N + 1];
bool ok[N + 1][N + 1];
double prob[N + 1][N + 1];
double ss[N + 1][N + 1];
void readin()
{
    scanf("%d%d%d", &nk, &l, &s);
    scanf("%s", keys + 1);
    scanf("%s", word + 1);
}
void kmp()
{
    fail[1] = 0;
    for (int i = 2, j = 0; i <= l; ++i)
    {
        while (j > 0 && word[j + 1] != word[i])
        {
            j = fail[j];
        }
        if (word[j + 1] == word[i])
        {
            ++j;
        }
        fail[i] = j;
    }
}
double solve()
{
    kmp();
    // max
    memset(dp, 0, sizeof(dp));
    memset(ok, false, sizeof(ok));
    ok[0][0] = true;
    for (int i = 1; i <= s; ++i)
    {
        for (int j = 0; j <= min(i - 1, l); ++j)
        {
            for (int k = 1; k <= nk; ++k)
            {
                if (!ok[i - 1][j])
                {
                    continue;
                }
                int j_copy = j;
                if (j_copy == l)
                {
                    j_copy = fail[j_copy];
                }
                while (j_copy != 0 && word[j_copy + 1] != keys[k])
                {
                    j_copy = fail[j_copy];
                }
                if (word[j_copy + 1] == keys[k])
                {
                    ++j_copy;
                }
                dp[i][j_copy] = max(dp[i][j_copy], dp[i - 1][j] + (j_copy == l ? 1 : 0));
                ok[i][j_copy] = true;
            }
        }
    }
    int r_max = *(max_element(dp[s], dp[s] + (l + 1)));
    // prob
    for (int i = 0; i <= s; ++i)
    {
        for (int j = 0; j <= l; ++j)
        {
            prob[i][j] = 0.0;
        }
    }
    prob[0][0] = 1.0;
    for (int i = 1; i <= s; ++i)
    {
        for (int j = 0; j <= min(i - 1, l); ++j)
        {
            for (int k = 1; k <= nk; ++k)
            {
                int j_copy = j;
                if (j_copy == l)
                {
                    j_copy = fail[j_copy];
                }
                while (j_copy != 0 && word[j_copy + 1] != keys[k])
                {
                    j_copy = fail[j_copy];
                }
                if (word[j_copy + 1] == keys[k])
                {
                    ++j_copy;
                }
                prob[i][j_copy] += prob[i - 1][j] / nk;
            }
        }
    }
    // sum
    for (int i = 0; i <= s; ++i)
    {
        for (int j = 0; j <= l; ++j)
        {
            ss[i][j] = 0.0;
        }
    }
    for (int i = 1; i <= s; ++i)
    {
        for (int j = 0; j <= min(i - 1, l); ++j)
        {
            for (int k = 1; k <= nk; ++k)
            {
                int j_copy = j;
                if (j_copy == l)
                {
                    j_copy = fail[j_copy];
                }
                while (j_copy != 0 && word[j_copy + 1] != keys[k])
                {
                    j_copy = fail[j_copy];
                }
                if (word[j_copy + 1] == keys[k])
                {
                    ++j_copy;
                }
                if (abs(prob[i][j_copy]) > 1e-7)
                {
                    ss[i][j_copy] += (ss[i - 1][j] + (j_copy == l ? 1 : 0)) * (prob[i - 1][j] / nk) / prob[i][j_copy];
                }
            }
        }
    }
    // ans
    double r_sum = 0.0;
    for (int j = 0; j <= l; ++j)
    {
        r_sum += ss[s][j] * prob[s][j];
    }
    return r_max - r_sum;
}
int main()
{
    int tc;
    scanf("%d", &tc);
    for (int cc = 1; cc <= tc; ++cc)
    {
        readin();
        printf("Case #%d: %.7f\n", cc, solve());
    }
    return 0;
}
