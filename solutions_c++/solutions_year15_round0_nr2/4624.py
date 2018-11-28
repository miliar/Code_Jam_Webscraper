#include <cstdio>
#include <queue>

using namespace std;

const int DMAX = 1000;
const int PMAX = 1000;

int d, p[DMAX + 1];

bool verif (int tmax) {
    for (int a = 0; a <= tmax; ++a) {
        int aux = a, t = tmax - a;
        priority_queue <int, vector <int> > hp;
        for (int i = 1; i <= d; ++i)
            hp.push (p[i]);

        while (aux--) {
            int c = hp.top ();
            hp.pop ();

            if (c > t)
                hp.push (c - t);
        }

        if (hp.top () <= t) return true;
    }

    return false;
}

int solve () {
    scanf ("%d", &d);
    for (int i = 1; i <= d; ++i)
        scanf ("%d", &p[i]);

    int ans = -1, st = 0, dr = PMAX, med;

    while (st <=dr) {
        med = (st + dr) >> 1;

        if (verif (med))
            ans = med, dr = med - 1;
        else
            st = med + 1;
    }

    return ans;
}

int main () {
    //freopen ("data.in", "r", stdin);
    //freopen ("data.out", "w", stdout);
    int tests;

    scanf ("%d", &tests);
    for (int test = 1; test <= tests; ++test) {
        int ans = solve ();
        printf ("Case #%d: %d\n", test, ans);
    }

    return 0;
}
