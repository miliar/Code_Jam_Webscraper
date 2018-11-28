#include <cstdio>
#include <cstring>

char s[1010];
void run(int cas) {
    int k;
    scanf(" %s%d", s, &k);
    int l = strlen(s), ans = 0;
    for (int i = 0; i <= l - k; i++)
        if (s[i] == '-') {
            ans += 1;
            for (int j = i; j < i + k; j++)
                s[j] = (s[j] == '+' ? '-' : '+');
        }
    bool ok = true;
    for (int i = l - k + 1; i < l; i++)
        if (s[i] == '-')
            ok = false;
    if (ok)
        printf("Case #%d: %d\n", cas, ans);
    else
        printf("Case #%d: IMPOSSIBLE\n", cas);
}

int main() {
    int tt;
    scanf("%d", &tt);
    for (int cas = 1; cas <= tt; cas++)
        run(cas);
    return 0;
}
