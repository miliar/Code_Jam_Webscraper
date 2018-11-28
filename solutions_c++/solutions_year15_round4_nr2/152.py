#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <string>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <queue>
#include <assert.h>

using namespace std;

#define ll long long
#define ull unsigned long long
#define ld long double
#define mp make_pair
#define pb push_back
#define fst first
#define snd second

template<typename T>
T abs(T x) {
    return x > 0 ? x : -x;
}

template<typename T>
T sqr(T x) {
    return x * x;
}



const int maxn = 105;

pair<ld, ld> a[maxn];
ld vNeed, tNeed;
int n;

ld eps = 1e-9;

ld f(ld x) {
    ld need = tNeed * vNeed;

    ld v = 0;

    for (int i = 0; i < n; i++) {
        ld m = x * a[i].snd * a[i].fst;

        if (m < need) {
            v += x * a[i].snd;
            need -= m;
        } else {
            v += need / a[i].fst;
            need = 0;
            break;
        }
    }

    if (abs(need) > eps) {
        return 1e18;
    } else {
        return v;
    }
}

bool check(ld x) {
    ld ma = f(x);
    reverse(a, a + n);
    ld mi = f(x);
    reverse(a, a + n);


    if (mi > 1e17 || ma > 1e17) {
        return false;
    }



    return mi < vNeed + eps && vNeed < ma + eps;
}


ld solve(ld _eps) {
    eps = _eps;
    ld lo = 0.0, hi = 1e18;
    for (int iter = 0; iter < 500; iter++) {
        ld mid = (lo + hi) / 2.0;

        if (check(mid)) {
            hi = mid;
        } else {
            lo = mid;
        }
    }
    return hi;
}


int main() {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);

    int t;
    scanf("%d\n", &t);
    int tt = 0;
    ld mm = 0;
    while (t--) {
        tt++;

        cin >> n >> vNeed >> tNeed;

        for (int i = 0; i < n; i++) {
            ld r, c;
            cin >> r >> c;
            a[i] = mp(c, r);
        }

        sort(a, a + n);

        ld hi2 = solve(1e-14);
        ld hi = solve(1e-13);

       // cerr << hi << " " << hi2 << endl;
        //assert((hi > 1e17) == (hi2 > 1e17));
       // cerr << abs(hi2 - hi) / hi << " "  << hi << " " << hi2  << endl;
        mm = max(mm, abs(hi2 - hi) / hi);

        printf("Case #%d: ", tt);

        if (hi > 1e17) {
            printf("IMPOSSIBLE\n");
        } else {
            cout.precision(12);
            cout << fixed << hi << endl;
        }
    }

    cerr << mm << endl;

    return 0;
}