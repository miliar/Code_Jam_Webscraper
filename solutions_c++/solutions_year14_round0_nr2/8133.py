#include <map>
#include <set>
#include <queue>
#include <time.h>
#include <string>
#include <math.h>
#include <vector>
#include <cstring>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>
const int inf = 1000000000,
          mod = 1000000007;
#define Wi(a) printf("%d ", (a))
#define Wi2(a, b) printf("%d %d ", (a), (b))
#define Wie(a) printf("%d\n", (a))
#define Wie2(a, b) printf("%d %d\n", (a), (b))
#define Ri(a) scanf("%d", &(a))
#define Ri2(a, b) scanf("%d%d", &(a), &(b))
#define F first
#define S second
#define pii pair < int, int >
#define v(tp) vector< tp >
#define ll long long
#define pb push_back
#define mp make_pair
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for(int (i) = (a), _n_ = (b); (i) <= _n_; (i)++)
#define FORD(i,a,b) for(int (i) = (a), _n_ = (b); (i) >= _n_; (i)--)
#define forn(i,b) FOR((i),0,(b) - 1)
using namespace std;

bool check( double time, double C, double F, double X ) {
    double speed = 2;
    while(1) {
        if( speed * time >= X ) return 1;
        if( C / speed >= time ) return 0;
        time -= C / speed;
        speed += F;
    }
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    Ri( t );
    FOR(n_,1,t) {
        double b = 0, g = 50010, C, F, X;
        scanf("%lf%lf%lf", &C, &F, &X);
        forn(it,40) {
            double m = (b + g) / 2;
            if( check( m, C, F, X ) ) g = m; else b = m;
        }
        printf("Case #%d: %.7lf\n", n_, g);
    }
    return 0;
}
