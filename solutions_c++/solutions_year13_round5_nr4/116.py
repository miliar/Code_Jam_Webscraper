#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <string>

using namespace std;
char s[100];

long double dp[1 << 21];
const long double inf = 10000000000000;
int n;

int main()
{
    freopen("in.txt", "r", stdin);
    int T, ca = 0;
    scanf("%d", &T);
    while (T--)
    {
        scanf("%s", s);
        n = strlen(s);
        int mark0 = 0;
        for (int i = 0; i < n; i++)
            if (s[i] == 'X') mark0 |= 1 << i;
        for (int mark = 0; mark < (1 << n); mark++)
        {
            int tmp = (mark) & (mark0);
        //  int tmp;
            if (tmp != mark0)
                dp[mark] = -inf;
            else dp[mark] = 0;
        }
        int ii, k;
        for (int mark = 0; mark < (1 << n) - 1; mark++)
        {
            if (dp[mark] < (long double)-1000000000) continue;
            for (int pos = 0; pos < n; pos++)
            {
                mark0 = mark;
                for (int _i = pos; _i < pos + n; _i++)
                {
                    ii = _i;
                    if (ii >= n) ii -= n;
                    if (mark & ( 1 << ii) == 1)
                        continue;
                    else
                    {
                            mark0 |= 1 << ii;
                            k = _i - pos;
                            break;
                    }
                }
                dp[mark0] += dp[mark] + (long double)(n - k);
            }
        }

        printf("Case #%d: %.10lf\n", ++ca, (double)dp[(1 << n) - 1]);



    }
    return 0;
}

