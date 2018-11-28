#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <deque>
#include <stack>
#include <queue>
#include <algorithm>
#include <cmath>
using namespace std;

typedef unsigned long long ull;
typedef long double ld;

const int MAX_N = 1e8;
int N, J;
vector<ull> primes;
bool is_prime[MAX_N];

void init_primes() {
    fill(is_prime, is_prime + MAX_N, true);
    is_prime[0] = is_prime[1] = false;
    for (ull i = 2; i < MAX_N; i++) {
        if (is_prime[i]) {
            primes.push_back(i);
            for (ull j = i * i; j < MAX_N; j += i)
                is_prime[j] = false;
        }
    }
}

ull get_divisor(ull q) {
    if (q == 0 || q == 1) return 1;

    const ull sq = ceil(sqrt(ld(q)));
    for (ull p : primes) {
        if (q % p == 0) return p;
        if (p >= sq) break;
    }
    return 1;
}

bool is_jamcoin(ull n, ull d[]) {
    for (int i = 2; i <= 10; i++) {
        ull val = 0;
        for (int j = N - 1; j >= 0; j--) {
            int flag = (n & (1 << j));
            val = val * i + ((flag != 0) ? 1 : 0);
        }

        d[i] = get_divisor(val);
        if (d[i] == 1)
            return false;
    }
    return true;
}

int main() {
    init_primes();

    int TC; cin >> TC;
    for (int tc = 1; tc <= TC; tc++) {
        printf("Case #%d:\n", tc);
        scanf("%d %d", &N, &J);
        ull lb = (1 << (N - 1)) + 1;
        ull ub = (1 << N) - 1;

        for (ull i = lb; i <= ub; i+=2) {
            ull d[11] = {0};
            if (is_jamcoin(i, d)) {
                for (int j = N - 1; j >= 0; j--) {
                    int flag = (i & (1 << j));
                    printf("%d", ((flag != 0) ? 1 : 0));
                }
                for (int j = 2; j <= 10; j++) {
                    printf(" %llu", d[j]);
                }
                printf("\n");

                J--;
                if (J == 0)
                    break;
            }
        }
    }

    return 0;
}
