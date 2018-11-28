// Authored by dolphinigle
// GCJ 2013 3

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
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <assert.h>

#define FORN(X,Y) for (int (X) = 0;(X) < (Y);++(X))
#define REP(X,Y,Z) for (int (X) = (Y);(X) < (Z);++(X))

#define RE(X,Y) for (int (X) = 0;(X) < (Y);++(X))
#define FOR(X,Y,Z) for (int (X) = (Y);(X) <= (Z);++(X))

#define SZ(Z) ((int)(Z).size())
#define ALL(W) (W).begin(), (W).end()
#define PB push_back

#define MP make_pair
#define A first
#define B second

#define INF 1023123123
#define EPS 1e-11

#define MX(Z,Y) Z = max((Z),(Y))
#define MN(X,Y) X = min((X),(Y))

#define FORIT(X,Y) for(typeof((Y).begin()) X = (Y).begin();X!=(Y).end();X++)

using namespace std;

typedef long long ll;
typedef double db;
typedef vector<int> vint;

typedef pair<double, double> Point;
typedef pair<Point, Point> Segment;
typedef vector<Point> Polygon;
typedef pair<double, double> Vector;

bool PointEquals(Point p1, Point p2) {
  return abs(p1.A - p2.A) <= EPS && abs(p1.B - p2.B) <= EPS;
}

// straight returns false O(1)
bool IsStrictLeftTurn(Point p1, Point p2, Point p3) {
  return ( p2.A - p1.A ) * ( p3.B - p1.B ) - ( p2.B - p1.B ) * ( p3.A - p1.A ) > EPS;
}

//O(N)
double PolygonArea(Polygon polygon) {
	double ret = 0;
	FORN(i,SZ(polygon)) {
		ret += (db)(polygon[i].A * polygon[(i+1)%SZ(polygon)].B);
		ret -= (db)(polygon[i].B * polygon[(i+1)%SZ(polygon)].A);
	}
	return abs(ret) / 2.0;
}
//vector< polygon > polygon;
//return PolygonArea(polygon);

//O(1)
bool IsIntersecting(Segment segment1, Segment segment2, int* parallel,
    Point* intersection_point) {

  // renamings
	double xx1 = segment1.A.A; double yy1 = segment1.A.B;
  double xx2 = segment1.B.A; double yy2 = segment1.B.B;
	double xx3 = segment2.A.A; double yy3 = segment2.A.B;
	double xx4 = segment2.B.A; double yy4 = segment2.B.B;

	*parallel = 0;
	if (fabs((yy4 - yy3) * (xx2 - xx1) - (xx4 - xx3) * (yy2 - yy1)) <= EPS) {
		*parallel = 1;
    if (PointEquals(segment1.A, segment2.A) || PointEquals(segment1.A, segment2.B)) {
      *intersection_point = segment1.A;
      return true;
    } else if (PointEquals(segment1.B, segment2.A) || PointEquals(segment1.B, segment2.B)) {
      *intersection_point = segment1.B;
      return true;
    }
		return false;
		}
	double ua = ((xx4 - xx3)*(yy1 - yy3) - (yy4-yy3)*(xx1-xx3)) /
      ((yy4-yy3) * (xx2-xx1) - (xx4-xx3) * (yy2 - yy1));
	double& xi = (*intersection_point).A;
	double& yi = (*intersection_point).B;
	xi = xx1 + ua * (xx2 - xx1);
	yi = yy1 + ua * (yy2 - yy1);
	return ( (xi + EPS >= fmin(xx1,xx2)) && (xi - EPS <= fmax(xx1,xx2)) &&
	         (yi + EPS >= fmin(yy1,yy2)) && (yi - EPS <= fmax(yy1,yy2)) &&
			 (xi + EPS >= fmin(xx3,xx4)) && (xi - EPS <= fmax(xx3,xx4)) &&
	         (yi + EPS >= fmin(yy3,yy4)) && (yi - EPS <= fmax(yy3,yy4))
			 );
	}
//IsIntersecting(seg1,seg, &isparallel, &intersectionpoint) //intersect ato touch kaga?

bool IsCollinear(Point p1, Point p2, Point p3) {
  return abs(p1.A * p2.B + p2.A * p3.B + p3.A * p1.B -
			 p1.B * p2.A - p2.B * p3.A - p3.B * p1.A) < EPS;
}

// O(N log N - gift wrapping)
vector< Point > ConvexHull (vector< Point > points) {
	if (SZ(points) <= 2) return points;
	sort(ALL(points));
	points.erase(unique(ALL(points)),points.end());
	vector< pair<double, Point > > p; // sorted clockwise with respect to center
	vector< Point > ans;
	int tn = SZ(points);
	double midx = 0.0,midy = 0.0;
	FORN(i,tn) midx += points[i].first;
	FORN(i,tn) midy += points[i].second;
	midx /= (double)tn;
	midy /= (double)tn;
	FORN(i,tn) p.PB(MP(atan2((double)points[i].second - midy,
                           (double)points[i].first - midx),
                  points[i]));
	sort(ALL(p));
	reverse(ALL(p));
	FORN(i,tn) {
		ans.PB(p[i].second);
		while (SZ(ans) > 2) {
			int bz = SZ(ans);
			if (IsStrictLeftTurn(ans[bz - 1], ans[bz - 2], ans[bz - 3])) break;
			swap(ans[bz - 1],ans[bz - 2]);
			ans.pop_back();
    }
  }

	int pd = 0;
	while (SZ(ans) - pd > 2) {
		//check the last as the MID part
		if (!IsStrictLeftTurn(ans[pd], ans[SZ(ans) - 1] ,ans[SZ(ans) - 2])) {
			ans.pop_back();
			continue;
    }
		if (!IsStrictLeftTurn(ans[pd + 1], ans[pd], ans[SZ(ans) - 1])) {
			pd++;
			continue;
    }
		break;
  }

	vector < Point > trans;
	REP(i,pd,SZ(ans)) trans.PB(ans[i]);
	return trans;
}
// vector<Point> res = ConvexHull(vector<Point> points);

int px[50234];
int py[50234];

int main() {
  int ntc;
  cin >> ntc;
  FORN(itc, ntc) {
    cout << "Case #" << (itc+1) << ":";
    int n;
    cin >> n;
    vector< Point > points;
    FORN(i, n) {
      int x, y;
      cin >> x >> y;
      points.PB(MP((db)x, (db)y));
      px[i] = x;
      py[i] = y;
    }
    db area = PolygonArea(ConvexHull(points));
    vector<int> seq;
    FORN(i, n-1) {
      seq.PB(i);
    }
    do {
      vector<int> s = seq;
      s.PB(n-1);
      // check segment intersection
      int fail = 0;
      FORN(i, n) FORN(j, n) {
        if ((i-j+n)%n < 2 || (j-i+n)%n < 2) {
          // okay
          continue;
        }
//        cout << i << " " << j << endl;
        Segment s1 = MP(points[s[i]], points[s[(i+1)%n]]);
        Segment s2 = MP(points[s[j]], points[s[(j+1)%n]]);
        int a;
        Point t;
        if (IsIntersecting(s1, s2, &a, &t)) {
          // fail
          //cout << "intersection failure" << endl;
          fail = 1;
          break;
        }
      }
      // collinearity check
      FORN(i, n) {
        int c1 = s[i];
        int c2 = s[(i+1)%n];
        int c3 = s[(i+2)%n];
        if (IsCollinear(points[c1], points[c2], points[c3])) {
          // check if a <= b <= c
          if (px[c2] == px[c1]) {
            // compare by y
            if (py[c2] > py[c1] && py[c2] > py[c3]) {
              fail = 1;
            }
            if (py[c2] < py[c1] && py[c2] < py[c3]) {
              fail = 1;
            }
          } else {
            if (px[c2] > px[c1] && px[c2] > px[c3]) {
              fail = 1;
            }
            if (px[c2] < px[c1] && px[c2] < px[c3]) {
              fail = 1;
            }
          }
        }
      }
      if (!fail) {
        // calculate area
        vector< Point > ps;
        FORN(i, n) {
          ps.PB(points[s[i]]);
        }
        db myarea = PolygonArea(ps);
        if (myarea * 2 > area + EPS) {
          // found
          FORN(i, n) {
            cout << " " << s[i];
          }
          cout << endl;
          break;
        }
      }
    } while (next_permutation(ALL(seq)));
  }
}
