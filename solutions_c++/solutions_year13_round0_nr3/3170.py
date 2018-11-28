#include <cstdio>
#include <cstring>
#include <cmath>

int T, TT;

bool IsPalindrome(long long i)
{
    char t[30];
    sprintf(t, "%lld", i);
    int len = strlen(t);
    for (i = 0; i < len; i++)
        if (t[i] != t[len-1-i])
            return 0;
    return 1;
}

int main()
{
    scanf("%d", &TT);
    for (T = 1; T <= TT; T++) {
        long long i, start, end;
        scanf("%lld %lld", &start, &end);
        int ans = 0;
        for (i = sqrt(start); i*i <= end; i++) {
            if (i*i < start)
                continue;
            if (IsPalindrome(i) && IsPalindrome(i*i))
                ans++;
        }
        printf("Case #%d: %d\n", T, ans);
    }
}