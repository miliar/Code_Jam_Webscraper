#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int T, n, r, a;
    bool visit[18];
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t)
    {
        scanf("%d", &r);
        memset(visit, false, sizeof(visit));
        for (int i = 1; i <= 4; ++i)
        {
            for (int j = 1; j <= 4; ++j)
            {
                scanf("%d", &a);
                if (r == i)
                {
                    visit[a] = true;
                }
            }
        }
        int ans, cnt = 0;
        scanf("%d", &r);
        for (int i = 1; i <= 4; ++i)
        {
            for (int j = 1; j <= 4; ++j)
            {
                scanf("%d", &a);
                if (r == i)
                {
                    if (visit[a])
                    {
                        ++cnt;
                        ans = a;
                    }
                }
            }
        }
        printf("Case #%d: ", t);
        if (cnt == 0)
        {
            puts("Volunteer cheated!");
        }
        else if (cnt == 1)
        {
            printf("%d\n", ans);
        }
        else
        {
            puts("Bad magician!");
        }
    }
    return 0;
}
