#include <cstdio>
#include <iostream>
using namespace std;
const int L = 1005;
int level;
char lnum[L];

int main()
{
    #ifdef LOCAL
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    #endif // LOCAL
    int T;
    scanf("%d", &T);
    for (int k = 0; k != T; ++k)
    {
        scanf("%d%s", &level, lnum);
        int cnt = 0, ans = 0;
        for (int i = 1; i <= level; ++i)
        {
            cnt += lnum[i - 1] - '0';
            if (cnt < i)
            {
                ans += i - cnt;
                cnt = i;
            }
        }
        printf("Case #%d: %d\n", k + 1, ans);
    }
    return 0;
}
