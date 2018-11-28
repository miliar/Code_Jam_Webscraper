#include <stdio.h>
#include <string.h>
#include <algorithm>

const int N = 110;

void do_flip(bool state[], int n)
{
    for (int i = 0; i < n / 2; i++) {
        state[i] = !state[i];
        state[n - 1 - i] = !state[n - 1 - i];
        std::swap(state[i], state[n - 1 - i]);
    }
    if (n % 2) state[n / 2] = !state[n / 2];
}

int flip(bool state[], int n)
{
    int ans = 0;
    while (1) {
        while (n > 0 && state[n - 1]) n--;
        if (n == 0) {
            break;
        }
        int i;
        for (i = 0; i < n; i++) {
            if (!state[i]) break;
        }
        if (i > 0) {
            do_flip(state, i);
            ans++;
        }
        do_flip(state, n);
        ans++;
    }
    return ans;
}

int main()
{
    int t;
    scanf("%d", &t);

    char s[N];
    bool state[N];

    for (int cases = 1; cases <= t; cases++) {
        scanf("%s", s);
        int n = strlen(s);
        for (int i = 0; i < n; i++) {
            if (s[i] == '+') state[i] = true;
            else state[i] = false;
        }
        printf("Case #%d: %d\n", cases, flip(state, n));
    }

    return 0;
}
