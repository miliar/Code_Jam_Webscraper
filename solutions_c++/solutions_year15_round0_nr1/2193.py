#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

int num[1005];
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T;
    cin >> T;
    for (int cas = 1; cas <= T; cas++)
    {
            int n;
            cin >> n;

            string ss;
            cin >> ss;

            for (int i = 0; i <= n; i++) num[i] = ss[i] - 48;

            int ans = 0;
            int sum = num[0];
            for (int i = 1; i <= n; i++)
            {
                    if (num[i]) ans = max(ans, i - sum);
                    sum += num[i];
            }
            printf("Case #%d: %d\n", cas, ans);
    }

    return 0;
}
