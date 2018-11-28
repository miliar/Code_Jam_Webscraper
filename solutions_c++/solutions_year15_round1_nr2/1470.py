#include <cstdio>
#include <cstring>
#include <set>

#define _N 1010

using namespace std;

struct Barber {
    int id, cost;
    long long st;
    Barber() { }
    Barber(int id, int cost, long long st) : id(id), cost(cost), st(st) { }
    bool operator < (const Barber &b) const {
        if (st == b.st) return id < b.id;
        return st < b.st;
    }
};

long long gcd(long long a, long long b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

long long lcm(long long a, long long b) {
    long long g = gcd(a, b);
    return a / g * b;
}

int main() {
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("B-small-attempt1.out", "w", stdout);

    int t, n, b[_N], m;
    scanf("%d", &t);
    for (int cas = 1; cas <= t; ++cas) {
        scanf("%d%d", &n, &m);
        set<Barber> rest;
        long long rep = 1;
        for (int i = 0; i < n; ++i) {
            scanf("%d", &b[i]);
            rep = lcm(rep, b[i]);
            rest.insert(Barber(i + 1, b[i], 0));
        }

        long long rnd = 0;
        for (int i = 0; i < n; ++i) {
            rnd += rep / b[i];
        }
        // printf("rnd = %d\n", rnd);
        m = (m - 1) % rnd;

        for (int i = 0; i < m; ++i) {
            Barber cur = *rest.begin();
            // printf("#%d -> %d\n", i, cur.id);
            rest.erase(rest.begin());
            rest.insert(Barber(cur.id, cur.cost, cur.st + cur.cost));
        }
        printf("Case #%d: %d\n", cas, (*rest.begin()).id);
    }

    return 0;
}
