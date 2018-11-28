#include <iostream>
#include <stdio.h>

using namespace std;
int T, n;
char s[1009];
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt","w", stdout);
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas)
    {
        scanf("%d %s", &n, s);
        int ans = 0, sum = 0;;
        for (int i = 0; i <= n; ++i)
        {
            if (sum < i)
            {
                ans += i - sum;
                sum = i;
            }
            sum += s[i] - '0';
        }

        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
