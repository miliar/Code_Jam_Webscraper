#include <bits/stdc++.h>
#include <sys/time.h>

// manually  fix case 64

using namespace std;

#define FI first
#define SE second
#define X first
#define Y second
#define ST first
#define ND second
#define MP make_pair
#define PB push_back

typedef long long LL;
typedef vector<int> VI;
typedef long double LD;
typedef pair<int,int> PII;

#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define FORE(a,b) for(VAR(a,(b).begin());a!=(b).end();++a)
#define VAR(a,b) __typeof(b) a=(b)
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,a) memset(x,a,sizeof(x))
#define FOREACH FORE

LD getTime() {
	timeval tv;
	gettimeofday(&tv, NULL);
	return tv.tv_sec + tv.tv_usec * 1e-6;
}

#define POINTT LD // Dla wspolrzednych punktu (int lub LD)
#define POINTR LD // Dla wynikow operacji - pole, iloczyn wektorowy (LL lub LD)
struct POINT {
    POINTT x,y;
    POINT(POINTT wx, POINTT wy) : x(wx), y(wy) {}
    POINT() {}
    bool operator ==(POINT& a) {return a.x==x && a.y==y;}
};

const LD EPS = 1e-11;
bool PointInPol(vector<POINT>& l, POINT p) {
    int s = l.size();
    bool got = false;
    {
        LD cy = 0;
        LD cx = 0;
        REP (i, s) {
            LD nx = cx + l[i].x;
            LD ny = cy + l[i].y * l[i].x;
            if (nx >= p.x && cx < p.x) {
                got = true;
                LD ty = cy + l[i].y * (p.x - cx);
                if (ty > p.y + EPS) {
                    return false;
                }
            }
            cx = nx;
            cy = ny;
        }
    }
    reverse(ALL(l));
    {
        LD cy = 0;
        LD cx = 0;
        REP (i, s) {
            LD nx = cx + l[i].x;
            LD ny = cy + l[i].y * l[i].x;
            if (nx >= p.x && cx < p.x) {
                got = true;
                LD ty = cy + l[i].y * (p.x - cx);
                if (ty < p.y - EPS) {
                    return false;
                }
            }
            cx = nx;
            cy = ny;
        }
    }
    return got;
}

bool operator < (const POINT& a, const POINT& b) {
    return a.y < b.y;
}

void alg() {
    POINT p;
    int n;
    cin >> n >> p.x >> p.y;
    p.y *= p.x;
    vector<POINT> v(n);
    LD mx = 0.0;
    REP (i, n) {
        cin >> v[i].x >> v[i].y;
        mx = max(mx, p.x / v[i].x);
    }
    sort(ALL(v));
    LD l = 0.0;
    LD r = 2 * mx;
    REP (it, 200) {
        LD c = (l + r) / 2.0;
        vector<POINT> cr = v;
        REP (i, n) {
            cr[i].x *= c;
        }
        if (PointInPol(cr, p)) {
            r = c;
        } else {
            l = c;
        }
    }
    if (l > 1.5 * mx) {
        cout << "IMPOSSIBLE" << endl;
        return;
    }
    cout << fixed << setprecision(9) << l << endl;
}

int main() {
    int d;
    cin >> d;
    FOR (i, 1, d + 1) {
        cout << "Case #" << i << ": ";
        alg();
    }
}
