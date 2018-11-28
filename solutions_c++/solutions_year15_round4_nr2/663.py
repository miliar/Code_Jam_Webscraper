#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <cctype>
#include <cassert>

#define REP(i, a, b) for (int i = (a), _end_ = (b); i < _end_; ++i)
#define debug(...) fprintf(stderr, __VA_ARGS__)
#define EXIT(...) printf(__VA_ARGS__), exit(0)
#define pb push_back
#define SZ(x) (int((x).size()))
#define ALL(x) (x).begin(), (x).end()
#define foreach(e,x) for (__typeof(x.begin()) e=x.begin();e!=x.end();++e)
#define FOR(i,a,b) for (int i=(a);i<=(b);++i)

using namespace std;

const int maxn = 100, max0 = 100000;

const long double eps=1e-13;
class point;
typedef point Vector;
inline int dcmp(const long double &x){return x<-eps?-1:x>eps;}
class point
{
	public:
		long double x,y;
		explicit point(long double x=0,long double y=0):x(x),y(y){}
		friend Vector operator+(const Vector &x,const Vector &y){return Vector(x.x+y.x,x.y+y.y);}
		friend Vector operator-(const Vector &x,const Vector &y){return Vector(x.x-y.x,x.y-y.y);}
		friend Vector operator*(const Vector &x,const long double &p){return Vector(x.x*p,x.y*p);}
		friend Vector operator/(const Vector &x,const long double &p){return Vector(x.x/p,x.y/p);}
		friend long double operator*(const Vector &x,const Vector &y){return x.x*y.x+x.y*y.y;}
		friend long double operator^(const Vector &x,const Vector &y){return x.x*y.y-x.y*y.x;}
		friend bool operator<(const point &x,const point &y){if (dcmp(x.x-y.x)) return x.x<y.x;return dcmp(x.y-y.y)<0;}
		friend bool operator==(const point &x,const point &y){return !dcmp(x.x-y.x)&&!dcmp(x.y-y.y);}
		virtual long double Length() const{return sqrt(*this**this);}
		virtual long double Angle(const Vector &a) const{return acos(*this*a/this->Length()/a.Length());}
		virtual long double Angle() const{return atan2(y,x);}
		virtual Vector &Rotate(const long double &rad){return *this=Vector(x*cos(rad)-y*sin(rad),x*sin(rad)+y*cos(rad));}
		virtual Vector Normal() const{long double L=this->Length();return Vector(-y/L,x/L);}
		virtual Vector ToLength(const long double &Len) const{long double L=Len/this->Length();return Vector(x*L,y*L);}
}O(0,0);
inline long double Angle(const Vector &a,const Vector &b){return a.Angle(b);}
class Line
{
	public:
		point P;
		Vector v;
		long double ang;
		Line(){}
		Line(const point &_P,const Vector &_v):P(_P),v(_v),ang(atan2(v.y,v.x)){}
		virtual bool operator<(const Line &L) const{return ang<L.ang;}
};
inline long double dist(const point &a,const point &b){return (b-a).Length();}
inline long double dist(const pair<point,point> &p){return (p.second-p.first).Length();}

void convex(point *p, const int &n, point *poly, int &top)
{
	sort(p, p + n);
	top = 0;
	poly[top++] = p[0];
	FOR(i, 1, n - 1)
	{
		while (top > 1 && dcmp((p[i] - poly[top - 1]) ^ (p[i] - poly[top - 2])) >= 0) --top;
		poly[top++] = p[i];
	}
	int tmp = top;
	for (int i = n - 2; i >= 0; --i)
	{
		while (top > tmp && dcmp((p[i] - poly[top - 1]) ^ (p[i] - poly[top - 2])) >= 0) --top;
		poly[top++] = p[i];
	}
	if (top > 1) --top;
}

int n;
point a[maxn + 5];

inline bool cmp(const point &a, const point &b)
{
	return a.Angle() < b.Angle();
}

point b[max0 + 5], c[max0 + 5];
int bn = 0;

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i)
	{
		printf("Case #%d: ", i); 
		static double x, y;
		point goal;
		long double tmp0;
		scanf("%d%lf%lf", &n, &x, &y), tmp0 = y, goal.x = x, goal.y = y, goal.y *= goal.x;
		long double l = 1e100, r = 1e-100;
		REP(i, 0, n) 
		{
			scanf("%lf%lf", &x, &y), a[i].x = x, a[i].y = y, a[i].y *= a[i].x;
			l = min(l, (long double)y), r = max(r, (long double)y);
		}
		if ((tmp0 - l) * (tmp0 - r) > 0)
		{
			printf("IMPOSSIBLE\n");
			continue;
		}
		sort(a, a + n, cmp);
		bn = 0;
		REP(i, 0, n) b[bn + 1] = b[bn] + a[i], ++bn;
		REP(i, 0, n) b[bn + 1] = b[bn] - a[i], ++bn;
		int lst = bn - 1;
		long double Max = 0;
		REP(i, 0, bn)
		{
			point u = b[lst], v = b[i] - u;
			if (!dcmp(u ^ goal)) Max = max(Max, u.Length());
			if (!dcmp((u + v) ^ goal)) Max = max(Max, (u + v).Length());
			if (!dcmp(v ^ goal)) continue;
			long double t = (goal ^ u) / (v ^ goal);
			point tmp = u + v * t;
			if (dcmp((tmp - (u + v)) * (tmp - u)) <= 0) Max = max(Max, tmp.Length());
			lst = i;
		}
		printf("%.16f\n", (double)(goal.Length() / Max));
	}
	return 0;
}
