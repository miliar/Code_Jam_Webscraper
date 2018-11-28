#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

long long pow(long long a, long long e) {
    long long ret = 1;
    for (; e; e >>= 1, a *= a)
        if (e & 1)
            ret *= a;
    return ret;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        int K, C, S;
        scanf("%d %d %d", &K, &C, &S);
        printf("Case #%d:", t);
        long long block = pow(K, C-1);
        for (int i = 0; i < K; i++)
            printf(" %lld", block * i + 1);
        puts("");
    }
}
