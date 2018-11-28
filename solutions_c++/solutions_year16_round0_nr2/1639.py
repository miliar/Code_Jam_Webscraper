#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

char s[105];

int main()
{
    //freopen("b.in", "r", stdin);
    //freopen("b_output.txt", "w", stdout);

    int cas = 0, t;
    scanf("%d", &t);
    while (t--) {
        scanf("%s", s);
        int ans = 0, n = strlen(s);
        for (int i = 0; i + 1 < n; ++i) if (s[i] != s[i + 1]) ++ans;
        if (s[n - 1] == '-') ++ans;
        printf("Case #%d: %d\n", ++cas, ans);
    }

    return 0;
}
