#include <cstdio>
#include <algorithm>

int solve(int N) {
    bool seen[10];
    int cnt_seen = 0, n = 0;
    std::fill(seen, seen+10, 0);
    while (1) {
        n += N;
        for (int tmp = n; tmp; tmp /= 10) {
            if (!seen[tmp%10]) {
                ++cnt_seen;
                seen[tmp%10] = true;
                if (cnt_seen == 10)
                    return n;
            }
        }
    }
}

int main() {
    int T, N;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        scanf("%d", &N);
        if (N == 0)
            printf("Case #%d: INSOMNIA\n", t);
        else
            printf("Case #%d: %d\n", t, solve(N));
    }
    return 0;
}
