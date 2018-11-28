#include <iostream>
#include <cstdio>
#include <cassert>
#include <cstring>
#include <vector>
#include <valarray>
#include <array>
#include <queue>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <algorithm>
#include <cmath>
#include <complex>
#include <random>
#include <bitset>
#include <gmpxx.h>

using namespace std;
typedef long long ll;
typedef unsigned long long ull;

//typedef long double R;
typedef mpf_class R;
typedef complex<R> P;

R EPS;

/*
 -1 -> neg
  0 -> near 0
  1 -> pos
  */
int sgn(R a) {
    if (a < -EPS) return -1;
    if (a > EPS) return 1;
    return 0;
}

int sgn(R a, R b) {
    return sgn(b-a);
}

bool near(P a, P b) {
    return !sgn(abs(a-b));
}

bool lessP(const P &l, const P &r) {
    if (sgn(l.real(), r.real())) return l.real() < r.real();
    if (sgn(l.imag(), r.imag())) return l.imag() < r.imag();
    return false;
}

R cross(P a, P b) { return a.real()*b.imag() - a.imag()*b.real(); }
R dot(P a, P b) { return a.real()*b.real() + a.imag()*b.imag(); }

/* 1->cclock
  -1->clock
   0->on
   2->back
  -2->front
  */
int ccw(P a, P b, P c) {
    assert(!near(a, b));
    if (near(a, c) || near(b, c)) return 0;
    int s = sgn(cross(b-a, c-a));
    if (s) return s;
    if (dot(b-a, c-a) < 0) return 2;
    if (dot(a-b, c-b) < 0) return -2;
    return 0;
}


struct L {
    P x, y;
    L() {};
    L(P x, P y) :x(x), y(y) {};
};

P vec(const L &l) {
    return l.y - l.x;
}

R abs(const L &l) {
    return abs(vec(l));
}


struct T {
    P d[3];
    T() {}
    T(P x, P y, P z) {
        d[0] = x; d[1] = y; d[2] = z;
    }
};

typedef vector<P> Pol;

P cu(const Pol &p, int i) { 
    int s = p.size();
    return p[(i%s+s)%s];
};

//0:P is out 1:P is on line 2:P is in
int contains(const Pol &pol, P p) {
    int in = -1;
    for (int i = 0; i < (int)pol.size(); i++) {
        P a=cu(pol,i)-p, b=cu(pol,i+1)-p;
        if (ccw(a, b, P(0, 0)) == 0) return 1;
        if (imag(a) > imag(b)) swap(a, b);
        if (imag(a) <= 0 && 0 < imag(b)) {
            if (cross(a, b) < 0) in *= -1;
        }
    }
    return in+1;
}



Pol convex(Pol p) {
    sort(p.begin(), p.end(), lessP);
    if (p.size() <= 2) return p;
    Pol up;
    for (P d: p) {
        while (up.size() > 1 && ccw(up[up.size()-2], up[up.size()-1], d) == 1) up.pop_back();
        up.push_back(d);
    }
    reverse(up.begin(), up.end());
    Pol down;
    for (P d: p) {
        while (down.size() > 1 && ccw(down[down.size()-2], down[down.size()-1], d) == -1) down.pop_back();
        down.push_back(d);
    }
    down.insert(down.begin(), up.begin()+1, up.end()-1);
    return down;
}







const int MN = 110;
int n;
R X, Y;
R x[MN], y[MN];

bool calc(R md) {
    Pol v = {P(0, 0)};
    for (int i = 0; i < n; i++) {
        P r = P(x[i], y[i]);
        r *= md;
        Pol v2 = v;
        for (P p: v) {
            v2.push_back(p+r);
        }
        v = convex(v2);
    }
//    cerr << "resprint X:" << X.get_d() << " Y:" << Y.get_d() << endl;
//    for (P p: v) {
//        cerr << p.real().get_d() << " " << p.imag().get_d() << endl;
//    }
    return contains(v, P(X, Y));
}



void solve(int T) {
    cerr << "Start:" << T << endl;
    string XX, YY;
    cin >> n >> XX >> YY;
    X = XX; Y = YY;
    Y *= X;
    for (int i = 0; i < n; i++) {
        string xx, yy;
        cin >> xx >> yy;
        x[i] = xx; y[i] = yy;
        y[i] *= x[i];
    }

    R l = 0, r = 1e10;
    for (int i = 0; i < 100; i++) {
        R md = (l+r)/2;
//        if (abs(md) < 1e-7) continue;
//        cerr << md.get_d() << endl;
//        printf("%Lf %Lf %Lf %d\n", l, r, md, calc(md));
        if (calc(md)) {
            r = md;
        } else {
            l = md;
        }
    }
    printf("Case #%d: ", T);
    if (r > 1e10/2) {
        printf("IMPOSSIBLE\n");
    } else {
        printf("%.20lf\n", l.get_d());
    }
}

int main() {
    cerr << EPS.get_d() << endl;
    cerr << mpf_get_default_prec() << endl;
    mpf_set_default_prec(500);
    X = R(); Y = R();
    for (int i = 0; i < MN; i++) {
        x[i] = R(); y[i] = R();
    }
    EPS = R("0.000000000000000000000000000000000001", 500);
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        solve(i);
    }
    return 0;
}
