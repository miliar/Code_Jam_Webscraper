#include <bits/stdc++.h>

#define mp make_pair

typedef std::pair<int, int> pii;

void get_ans(std::string s)
{
    int k;
    scanf("%d", &k);
    int len = s.length();
    int a[len];
    for (int i = 0; i < len; ++i)
        if (s[i] == '+')
            a[i] = 1;
        else
            a[i] = 0;
    int ans = 0;
    for (int i = 0; i <= len - k; ++i)
    {
        if (!a[i])
        {
            for (int j = i; j < i + k; ++j)
                a[j] = !a[j];
            ++ans;
        }
    }
    int is_good = 1;
    for (int i = len - k + 1; i < len; ++i)
        is_good = is_good && a[i];
    if (is_good)
        printf("%d\n", ans);
    else
        printf("IMPOSSIBLE\n");
}

int main()
{
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
    int n;
    scanf("%d", &n);
    n = 0;
    std::string s;
    while (std::cin >> s)
    {
        printf("Case #%d: ", ++n);
        get_ans(s);
    }
    return 0;
}