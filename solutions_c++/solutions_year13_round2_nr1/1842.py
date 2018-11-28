#include <cstdio>
#include <algorithm>
using namespace std;

const int MAXN = 100 + 5;
long long num[MAXN];
long long A;
int N;

void input() {
    scanf("%lld%d", &A, &N);
    for (int i=0; i<N; ++i) {
        scanf("%lld", &num[i]);
    }
}

void progress(int &pos, long long &A) {
    while (pos < N && num[pos] < A) {
        A += num[pos];
        ++ pos;
    }
}

void solve() {
    sort(num, num + N);

    int pos = 0;
    progress(pos, A);

    int best = N - pos;

    for (int i=1; i<best; ++i) {
        int tp = pos;
        long long ta = A;

        int j;
        for (j=0; j<i && tp<N; ++j) {
            ta += ta - 1;
            progress(tp, ta);
        }
        int cost = j + N - tp;

        if (cost < best) {
            best = cost;
        }
    }

    printf("%d\n", best);
}

int main() {
    int t;
    scanf("%d", &t);
    for (int i=0; i<t; ++i) {
        printf("Case #%d: ", i+1);
        input();
        solve();
    }
}
