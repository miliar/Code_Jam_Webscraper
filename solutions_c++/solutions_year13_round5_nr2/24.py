#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>

using namespace std;

typedef long long LL;
typedef pair<int, int> PII;
#define MP make_pair
#define FOR(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define REP(i,n) for(int i=0;i<(n);++i)
#define VAR(v,i) __typeof(i) v=(i)
#define FORE(i,c) for(__typeof(c.begin()) i=(c.begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second
#define SZ(x) (int)(x).size()
#define ALL(c) c.begin(),c.end()
#define ZERO(x) memset(x,0,sizeof(x))
const double EPS = 1e-9;
inline bool IsZero(double x){ return x>=-EPS && x<=EPS; }
#define POINTT int // Dla wspolrzednych punktu (int lub double)
#define POINTR LL // Dla wynikow operacji - pole, iloczyn wektorowy (LL lub double)
struct POINT {
    POINTT x,y;
    POINT(POINTT wx, POINTT wy) : x(wx), y(wy) {}
    POINT() {}
    bool operator ==(POINT& a) {return a.x==x && a.y==y;}
};
typedef POINT Point;
#define Det(p1,p2,w) (POINTR(p2.x-p1.x)*POINTR(w.y-p1.y)-POINTR(p2.y-p1.y)*POINTR(w.x-p1.x))
int sgn(double x){ return IsZero(x)?0:(x < 0 ? -1 : 1); }
#define PointInRect(p1,p2,p3) (min(p1.x,p2.x) <= p3.x && min(p1.y,p2.y) <= p3.y && max(p1.x,p2.x) >= p3.x && max(p1.y,p2.y) >= p3.y)
#define PointInSegment(p1,p2,l) (Det(p1,p2,l)==0 && PointInRect(p1,p2,l))
inline bool SegmentCross(POINT& p1, POINT& p2, POINT& l1, POINT& l2) {
    return sgn(Det(p1,p2,l1))*sgn(Det(p1,p2,l2)) == -1 && sgn(Det(l1,l2,p1))*sgn(Det(l1,l2,p2)) == -1;
}
inline bool SegmentTouch(POINT& p1, POINT &p2, POINT &l1, POINT &l2) {
    return SegmentCross(p1,p2,l1,l2) || PointInSegment(p1,p2,l1) || PointInSegment(p1,p2,l2) || PointInSegment(l1,l2,p1) || PointInSegment(l1,l2,p2);
}
/* Zwraca w zaleznosci od tego czy sie touch false lub true.  Przeciecie umieszcza w r, jeden punkt to [puntk, 2 punkty to odpicinek. */
bool SCPcmp(POINT a, POINT b){ return IsZero(a.x-b.x)? a.y < b.y : a.x < b.x; }
inline bool SegmentCrossPoint(POINT p1, POINT p2, POINT l1, POINT l2, vector<POINT> &r) {
  r.clear();
  int w1=sgn(Det(p1,p2,l1)),w2=sgn(Det(p1,p2,l2)),v1=sgn(Det(l1,l2,p1)),v2=sgn(Det(l1,l2,p2));
  if (w1 * w2 > 0 || v1*v2 > 0) return false;  // Nie przecinaja sie
  if (!w1 && !w2){ // Sa wspolliniowe
    POINT p;
    if (SCPcmp(p2,p1)) { p=p1; p1=p2; p2=p; }
    if (SCPcmp(l2,l1)) { p=l1, l1=l2, l2=p; }
    if (SCPcmp(p2,l1) || SCPcmp(l2,p1)) return false;
    if (p2==l1){ r.PB(POINT(p2.x,p2.y));  }
    else if (p1==l2){ r.PB(POINT(l2.x,l2.y)); }
    else{
      r.PB(SCPcmp(p1,l1)?l1:p1);
      r.PB(SCPcmp(p2,l2)?p2:l2);
    }
  }
  else if (l1==l2) { r.PB(POINT(l1.x,l1.y)); }
  else if (p1==p2) { r.PB(POINT(p1.x,p2.y)); }
  else{
    double t = (double)( POINTR(l2.x-p2.x) * POINTR(l1.y-l2.y) - POINTR(l2.y-p2.y) * POINTR(l1.x-l2.x) ) /
               (double)( POINTR(p1.x-p2.x) * POINTR(l1.y-l2.y) - POINTR(p1.y-p2.y) * POINTR(l1.x-l2.x) );
    r.PB(POINT(t * (double)p1.x + (1.0-t)*(double)p2.x, t * (double)p1.y + (1.0-t)*(double)p2.y));
  }
  return true;
}

LL area(const vector<Point>& p, vector<int> ord) {
    int n = (int) ord.size();
    LL res = 0;
    for (int i = 0; i < n; ++i) {
        int j = (i + 1) % n;
        res += p[ord[i]].x * (LL) p[ord[j]].y - p[ord[i]].y * (LL) p[ord[j]].x;
    }
    return abs(res);
}

vector<int> alg() {
    int n;
    cin >> n;
    vector<Point> p(n);
    for (int i = 0; i < n; ++i) {
        cin >> p[i].x >> p[i].y;
    }
    vector<int> ord(n);
    for (int i = 0; i < n; ++i) {
        ord[i] = i;
    }
    vector<int> best;
    LL best_area = -(LL) 1e18;
    vector<POINT> r;
    while (ord[0] == 0) {
        bool good = true;
        for (int i = 0; i < n; ++i) {
            int j = (i + 1) % n;
            for (int k = 0; k < n; ++k) {
                int l = (k + 1) % n;
                if (k != i && k != j && l != i && l != j) {
                    if (SegmentCrossPoint(p[ord[i]], p[ord[j]], p[ord[k]], p[ord[l]], r)) {
                        good = false;
                        break;
                    }
                }
            }
            if (!good) {
                break;
            }
        }
        if (good) {
            LL cur = area(p, ord);
            if (cur > best_area) {
                best_area = cur;
                best = ord;
            }
        }
        next_permutation(ALL(ord));
    }
    return best;
}

int main() {
    ios_base::sync_with_stdio(false);
    int d;
    cin >> d;
    for (int i = 1; i <= d; ++i) {
        cout << "Case #" << i << ":";
        vector<int> v = alg();
        FORE (it, v) {
            cout << " " << *it;
        }
        cout << endl;
    }
}
