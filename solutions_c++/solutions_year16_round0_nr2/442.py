// vim:set sw=4 et smarttab:
// Qualification Round 2016

#include <cstdio>
#include <cstring>

int solve(const char s[])
{
    int ret = 0;
    int n = strlen(s);
    for (int i = 1; i < n; ++i)
        if (s[i - 1] != s[i])
            ++ret;
    if (s[n - 1] != '+')
        ++ret;
    return ret;
}

int main()
{
    int ntc;
    scanf("%d", &ntc);
    for (int tc = 1; tc <= ntc; ++tc)
    {
        char s[101];
        scanf("%s", s);
        int answer = solve(s);
        printf("Case #%d: %d\n", tc, answer);
    }
}
