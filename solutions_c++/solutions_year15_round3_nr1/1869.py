#include <bits/stdc++.h>

using namespace std;

int T, m, n, w, ans;

int get(int a, int b)
{
    return (a >> b) & 1;
}
int Check(int s, int len)
{
    for (int i = 0; i < len - w + 1; i++)
    {
        int d = 0;
        for (int j = 0; j < w; j++)
            d += get(s, i + j);
        if (d == 0) return 0;
    }

    return 1;
}

int Count(int s, int len)
{
    int ans = 0;
    for (int i = 0; i < len; i++)
        ans += get(s, i);
    return ans;
}

int OnBit(int a, int b)
{
    return a | (1 << b);
}

int main()
{
    freopen("in.in", "r", stdin);
    freopen("ou.out", "w", stdout);
    scanf("%d", &T);
    for (int itest = 0; itest < T; itest++)
    {
        scanf("%d %d %d", &m, &n, &w);
        ans = n;
        for (int s = 0; s < (1 << n); s++)
            if (Check(s, n))
            {
                for (int i = 0; i < n; i++)
                    if (get(s, i) == 1)
                    {
                        int tmp = s;
                        int L = max(i - w + 1, 0), R = min(n - 1, i + w - 1);
                        for (int j = i + 1; j <= R; j++)
                            if (get(s, j))
                            {
                                R = j - 1;
                                break;
                            }
                        for (int j = L; j < i; j++)
                            if (get(s, j))
                            {
                                L = j + 1;
                            }
                        if (R - L + 1 < w) continue;
                        for (int j = L; j <= R; j++) tmp = OnBit(tmp, j);
                        ans = min(ans, Count(tmp, n));
                    }
            }
        ans += (m - 1)*n;
        printf("Case #%d: %d\n", itest + 1, ans);
    }
}
