#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

const int maxn = 1000 + 10;

double a[maxn];
double b[maxn];

bool used[maxn];

int main()
{
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

    int T;
    scanf("%d", &T);
    for (int test = 1; test <= T; ++test)
    {
        int n;
        scanf("%d", &n);
        for (int i = 0; i < n; ++i)
            scanf("%lf", &a[i]);
        for (int i = 0; i < n; ++i)
            scanf("%lf", &b[i]);

        sort(a, a + n);
        sort(b, b + n);

        int ans1 = 0;
        int ans2 = 0;

        memset(used, false, sizeof(used));

        for (int i = 0; i < n; ++i)
        {
            bool ok = false;
            for (int j = 0; j < n; ++j)
            {
                if (!used[j] && b[j] > a[i])
                {
                    ok = true;
                    used[j] = true;
                    break;
                }
            }
            if (!ok)
            {
                for (int j = 0; j < n; ++j)
                    if (!used[j])
                    {
                        used[j] = true;
                        break;
                    }
                ++ans2;
            }
        }

        memset(used, false, sizeof(used));
        for (int j = 0; j < n; ++j)
        {
            bool ok = false;
            for (int i = 0; i < n; ++i)
            {
                if (!used[i] && a[i] > b[j])
                {
                    ok = true;
                    used[i] = true;
                    ++ans1;
                    break;
                }
            }
            if (!ok)
            {
                break;
            }
        }

        printf("Case #%d: %d %d\n", test, ans1, ans2);
    }

    return 0;
}
