#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <valarray>
#include <vector>

#define EPS 1e-9
#define INF 1070000000LL
#define MOD 1000000007LL
#define fir first
#define foreach(it,X) for(__typeof((X).begin()) it=(X).begin();it!=(X).end();it++)
#define ite iterator
#define mp make_pair
#define rep(i,n) rep2(i,0,n)
#define rep2(i,m,n) for(int i=m;i<(n);i++)
#define pb push_back
#define sec second
#define sz(x) ((int)(x).size())

using namespace std;

struct timer{
	time_t start;
	timer(){start=clock();}
	~timer(){cerr<<1.*(clock()-start)/CLOCKS_PER_SEC<<" secs"<<endl;}
};

typedef istringstream iss;
typedef long long ll;
typedef pair<int,int> pi;
typedef stringstream sst;
typedef vector<int> vi;

#define PI 3.14159265358979323846

#define curr(P, i) P[(i) % P.size()]
#define next(P, i) P[(i+1) % P.size()]
#define prev(P, i) P[(i+P.size()-1) % P.size()]
#define diff(P, i) (next(P,i) - curr(P,i))
#define EQ(x,y) (fabs((x)-(y))<EPS)
#define GE(x,y) ((x)+EPS>(y))
#define LE(x,y) ((x)<(y)+EPS)
enum { OUT, ON, IN };

typedef complex<double> P;
typedef vector<P> G;

namespace std{
  bool operator < (const P& a, const P& b) {
    return real(a) != real(b) ? real(a) < real(b) : imag(a) < imag(b);
  }
}

double cross(const P& a, const P& b) {
  return imag(conj(a)*b);
}
double dot(const P& a, const P& b) {
  return real(conj(a)*b);
}

struct L : public vector<P> {
  L(){}
  L(const P &a, const P &b) {
    push_back(a); push_back(b);
  }
};

struct C {
  P p; double r;
  C(const P &p, double r) : p(p), r(r) { }
};

int ccw(P a, P b, P c) {
  b -= a; c -= a;
  if (cross(b, c) > EPS)   return +1;       // counter clockwise
  if (cross(b, c) < -EPS)   return -1;       // clockwise
  if (dot(b, c) < -EPS)     return +2;       // c--a--b on line
  if (norm(b) < norm(c)+EPS) return -2;       // a--b--c on line
  return 0;
}

bool intersectLL(const L &l, const L &m) {
  return abs(cross(l[1]-l[0], m[1]-m[0])) > EPS || // non-parallel
         abs(cross(l[1]-l[0], m[0]-l[0])) < EPS;   // same line
}
bool intersectLS(const L &l, const L &s) {
  return cross(l[1]-l[0], s[0]-l[0])*       // s[0] is left of l
         cross(l[1]-l[0], s[1]-l[0]) < EPS; // s[1] is right of l
}
bool intersectLP(const L &l, const P &p) {
  return abs(cross(l[1]-p, l[0]-p)) < EPS;
}
bool intersectSS(const L &s, const L &t) {
  return ccw(s[0],s[1],t[0])*ccw(s[0],s[1],t[1]) <= 0 &&
         ccw(t[0],t[1],s[0])*ccw(t[0],t[1],s[1]) <= 0;
}
bool intersectSP(const L &s, const P &p) {
  return abs(s[0]-p)+abs(s[1]-p)-abs(s[1]-s[0]) < EPS; // triangle inequality
}

P projection(const L &l, const P &p) {
  double t = dot(p-l[0], l[0]-l[1]) / norm(l[0]-l[1]);
  return l[0] + t*(l[0]-l[1]);
}
P reflection(const L &l, const P &p) {
  return p + 2.0 * (projection(l, p) - p);
}
double distanceLP(const L &l, const P &p) {
  return abs(p - projection(l, p));
}
double distanceLL(const L &l, const L &m) {
  return intersectLL(l, m) ? 0 : distanceLP(l, m[0]);
}
double distanceLS(const L &l, const L &s) {
  if (intersectLS(l, s)) return 0;
  return min(distanceLP(l, s[0]), distanceLP(l, s[1]));
}
double distanceSP(const L &s, const P &p) {
  const P r = projection(s, p);
  if (intersectSP(s, r)) return abs(r - p);
  return min(abs(s[0] - p), abs(s[1] - p));
}
double distanceSS(const L &s, const L &t) {
  if (intersectSS(s, t)) return 0;
  return min(min(distanceSP(s, t[0]), distanceSP(s, t[1])),
             min(distanceSP(t, s[0]), distanceSP(t, s[1])));
}
P crosspoint(const L &l, const L &m) {
  double A = cross(l[1] - l[0], m[1] - m[0]);
  double B = cross(l[1] - l[0], l[1] - m[0]);
  if (abs(A) < EPS && abs(B) < EPS) return m[0]; // same line
  if (abs(A) < EPS) assert(false); // !!!PRECONDITION NOT SATISFIED!!!
  return m[0] + B / A * (m[1] - m[0]);
}

vector<P> crosspointLC(const L &l, const C &c){
	vector<P> res;
	P p = projection(l, c.p);
	double d1 = abs(p - c.p);
	if(EQ(d1, c.r)){
		res.pb(p);
		return res;
	}
	if(d1 > c.r){
		return res;
	}
	double d2 = sqrt(c.r*c.r - d1*d1);
	P v = d2/abs(l[1] - l[0]) * (l[1] - l[0]);
	res.pb(p + v);
	res.pb(p - v);
	return res;
}

#define sq(x) ((x)*(x))

vector<P> crosspointCC(const C &c1, const C &c2){
	vector<P> res;
	P v = c2.p - c1.p;
	double d = abs(v);
	if(d < EPS){
		if(EQ(c1.r, c2.r)){ // coincide
			res.pb(c1.p + P(c1.r, 0));
		}
		return res;
	}
	vector<double> thetas;
	if(EQ(d, c1.r + c2.r)){
		thetas.pb(0);
	}else if(EQ(d, c1.r - c2.r)){
		thetas.pb(0);
	}else if(EQ(d, c2.r - c1.r)){
		thetas.pb(PI);
	}else if(d > c1.r + c2.r || d < abs(c1.r - c2.r)){
		return res;
	}else{
		double t = acos((sq(c1.r) + sq(d) - sq(c2.r))
			/ (2.0 * c1.r * d));
		thetas.pb(t);
		thetas.pb(-t);
	}
	rep(i, sz(thetas)){
		res.pb(c1.p + c1.r/d * v
			* P(cos(thetas[i]), sin(thetas[i])));
	}
	return res;
}


vector<L> tangentPC(const P& p, const C& c){
	vector<L> res;
	P v = c.p - p;
	double d1 = abs(v), d2;
	if(EQ(d1, c.r)){
		d2 = sqrt(sq(d1) - sq(c.r));
		P q = p + v * P(cos(PI/2.0), sin(PI/2.0));
		res.pb(L(q, p));
		return res;
	}else if(d1 < c.r){
		return res;
	}else{
		d2 = sqrt(sq(d1) - sq(c.r));
		double t = atan2(c.r, d2);
		P q = p + d2/d1 * v * P(cos(t), sin(t));
		res.pb(L(p, q));
		q = p + d2/d1 * v * P(cos(-t), sin(-t));
		res.pb(L(p, q));
		return res;
	}
}

vector<L> commontangentCC(const C& c1, const C& c2){
	vector<L> res;
	P v = c2.p - c1.p;
	double d = abs(v);
	if(d < EPS){
		if(EQ(c1.r, c2.r)){ // coinside
			P q1 = c1.p + P(c1.r, 0);
			P q2 = q1 + P(0, c1.r);
			res.pb(L(q1, q2));
		}
		return res;
	}
	if(d + EPS <= abs(c1.r - c2.r)){
		return res;
	}else if(EQ(d, c1.r - c2.r)){
		P q1 = c1.r/d * v;
		P q2 = q1 + v * P(cos(PI/2.0), sin(PI/2.0));
		res.pb(L(q1, q2));
		return res;
	}else if(EQ(d, c2.r - c1.r)){
		P q1 = c2.r/d * -v;
		P q2 = q1 + v * P(cos(PI/2.0), sin(PI/2.0));
		res.pb(L(q1, q2));
		return res;
	}else{
		double t1 = asin((c2.r - c1.r)/d) + PI/2.0;
		P q1 = c1.p + c1.r/d * v * P(cos(t1), sin(t1));
		P q2 = c2.p + c2.r/d * v * P(cos(t1), sin(t1));
		res.pb(L(q1, q2));
		q1 = c1.p + c1.r/d * v * P(cos(-t1), sin(-t1));
		q2 = c2.p + c2.r/d * v * P(cos(-t1), sin(-t1));
		res.pb(L(q1, q2));
		if(d + EPS <= c1.r + c2.r){
			return res;
		}else if(EQ(d, c1.r + c2.r)){
			P q3 = c1.p + c1.r/d * v;
			P q4 = q3 + v * P(cos(PI/2.0), sin(PI/2.0));
			res.pb(L(q3, q4));
		}else{
			double t2 = acos((c1.r + c2.r)/d);
			P q3 = c1.p + c1.r/d * v * P(cos(t2), sin(t2));
			P q4 = c2.p - c2.r/d * v * P(cos(t2), sin(t2));
			res.pb(L(q3, q4));
			q3 = c1.p + c1.r/d * v * P(cos(-t2), sin(-t2));
			q4 = c2.p - c2.r/d * v * P(cos(-t2), sin(-t2));
			res.pb(L(q3, q4));
		}
	}
	return res;
}

vector<C> tangentcircleLL(const L& l, const L& m, const double& r){
	vector<C> res;
	if(abs(cross(l[1]-l[0], m[1]-m[0])) < EPS){ // parallel
		double d = distanceLL(l, m);
		if(EQ(d, r*2.0)){
			P p = P(l[0] + r/abs(l[1]-l[0]) * (l[1]-l[0])
				* P(cos(PI/2), sin(PI/2)));
			res.pb(C(p, r));
		}
		return res;
	}
	P p = crosspoint(l, m);
	double t1 = (arg(m[1]-m[0]) - arg(l[1]-l[0])) / 2.0;
	P v1 = abs(r/sin(t1)) / abs(l[1]-l[0]) * (l[1]-l[0])
		* P(cos(t1), sin(t1));
	double t2 = PI/2 - t1;
	P v2 = abs(r/sin(t2)) / abs(m[1]-m[0]) * (m[1]-m[0])
		* P(cos(t2), sin(t2));
	res.pb(C(p + v1, r));
	res.pb(C(p + v2, r));
	res.pb(C(p - v1, r));
	res.pb(C(p - v2, r));
	return res;
}

#undef sq

int contains(const G& g, const P& p) {
  bool in = false;
  for (int i = 0; i < g.size(); ++i) {
    P a = curr(g,i) - p, b = next(g,i) - p;
    if (imag(a) > imag(b)) swap(a, b);
    if (imag(a) <= 0 && 0 < imag(b))
      if (cross(a, b) < 0) in = !in;
    if (cross(a, b) == 0 && dot(a, b) <= 0) return ON;
  }
  return in ? IN : OUT;
}

#define d(k) (dot(p[k], l[1] - l[0]))
P extreme(const vector<P> &p, const L &l) {
  int k = 0;
  for (int i = 1; i < p.size(); ++i)
    if (d(i) > d(k)) k = i;
  return p[k];
}

#undef d

double area2(const G& p) {
  double A = 0;
  for (int i = 0; i < p.size(); ++i) 
    A += cross(curr(p, i), next(p, i));
  return A;
}

vector<P> convex_hull(vector<P> ps) {
  int n = ps.size(), k = 0;
  sort(ps.begin(), ps.end());
  vector<P> ch(2*n);
  for (int i = 0; i < n; ch[k++] = ps[i++]) // lower-hull
    while (k >= 2 && ccw(ch[k-2], ch[k-1], ps[i]) <= 0) --k;
  for (int i = n-2, t = k+1; i >= 0; ch[k++] = ps[i--]) // upper-hull
    while (k >= t && ccw(ch[k-2], ch[k-1], ps[i]) <= 0) --k;
  ch.resize(k-1);
  return ch;
}

bool isconvex(const G &P) {
  for (int i = 0; i < P.size(); ++i)
    if (ccw(prev(P, i), curr(P, i), next(P, i)) > 0) return false;
  return true;
}

G convex_cut(const G& p, const L& l) {
  G Q;
  for (int i = 0; i < p.size(); ++i) {
    P A = curr(p, i), B = next(p, i);
    if (ccw(l[0], l[1], A) != -1) Q.push_back(A);
    if (ccw(l[0], l[1], A)*ccw(l[0], l[1], B) < 0)
      Q.push_back(crosspoint(L(A, B), l));
  }
  return Q;
}

int convex_contains(const G &Q, const P &p) {
  const int n = Q.size();
  P g = (Q[0] + Q[n/3] + Q[2*n/3]) / 3.0; // inner-point
  int a = 0, b = n;
  while (a+1 < b) { // invariant: c is in fan g-Q[a]-Q[b]
    int c = (a + b) / 2;
    if (cross(Q[a]-g, Q[c]-g) > 0) { // angle < 180 deg
      if (cross(Q[a]-g, p-g) > 0 && cross(Q[c]-g, p-g) < 0) b = c;
      else                                                  a = c;
    } else {
      if (cross(Q[a]-g, p-g) < 0 && cross(Q[c]-g, p-g) > 0) a = c;
      else                                                  b = c;
    }
  }
  b %= n;
  if (cross(Q[a] - p, Q[b] - p) < 0) return 0;
  if (cross(Q[a] - p, Q[b] - p) > 0) return 2;
  return 1;
}

bool intersect_1pt(const P& a, const P& b,
                   const P& c, const P& d, P &r) {
  double D =  cross(b - a, d - c);
  if (EQ(D, 0)) return false;
  double t =  cross(c - a, d - c) / D;
  double s = -cross(a - c, b - a) / D;
  r = a + t * (b - a);
  return GE(t, 0) && LE(t, 1) && GE(s, 0) && LE(s, 1);
}
G convex_intersect(const G &p, const G &Q) {
  const int n = p.size(), m = Q.size();
  int a = 0, b = 0, aa = 0, ba = 0;
  enum { Pin, Qin, Unknown } in = Unknown;
  G R;
  do {
    int a1 = (a+n-1) % n, b1 = (b+m-1) % m;
    double C = cross(p[a] - p[a1], Q[b] - Q[b1]);
    double A = cross(p[a1] - Q[b], p[a] - Q[b]);
    double B = cross(Q[b1] - p[a], Q[b] - p[a]);
    P r;
    if (intersect_1pt(p[a1], p[a], Q[b1], Q[b], r)) {
      if (in == Unknown) aa = ba = 0;
      R.push_back( r );
      in = B > 0 ? Pin : A > 0 ? Qin : in;
    }
    if (C == 0 && B == 0 && A == 0) {
      if (in == Pin) { b = (b + 1) % m; ++ba; }
      else           { a = (a + 1) % m; ++aa; }
    } else if (C >= 0) {
      if (A > 0) { if (in == Pin) R.push_back(p[a]); a = (a+1)%n; ++aa; }
      else       { if (in == Qin) R.push_back(Q[b]); b = (b+1)%m; ++ba; }
    } else {
      if (B > 0) { if (in == Qin) R.push_back(Q[b]); b = (b+1)%m; ++ba; }
      else       { if (in == Pin) R.push_back(p[a]); a = (a+1)%n; ++aa; }
    }
  } while ( (aa < n || ba < m) && aa < 2*n && ba < 2*m );
  if (in == Unknown) {
    if (convex_contains(Q, p[0])) return p;
    if (convex_contains(p, Q[0])) return Q;
  }
  return R;
}

double convex_diameter(const G &pt) {
  const int n = pt.size();
  int is = 0, js = 0;
  for (int i = 1; i < n; ++i) {
    if (imag(pt[i]) > imag(pt[is])) is = i;
    if (imag(pt[i]) < imag(pt[js])) js = i;
  }
  double maxd = norm(pt[is]-pt[js]);

  int i, maxi, j, maxj;
  i = maxi = is;
  j = maxj = js;
  do {
    if (cross(diff(pt,i), diff(pt,j)) >= 0) j = (j+1) % n;
    else i = (i+1) % n;
    if (norm(pt[i]-pt[j]) > maxd) {
      maxd = norm(pt[i]-pt[j]);
      maxi = i; maxj = j;
    }
  } while (i != is || j != js);
  return maxd; /* farthest pair is (maxi, maxj). */
}

#define d(k) (dot(p[k], l[1] - l[0]))
P convex_extreme(const G &p, const L &l) {
  const int n = p.size();
  int a = 0, b = n;
  if (d(0) >= d(n-1) && d(0) >= d(1)) return p[0];
  while (a < b) {
    int c = (a + b) / 2;
    if (d(c) >= d(c-1) && d(c) >= d(c+1)) return p[c];
    if (d(a+1) > d(a)) {
      if (d(c+1) <= d(c) || d(a) > d(c)) b = c;
      else                               a = c;
    } else {
      if (d(c+1) > d(c) || d(a) >= d(c)) a = c;
      else                               b = c;
    }
  }
  return P();
}
#undef d

//#define y2 Y2

int N;
P p[11];

int points[11];
int used[11];

ll maxi;
bool found;

void f(int cur,int mode){
	//cout<<cur<<" "<<mode<<endl;
	if(found)return;
	
	L line[11];
	rep(i,cur-1)line[i]=L(p[points[i]],p[points[i+1]]);
	rep(i,cur-1)rep2(j,i+2,cur-1){
		if(intersectSS(line[i],line[j])){
			return;
		}
	}
	int ok=1;
	if(cur<=2)ok=0;
	else{
		ok=1;
		line[cur-1] = L(p[points[cur-1]],p[points[0]]);
		rep2(i,1,cur-2)if(intersectSS(line[i],line[cur-1])){
			ok=0;
		}
	}
	
	if(ok && (mode==0 && cur>=3 || mode==1 && cur==N)){
		G g;
		rep(i,cur)g.pb(p[points[i]]);
		ll area=area2(g)+EPS;
		if(area<0)area*=-1;
		//cout<<mode<<" "<<area<<endl;
		if(mode==0){
			maxi=max(maxi,area);
			//cout<<maxi<<endl;
		}
		else{
			if(2*area > maxi){
				found=1;
				rep(i,cur)cout<<points[i]<<" ";cout<<endl;
			}
		}
	}
	rep(i,N)if(!used[i]){
		points[cur]=i;
		used[i]=1;
		f(cur+1,mode);
		used[i]=0;
	}
}

void main2(){
	cin>>N;
	rep(i,N){
		int x,y;
		cin>>x>>y;
		p[i]=P(x,y);
	}
	maxi=0;
	fill(used,used+N,0);
	found=0;
	f(0,0);
	cerr<<"maxi: "<<maxi<<endl;
	found=0;
	fill(used,used+N,0);
	f(0,1);
}

int main(){
	int T;
	cin>>T;
	time_t start=clock(),pre=start;
	rep(tc,T){
		cout<<"Case #"<<tc+1<<": ";
		main2();
		time_t now=clock();
		cerr<<tc+1<<"/"<<T<<": "<<(double)(now-pre)/CLOCKS_PER_SEC<<endl;
		if(tc==T-1){
			cerr<<"Total: "<<(double)(now-start)/CLOCKS_PER_SEC<<endl;
			cerr<<"  Ave: "<<(double)(now-start)/CLOCKS_PER_SEC/T<<endl;
		}
		pre=now;
	}
}
