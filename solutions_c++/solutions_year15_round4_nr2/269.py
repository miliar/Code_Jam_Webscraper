#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <vector>

using namespace std;

#define FOR(prom, a, b) for(int prom = (a); prom < (b); prom++)
#define FORD(prom, a, b) for(int prom = (a); prom > (b); prom--)
#define FORDE(prom, a, b) for(int prom = (a); prom >= (b); prom--)

#define DRI(a) int a; scanf("%d ", &a);
#define DRII(a, b) int a, b; scanf("%d %d ", &a, &b);
#define DRIII(a, b, c) int a, b, c; scanf("%d %d %d ", &a, &b, &c);
#define DRIIII(a, b, c, d) int a, b, c, d; scanf("%d %d %d %d ", &a, &b, &c, &d);
#define RI(a) scanf("%d ", &a);
#define RII(a, b) scanf("%d %d ", &a, &b);
#define RIII(a, b, c) scanf("%d %d %d ", &a, &b, &c);
#define RIIII(a, b, c, d) scanf("%d %d %d %d ", &a, &b, &c, &d);

#define PB push_back
#define MP make_pair

#define ll long long
#define ull unsigned long long

#define MM(co, cim) memset((co), (cim), sizeof((co)))

#define DEB(x) cerr << ">>> " << #x << " : " << x << endl;

struct Vector
{
	ll x, y;
	
	Vector(ll a = 0.0, ll b = 0.0): x(a), y(b) { }
	Vector(const Vector & v): x(v.x), y(v.y) { }

	Vector & operator=(const Vector & v) { x = v.x; y = v.y; return *this; }
	Vector operator+(const Vector & v) const { return Vector(x + v.x, y + v.y); }
	Vector & operator+=(const Vector & v) { x += v.x; y += v.y; return *this; }
	Vector operator-(const Vector & v) const { return Vector(x - v.x, y - v.y); }
	Vector & operator-=(const Vector & v) { x -= v.x; y -= v.y; return *this; }
	Vector operator*(ll n) const { return Vector(x * n, y * n); }
	Vector & operator*=(ll n) { x *= n; y *= n; return *this; }
	Vector operator/(ll n) const { return Vector(x / n, y / n); }
	Vector & operator/=(ll n) { x /= n; y /= n; return *this; }

	bool operator<(const Vector & v) const { return x < v.x; }

};

inline ll dot_product(const Vector & v1, const Vector & v2) 
	{ return v1.x * v2.x + v1.y * v2.y; }

inline double cross_product(const Vector & v1, const Vector & v2) 
	{ return (double)v1.x * (double)v2.y - (double)v1.y * (double)v2.x; }

// + => seg2 is to the left from seg1
inline double direction(const Vector & base, const Vector & seg1, const Vector & seg2) 
	{ return cross_product(seg1 - base, seg2 - base); }

void convex_hull(vector<Vector> & points, vector<Vector> & hull)
{
	sort(points.begin(), points.end());
	vector<Vector> top, bot;
	for (int i = 0; i < points.size(); ++i)
	{
		while (top.size() >= 2 && direction(top[top.size()-2], top[top.size()-1], points[i]) > 0)
			top.pop_back();
		top.push_back(points[i]);
		while (bot.size() >= 2 && direction(bot[bot.size()-2], bot[bot.size()-1], points[i]) < 0)
			bot.pop_back();
		bot.push_back(points[i]);
	}
	reverse(bot.begin(), bot.end());
	hull = top;
	if (bot.size() > 2) hull.insert(hull.end(), bot.begin()+1, bot.end()-1);
}

void printVec(Vector a) {
  printf(" %lf %lf\n", a.x, a.y);
}

vector<Vector> source;

ll readV() {
  ll a, r;
  scanf("%lld", &r);
  r *= 10000LL;
  scanf(".");
  scanf("%lld", &a);
  r += a;
  return r;
}

int main ()
{
  // TODO errors
  DRI(T);
  FOR(t,0,T) {
    source.clear();
    DRI(N);
    ll V, X;
    V = readV();
    X = readV();
    
    FOR(i,0,N) {
      ll R, C;
      R = readV();
      C = readV();
      source.PB(Vector(C,R));
    }
    ll sumV = 0;
    ll sumE = 0;
    FOR(i,0,N) {
      sumV += source[i].y;
      sumE += source[i].y*source[i].x;
    }
    sort(source.begin(),source.end());
    if(source[0].x > X || source[N-1].x < X) {
      printf("Case #%d: IMPOSSIBLE\n", t+1);
      continue;
    }
    bool tooHot = true;
    if(sumE < X*sumV) {reverse(source.begin(),source.end()); tooHot = false;}
    // TODO ==?
    FOR(i,0,N) {
      ll tmp = source[i].x;
      source[i].x = source[i].y;
      source[i].y = tmp;
      source[i].y *= source[i].x;
    }
    Vector req(V,V*X);
    Vector cur(0,0);
    
    double res = 0;
    FOR(i,0,N) {
      cur += source[i];
      if(tooHot) {
        if(cur.y/cur.x > X || (cur.y/cur.x == X && cur.y%cur.x > 0LL)) {
          // TODO
          double d2 = fabs(cross_product(cur,req));
          cur -= source[i];
          double d1 = fabs(cross_product(cur,req));
          res += source[i].x*d1/(d1+d2);
          break;
        }
        res = cur.x;
      } else {
        if(cur.y/cur.x < X || (cur.y/cur.x == X && cur.y%cur.x < 0LL)) {
          // TODO
          double d2 = fabs(cross_product(cur,req));
          cur -= source[i];
          double d1 = fabs(cross_product(cur,req));
          res += source[i].x*d1/(d1+d2);
          break;
        }
        res = cur.x;
      }
    }
    printf("Case #%d: %.9lf\n", t+1, (double)V/(double)res);
    
    
    
    /*
    //printVec(req);
    //printVec(cur);
    //FOR(i,0,N) printVec(source[i]);
    FOR(i,0,N) {
      //printf("%d\n", i);
      if(fabs((double)req.y/(double)req.x-(double)cur.y/(double)cur.x) < 1e-9) break;
      
      double dir1 = cross_product(req,cur);
      cur -= source[i];
      double dir2 = cross_product(req,cur);
      //printVec(cur);
      if((dir1 >= 0) != (dir2 >= 0)) {
        dir1 = fabs(dir1);
        dir2 = fabs(dir2);
        source[i] *= dir2/(dir1+dir2);
        //printVec(source[i]);
        cur += source[i];
        break;
      }
    }
    //printf("%lf\n", cur.x);
    if(cur.x > 1e-9) {
      printf("Case #%d: %.9lf\n", t+1, V/cur.x);
    } else printf("Case #%d: IMPOSSIBLE\n", t+1);
    */
  }
  return 0;
}
