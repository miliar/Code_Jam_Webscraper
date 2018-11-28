#include <cstdio>

int main()
{
    int t;
    scanf("%d\n", &t);

    for (int i = 1; i <= t; i++) {
        char c, cur = '\0';
        int ans = -1;

        while ((c = getchar()) != '\n') {
            if (c != cur) {
                cur = c;
                ans++;
            }
        }

        if (cur == '-') ans++;
        printf("Case #%d: %d\n", i, ans);
    }

    return 0;
}
