#include <vector>
#include <map>
#include <numeric>
#include <iostream>
#include <cmath>
#include <cstdio>
#include <cassert>
#include <cstring>
#include <algorithm>
#include <ctime>
#include <stack>
using namespace std;
typedef long long ll;
#define REP(i,n) for(int i=0;i<(n);i++)
const double EPS=1e-7;

struct point
{
	double x,y,z;
	point(double x=0, double y=0, double z=0):x(x),y(y),z(z)
	{
	}
	point operator+(const point& b) const
	{
		return point(x+b.x, y+b.y, z+b.z);
	}
	point operator-(const point& b) const
	{
		return point(x-b.x, y-b.y, z-b.z);
	}
	double inner(const point& b) const
	{
		return x*b.x + y*b.y + z*b.z;
	}
	double norm2() const
	{
		return inner(*this);
	}
	double norm() const
	{
		return sqrt(norm2());
	}
};

struct DSU
{
	int n;
	int *p;
	DSU(int n):n(n),p(new int[n])
	{
		REP(i,n)
			p[i]=i;
	}
	~DSU()
	{
		delete[] p;
	}
	int get(int a)
	{
		if(p[a]==a) return a;
		return p[a]=get(p[a]);
	}
	bool unite(int a, int b)
	{
		a=get(a);
		b=get(b);
		p[a]=b;
		return a!=b;
	}
};

double solve()
{
	int n,s;
	scanf("%d%d",&n,&s);
	vector<point> v;
	vector<pair<double, pair<int,int> > > d;
	REP(i,n)
	{
		double x,y,z;
		scanf("%lf%lf%lf",&x,&y,&z);
		v.push_back(point(x,y,z));
		scanf("%*f%*f%*f");
	}
	REP(i,n) REP(j,n)
		d.push_back(make_pair((v[i]-v[j]).norm2(),make_pair(i,j)));
	double res=0;
	sort(d.begin(), d.end());
	DSU dsu(n);
	for(int i=0;i<(int)d.size() && dsu.get(0)!=dsu.get(1);i++)
	{
		if(dsu.unite(d[i].second.first, d[i].second.second))
		{
			res=d[i].first;
		}
	}
	return sqrt(res);
}

int main()
{
	int T;
	scanf("%d",&T);
	for(int test=1;test<=T;test++)
		printf("Case #%d: %.10lf\n",test, solve());
	return 0;
}
