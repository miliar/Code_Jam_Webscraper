#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int n, x, s[20000];
int c[20000], cnt[20000];


int main()
{
    //freopen("A-small-attempt0.in","r", stdin);
    //freopen("A-small-attempt0.out", "w", stdout);
    int T; scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas)
    {
        scanf("%d %d", &n, &x);
        for (int i = 0; i < n; ++i)
            scanf("%d", &s[i]);

        sort(s, s+n);
        int ans = 1;
        c[1] = s[n-1];
        cnt[1] = 1;
        for (int i = n - 2; i >= 0; --i)
        {
            bool put = false;
            for (int j = 1; j <= ans; ++j)
            {
                if (c[j] + s[i] <= x && cnt[j] < 2)
                {
                    c[j] += s[i];
                    cnt[j]++;
                    put = true;
                    break;
                }
            }
            if (!put)
            {
                //printf("i = %d, new box\n", i);
                ans++;
                c[ans] = s[i];
                cnt[ans] = 1;
            }
        }
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
