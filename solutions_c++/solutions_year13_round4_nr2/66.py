#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <sstream>
using namespace std;

#define PB push_back
#define MP make_pair

#define FOR(it,a) for (__typeof((a).begin()) it=(a).begin();it!=(a).end();++it)
#define sqr(x) ((x)*(x))
#define lowbit(x) ((x)&(-(x)))

const double PI = acos(-1.0);
const double EPS = 1e-8;

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<string> VS;

inline double mySqrt(double x)
{
	if (x < EPS) {
		return 0;
	}
	return sqrt(x);
}

inline int signum(double x)
{
	if (x < -EPS) {
		return -1;
	}
	return x > EPS;
}

struct Point
{
	double x, y;
	Point(){}
	Point(double x, double y): x(x), y(y){}
	double norm(){
		return sqrt(x * x + y * y);
	}
	void rotate(double ang) {
		double co = cos(ang), si = sin(ang);
		double tx = x, ty = y;
		x = tx * co - ty * si;
		y = tx * si + ty * co;
	}
};

inline Point operator + (const Point &a,const Point &b) {return Point(a.x + b.x, a.y + b.y);}
inline Point operator - (const Point &a,const Point &b) {return Point(a.x - b.x, a.y - b.y);}
inline Point operator * (const Point &a,const double &b) {return Point(a.x * b, a.y * b);}
inline Point operator / (const Point &a,const double &b) {return Point(a.x / b, a.y / b);}
inline double det(const Point &a, const Point &b) {return a.x * b.y - a.y * b.x;}
inline double dot(const Point &a, const Point &b) {return a.x * b.x + a.y * b.y;}
//==========================

long long calc(int n, long long x)
{
	long long small = x;
	long long rank = 0;
	for (int round = n - 1; round >= 0; -- round) {
		if (small > 0) {
			rank |= 1LL << round;
			-- small;
			small = small / 2;
		} else {
			break;
		}
	}
	return rank + 1;
}

long long prob(int n, long long p)
{
	long long all = (1LL << n) - 1;
	long long l = 0, r = (1LL << n);
	p = all + 2 - p;
	while (l + 1 < r) {
		long long mid = (l + r) / 2;
		if (calc(n, all - mid) >= p) {
			l = mid;
		} else {
			r = mid;
		}
	}
	return l;
}

long long must(int n, long long p)
{
	long long l = 0, r = (1LL << n);
	while (l + 1 < r) {
		long long mid = (l + r) / 2;
		if (calc(n, mid) <= p) {
			l = mid;
		} else {
			r = mid;
		}
	}
	return l;
}

int main()
{
	//printf("%I64d\n", calc(3, 2));
	int T;
	scanf("%d", &T);
	for (int test = 1; test <= T; ++ test) {
		int n;
		long long p;
		scanf("%d%I64d", &n, &p);
		printf("Case #%d: %I64d %I64d\n", test, must(n, p), prob(n, p));
	}
	return 0;
}

