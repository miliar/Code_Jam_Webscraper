//#pragma comment(linker, "/STACK:16777216")

#include <iostream>
#include <cstdio>
#include <cmath>
#include <set>
#include <vector>
#include <map>
#include <cstring>
#include <sstream>
#include <algorithm>
#include <string>
#include <queue>
#include <fstream>

#define FOR(i,a,b) for(int i = (a); i <= (b); i++)
#define FR(i,a) for(int i = 0; i < (a); i++)
#define DR(i,a) for(int i = (a)-1; i >=0; i--)
#define DOWN(i,a,b) for(int i = (a); i >= (b); i--)
#define FORD(i,a,b) for(int i = (a), _b = (b); i >= _b; i--)
#define REPD(i,n) for(int i = (n) - 1; i >= 0; i--)
#define PB push_back
#define MP make_pair

#define F first
#define S second
#define RESET(c,x) memset(c,x,sizeof(c))
#define SIZE(c) (c).size()
#define ALL(c) (c).begin(), (c).end()

#define REP(i,a) for(int i = 0; i < (a); i++)

#define sqr(x) ((x)*(x))
#define oo 1000000009
using namespace std;
/*************************TEMPLATE**********************************/
long long convertToNum(string s)
{
    long long val = 0; FR(i,s.size()) val = val * 10 + s[i] - '0';
    return val;
}
char bu[50];
string convertToString(int a) {
    sprintf(bu,"%d",a);
    return string(bu);
}
long long GCD(long long x,long long y)  {
    if (!x) return y; if (!y) return x;
    if (x == y) return x; if (x < y) return GCD(x,y%x); else return GCD(x%y,y);
}
long long POW(long long x,long long y,long long Base){
    if (!y) return 1; long long u = POW(x,y/2,Base);
    u = (u * u) % Base;
    if (y % 2) return (u * x) % Base; else return u;
}
void extended_euclid(long long A, long long B, long long &x,long long &y) {
    if (A == 1 && B == 0) {
        x = 1;
        y = 0;
        return;
    }
    if (A < B) extended_euclid(B,A,y,x);
    else {
        long long xx,yy;
        extended_euclid(A%B,B,xx,yy);
        x = xx;
        y = yy - (A/B)*xx;

    }
}
//newstate = (newstate-1) & oldstate
/*******************************CODE HERE***********************************/
const double eps = 1e-10;
int cmp(double q,double w) {
    return (q < w + eps) ? (q > w - eps) ? 0 : -1 : 1;
}
struct point {
    double x,y;
    point (double x,double y): x(x),y(y) {}
    point () {x=y=0.0; }
    point operator +(point q) { return point(x+q.x,y+q.y); }
    point operator -(point q) { return point(x-q.x,y-q.y); }
    point operator *(double t) { return point(x*t,y*t); }
    point operator /(double t) { return point(x/t,y/t); }
    double operator *(point q){ return q.x * x + q.y * y; }
    double operator %(point q){ return x*q.y - y*q.x; }
    int cmp(point q) const { if(int t = ::cmp(x,q.x)) return t; return ::cmp(y,q.y); }
    #define Comp(x) bool operator x (point q) const { return cmp(q) x 0; }
    Comp(>) Comp(<) Comp(==) Comp(>=) Comp(<=) Comp(!=)
    #undef Comp
};
typedef vector<point> polygon;
inline int ccw(point a, point b, point c) {
    return cmp((b-a)%(c-a),0);
}
double area(polygon &p) {
    double s = 0.0;
    FOR(i,1,(int)p.size()-1) s+= (p[i]-p[0])%(p[(i+1)%p.size()]-p[0]);
    return fabs(s) / 2.0;
}
struct comp_hull {
    point pivot;
    bool operator() (point q,point w) {
        point Q = q - pivot, W = w - pivot;
        double R = Q % W;
        if (cmp(R,0)) return R < 0;
        return cmp(Q*Q,W*W) < 0;
    }
};
polygon convex_hull(polygon p) { // minimum vertices
    int j = 0, k, n = p.size();
    polygon r(n);
    if (!n) return r;
    comp_hull comp;
    comp.pivot = *min_element(p.begin(),p.end());
    sort(p.begin(),p.end(),comp);
    FR(i,n) {
        while (j > 1 && ccw(r[j-1],r[j-2],p[i]) <= 0) j--;
        r[j++] = p[i];
    }
    r.resize(j);
    return r;
}

#define maxn 20
polygon A;
int n;
point p[maxn];
long double Area;

int id[maxn];

void get(point D1, point D2, long long &a1, long long &b1, long long &c1) {
    a1 = D1.y - D2.y;
    b1 = D2.x - D1.x;
    c1 = -D1.x*a1-D1.y*b1;
}

long double f(point X, long double a, long double b, long double c) {
    return a * X.x + b * X.y + c;
}
bool giua(point a, point b, point c) {
    return min(b.x,c.x) <= a.x && a.x <= max(b.x,c.x) &&
            min(b.y,c.y) <= a.y && a.y <= max(b.y,c.y);
}
bool correct() {
    long long a1,b1,c1,a2,b2,c2;
    FOR(i,0,n-1)
    FOR(j,i+2,n-1) if (i != 0 || j != n-1) {
        get(p[id[i]],p[id[(i+1)%n]],a1,b1,c1);
        get(p[id[j]],p[id[(j+1)%n]],a2,b2,c2);
        long double val1 = f(p[id[i]],a2,b2,c2) * f(p[id[(i+1)%n]],a2,b2,c2);
        long double val2 = f(p[id[j]],a1,b1,c1) * f(p[id[(j+1)%n]],a1,b1,c1);
        if (val1 < 0 && val2 < 0) return false;
        if (val1 == 0) {
            if (f(p[id[i]],a2,b2,c2) == 0 && giua(p[id[i]],p[id[j]],p[id[(j+1)%n]])) return false;
            if (f(p[id[(i+1)%n]],a2,b2,c2) == 0 && giua(p[id[(i+1)%n]],p[id[j]],p[id[(j+1)%n]])) return false;
        }
        if (val2 == 0) {
            if (f(p[id[j]],a1,b1,c1)  == 0 && giua(p[id[j]],p[id[i]],p[id[(i+1)%n]])) return false;
            if ( f(p[id[(j+1)%n]],a1,b1,c1) == 0 && giua(p[id[(j+1)%n]],p[id[i]],p[id[(i+1)%n]])) return false;
        }

    }
    polygon B(0);
    FR(i,n) B.push_back(p[id[i]]);
    B.push_back(p[id[0]]);
    long double cur_area = 0;
    FR(i,n) cur_area += (B[i].x-B[i+1].x)*(B[i].y+B[i+1].y);
    cur_area = abs(cur_area);
    cur_area /= 2;
    //return true;
    if (cur_area*2>Area) {
            return true;
    }
    else return false;

}
void solve() {
    A = convex_hull(A);

    A.push_back(A[0]);
    Area = 0;
    FR(i,A.size()-1) Area += (A[i].x-A[i+1].x)*(A[i].y+A[i+1].y);
    Area = abs(Area);
    Area /= 2;

    FR(i,n) id[i] = i;
    do {
        if (correct()) {
            FR(i,n) cout << id[i] << " ";
            cout << endl;
            return;
        }
    } while (next_permutation(id,id+n));
}
int main() {
    freopen("test6.in","r",stdin);
    freopen("test.out","w",stdout);
    int ntest;
    cin >> ntest;
    FOR(test,1,ntest) {
        cout << "Case #" << test << ": ";
        cin >> n;
        A.clear();
        FR(i,n) {
            cin >> p[i].x >> p[i].y;
            A.push_back(p[i]);
        }
        solve();
    }
    return 0;
}
