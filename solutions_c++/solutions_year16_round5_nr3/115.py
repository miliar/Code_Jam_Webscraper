#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
template <class T> int size(const T &x) { return x.size(); }
const int INF = 2147483647;
#define rep(i,a,b) for (__typeof(a) i=(a); i<(b); ++i)
#define iter(it,c) for (__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)

struct point  {
    double x, y, z;
    point(double _x=0, double _y=0, double _z=0) {
        x = _x;
        y = _y;
        z = _z;
    }
    double dist(point other) {
        return sqrt(
                pow(x - other.x, 2.0) + 
                pow(y - other.y, 2.0) + 
                pow(z - other.z, 2.0)
                );
    }
    point operator +(const point &other) const {
        return point(x + other.x,
                     y + other.y,
                    z + other.z);
    }
    point operator *(const double &d) const {
        return point(x * d, y * d, z * d);
    }
};

double dist[1010];
bool done[1010];

struct cmp {
    bool operator()(const int &a, const int &b) {
        double x = dist[a],
                 y = dist[b];
        if (std::isinf(x)) {
            return false;
        }
        if (std::isinf(y)) {
            return true;
        }
        if (abs(x-y) < 1e-9){
            return a < b;
        }
        return x < y;
    }
};

double get_dist(point a, point av, point b, point bv, double t1) {
    point A1 = a + av * t1,
            B1 = b + bv * t1;
    return A1.dist(B1);
}

double get_best(point a, point av, point b, point bv) {
    double lo = 0,
           hi = 1e9;
    rep(it,0,100) {
        double t1 = lo+(hi-lo) / 3.0,
               t2 = lo+(hi-lo)*2.0 / 3.0;
        if (get_dist(a,av,b,bv,t1) < get_dist(a,av,b,bv,t2)) {
            hi = t2;
        } else {
            lo = t1;
        }
    }
    return hi;
}

struct union_find {
    vi p; union_find(int n) : p(n, -1) { }
    int find(int x) { return p[x] < 0 ? x : p[x] = find(p[x]); }
    bool unite(int x, int y) {
        int xp = find(x), yp = find(y);
        if (xp == yp) return false;
        if (p[xp] > p[yp]) swap(xp,yp);
        p[xp] += p[yp], p[yp] = xp;
        return true; }
    int size(int x) { return -p[find(x)]; } };

int main() {
    int ts;
    scanf("%d", &ts);
    rep(tZ,0,ts) {
        int n, s;
        scanf("%d %d", &n, &s);
        vector<point> pt(n), vel(n);
        rep(i,0,n) {
            scanf("%lf %lf %lf", &pt[i].x, &pt[i].y, &pt[i].z);
            scanf("%lf %lf %lf", &vel[i].x, &vel[i].y, &vel[i].z);
        }
        double lo = 0.0,
               hi = 1e9;
        double res = -1.0;
        rep(it,0,200) {
            double d = (lo+hi)/2.0;
            union_find uf(n);
            rep(cur,0,n) {
                rep(nxt,0,n) {
                    if (get_dist(pt[cur], vel[cur], pt[nxt], vel[nxt], 0.0) <= d) {
                        uf.unite(cur,nxt);
                    }
                }
            }
            if (uf.find(0) == uf.find(1)) {
                hi = d;
                res = d;
            }  else {
                lo = d;
            }
        }
        printf("Case #%d: %0.10lf\n", tZ +1, res);
    }
    return 0;
}

