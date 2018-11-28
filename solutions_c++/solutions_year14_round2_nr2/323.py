#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>
#include <map>

using namespace std;

typedef long long ll;
typedef long double ldb;

#define forab(i, a, b) for(int i = int(a); i < int(b); ++i)
#define forba(i, b, a) for(int i = int(b) - 1; i >= int(a); --i)
#define forn(i, n) forab(i, 0, n)

struct thing {
    int a, b, k, z;

    thing(): a(), b(), k(), z() {}
    thing(int a, int b, int k, int z): a(a), b(b), k(k), z(z) {}

    bool operator <(const thing & t) const {
        if (a != t.a)
            return a < t.a;
        if (b != t.b)
            return b < t.b;
        if (k != t.k)
            return k < t.k;
        return z < t.z;
    }
};

map<thing, ll> q;

ll cnt(int a, int b, int k, int z) {
    if (z == -1)
        return 1ll;
    if (q.count(thing(a, b, k, z)))
        return q[thing(a, b, k, z)];

    ll res = 0;
    if ((a & (1 << z)) && (b & (1 << z)) && (k & (1 << z))) {
        res += cnt((a ^ (1 << z)), (b ^ (1 << z)), (k ^ (1 << z)), z - 1);
    }
    int newA = a, newB = b, newK = k;
    if (a & (1 << z)) 
        newA = (1 << z) - 1;
    if (b & (1 << z)) 
        newB = (1 << z) - 1;
    if (k & (1 << z))
        newK = (1 << z) - 1;

    res += cnt(newA, newB, newK, z - 1);

    if (a & (1 << z))
        res += cnt((a ^ (1 << z)), newB, newK, z - 1);
    if (b & (1 << z))
        res += cnt(newA, (b ^ (1 << z)), newK, z - 1);

    q[thing(a, b, k, z)] = res;
    return res;
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    scanf("%d ", &T);
    forn(test, T) {
        printf("Case #%d: ", test + 1);

        int a, b, k;
        cin >> a >> b >> k;
        a--, b--, k--;
        cout << cnt(a, b, k, 30) << '\n';
    }
    return 0;
}
