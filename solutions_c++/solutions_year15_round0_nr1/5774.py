#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

int T, t, N;
char shy[1024];

int solve() {
    int extra = 0;
    int clap = shy[0] - '0';

    for (int i = 1; i <= N; i++) {
        int s = shy[i] - '0';
        int add = max(0, i - clap);
        extra += add;
        clap += add + s;
    }

    return extra;
}

int main() {
    scanf("%d", &T);

    for (int t = 1; t <= T; t++) {
        scanf("%d%s", &N, shy);
        printf("Case #%d: %d\n", t, solve());
    }

    return 0;
}
