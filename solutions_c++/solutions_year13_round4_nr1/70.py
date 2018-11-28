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
//================================

const long long base = 1000002013LL;

inline void mod(long long &a)
{
	a %= base;
	if (a < 0) {
		a += base;
	}
}

long long sum(long long r, long long l)
{
	return (l + r) * (r - l + 1) / 2 % base;
}

int main()
{
	int T, test = 1;
	for (scanf("%d", &T); test <= T; ++ test) {
		int n, m;
		scanf("%d%d", &n, &m);
		vector<PII> event;
		vector<PII> ticket;
		long long answer = 0;
		for (int i = 0; i < m; ++ i) {
			int a, b, c;
			scanf("%d%d%d", &a, &b, &c);
			answer += (long long) c * sum(n, n - (b - a - 1));
			mod(answer);
			event.PB(MP(a, -c));
			event.PB(MP(b, c));
		}
		sort(event.begin(), event.end());
		for (int i = 0; i < event.size(); ++ i) {
			int index = event[i].first;
			int delta = event[i].second;
			if (delta < 0) {
				ticket.PB(MP(index, -delta));
			} else {
				while (delta > 0) {
					int x = min(delta, ticket.back().second);
					answer -= (long long) x * sum(n, n - (index - ticket.back().first - 1));
					mod(answer);
					delta -= x;
					if (x == ticket.back().second) {
						ticket.pop_back();
					} else {
						ticket.back().second -= x;
					}
				}
			}
		}
		printf("Case #%d: %I64d\n", test, answer);
	}
	return 0;
}

