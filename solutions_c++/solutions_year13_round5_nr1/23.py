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

vector<LL> event;

inline void addEvent(LL x)
{
	for (int d = -1000; d <= 1000; ++ d) {
		if (x + d >= 0) {
			event.PB(x + d);
		}
	}
}

int main()
{
	int T, test = 1;
	for (scanf("%d", &T); test <= T; ++ test) {
		int n;
		LL x[100];
		LL B;
		scanf("%I64d%d", &B, &n);
		for (int i = 0; i < n; ++ i) {
			scanf("%I64d", &x[i]);
		}
		for (int i = n; i <= 36; ++ i) {
			x[i] = 0;
		}
		n = 37;
		sort(x, x + n);
		
		event.clear();
		LL sum = 0;
		for (int i = 0; i < n; ++ i) {
			addEvent(x[i]);
			sum += x[i];
			addEvent((B + sum) / (i + 1));
		}
		
		double ans = 0;
		FOR (it, event) {
			LL mini = *it;
			int last = -1;
			for (int i = 0; i < n; ++ i) {
				if (x[i] <= mini) {
					last = i;
				}
			}
			for (int i = 0; i <= last + 1; ++i) {
				LL profit = 0;
				LL cnt = 0;
				LL bet = 0;
				for (int j = 0; j < i; ++ j) {
					if (x[j] <= mini) {
						bet += mini - x[j];
						profit += mini - x[j];
						++ cnt;
					}
				}
				for (int j = i; j <= last; ++ j) {
					if (x[j] <= mini) {
						bet += mini + 1 - x[j];
					}
				}
				if (bet <= B) {
					ans = max(ans, ((double)profit / cnt * 36 - bet));
				}
			}
		}
		
		printf("Case #%d: %.10f\n", test ,ans);
	}
	return 0;
}

