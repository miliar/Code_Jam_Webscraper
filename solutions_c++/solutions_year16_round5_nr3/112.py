#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker,"/STACK:32000000")
#include <algorithm>
#include <numeric>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <cassert>

using namespace std;

#define REP(i,n) for (int i=0,_n=(n); i < _n; i++)
#define REPD(i,n) for (int i=(n)-1; i >= 0; i--)
#define FOR(i,a,b) for (int _b=(b), i=(a); i <= _b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))

#define CLEAR(x) memset(x,0,sizeof x);
#define CLEARA(x) memset(&x,0,sizeof x);
#define FILL(x,v) memset(x,v,sizeof x);
#define FILLA(x,v) memset(&x,v,sizeof x);

#define VAR(a,b) __typeof(b) a=(b)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)

#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 0x7fffffff
#define X first
#define Y second
#define pb push_back
#define SZ(c) (int)(c).size()
#define MP make_pair
#define eps 1.0e-11
const double pi = acos(-1.0);

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;

template<typename T> struct Point {
	T x,y,z;
	Point() : x(0),y(0),z(0) {}
	Point(T _x,T _y,T _z) : x(_x),y(_y),z(_z) {}
	void read() { scanf("%d%d%d",&x,&y,&z); }
	T len2() const;
	double len() const;
	Point<T> norm() const;
};

template<typename T> Point<T> operator+ (const Point<T> &a, const Point<T> &b) { return Point<T>(a.x+b.x,a.y+b.y,a.z+b.z); }
template<typename T> Point<T> operator- (const Point<T> &a, const Point<T> &b) { return Point<T>(a.x-b.x,a.y-b.y,a.z-b.z); }
template<typename T> Point<T> operator* (const T a, const Point<T> &b) { return Point<T>(a*b.x,a*b.y,a*b.z); }
template<typename T> Point<T> operator* (const Point<T> &b, const T a) { return a*b; }
template<typename T> T operator* (const Point<T> &a, const Point<T> &b) { return a.x*b.x+a.y*b.y+a.z*b.z; }
template<typename T> Point<T> operator^ (const Point<T> &a, const Point<T> &b) { return Point<T>(a.y*b.z-a.z*b.y, a.z*b.x-a.x*b.z, a.x*b.y-a.y*b.x); }
template<typename T> T Point<T>::len2() const { return ((*this)*(*this)); }
template<typename T> double Point<T>::len() const { return sqrt((double)((*this)*(*this))); }
template<typename T> Point<T> Point<T>::norm() const { return (1.0/len())*(*this); }

typedef Point<int> IPnt;

#define N 1024
int n,s;
IPnt a[N],v[N];

bool basic(double limit)
{
	REP(i,n) if (v[i].len2() != 0) return false;
	static bool mark[N];
	CLEAR(mark);
	queue<int> q;
	q.push(0);
	mark[0]=true;
	while (!q.empty()) {
		int x = q.front();
		q.pop();
		if (x==1) return true;
		REP(i,n) if (!mark[i] && (a[i]-a[x]).len2() <= limit*limit)
		{
			mark[i]=true;
			q.push(i);
		}
	}
	return false;
}

int main(int argc, char **argv)
{
	string FN = "C-small-attempt0";
	if (argc>1) FN = string(argv[1]);
	int shift = 0;
	if (argc>2) sscanf(argv[2],"%d",&shift);
	freopen((FN+".in").c_str(),"r",stdin);
	freopen((FN+".out").c_str(),"w",stdout);

	int tests;
	scanf("%d",&tests);
	for (int test = 1; test<=tests; test++)
	{
		fprintf(stderr,"=== %s : %d\n", FN.c_str(), test+shift);
		printf("Case #%d: ",test+shift);
		////////////////////////////////////////////////////////////
		scanf("%d%d",&n,&s);
		REP(i,n) a[i].read(),v[i].read();
		double left=0,right=100000;
		REP(step,50) {
			double mid = (left+right)/2;
			if (basic(mid))
				right = mid;
			else
				left=mid;
		}
		printf("%.12lf\n",left);
	}
	fprintf(stderr,"=== %s DONE\n", FN.c_str());
	return 0;
}