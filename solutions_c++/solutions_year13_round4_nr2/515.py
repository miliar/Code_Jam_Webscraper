#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;

bool isOk1(int N, long long P, long long n) {
    long long rank = 0;
    //printf("isOk1: N:%d, P:%lld, n:%lld\n", N, P, n);
    for (int r = 1; r <= N; ++r) {
        //printf("- isOk1: r:%d, rank:%lld, n:%lld\n", r, rank, n);
        rank <<= 1;
        if (n > 0) {
            rank += 1;
            n = (n - 1) / 2;
        }
    }
    //printf("- isOk1: rank:%lld, n:%lld\n", rank, n);
    return rank < P;
}

bool isOk2(int N, long long P, long long n) {
    //printf("isOk2: N:%d, P:%lld, n:%lld\n", N, P, n);
    long long rank = 0;
    long long total = 1;
    total <<= N;
    n = total - n - 1;
    for (int r = 1; r <= N; ++r) {
        //printf("- isOk2: r:%d, rank:%lld, n:%lld\n", r, rank, n);
        rank <<= 1;
        if (n > 0) {
           n = (n - 1) /2;
        } else {
            rank += 1;
        }
    }
    //printf("- isOk2: rank:%lld, n:%lld\n", rank, n);
    return rank < P;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        int N;
        long long P;
        scanf("%d%lld", &N, &P);

        long long L = 0;
        long long H = ((long long)1 << N) - 1;
        long long res1 = H;
        //printf("%lld %lld\n", L, H);
        while (L <= H) {
            long long T = (L + H) / 2;
            if (isOk1(N, P, T)) {
                res1 = T;
                L = T + 1;
            } else {
                H = T - 1;
            }
        }
        L = 0;
        H = ((long long)1 << N) - 1;
        long long res2 = H;
        while (L <= H) {
            long long T = (L + H) / 2;
            if (isOk2(N, P, T)) {
                res2 = T;
                L = T + 1;
            } else {
                H = T - 1;
            }
        }
        printf("Case #%d: %lld %lld\n", t, res1, res2);
    }
    return 0;
}
