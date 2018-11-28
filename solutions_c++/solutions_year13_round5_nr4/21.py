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

double f[1<<20];
bool mark[1<<20];
int n;

inline double dfs(int mask)
{
	if (mask + 1 == (1 << n)) {
		return 0;
	}
	if (mark[mask]) {
		return f[mask];
	}
	mark[mask] = true;
	f[mask] = 0;
	for (int i = 0; i < n; ++ i) {
		int j = i, pay = n;
		while (mask >> j & 1) {
			++ j;
			if (j == n) {
				j = 0;
			}
			-- pay;
		}
		f[mask] += (dfs(mask ^ (1 << j)) + pay);
	}
	f[mask] /= n;
	return f[mask];
}

int main()
{
	int T, test = 1;
	for (scanf("%d", &T); test <= T; ++ test) {
		char s[100];
		scanf("%s", s);
		n = strlen(s);
		int mask = 0;
		for (int i = 0; i < n; ++ i) {
			if (s[i] == 'X') {
				mask |= 1 << i;
			}
		}
		memset(mark, false, sizeof(mark));
		printf("Case #%d: %.10f\n", test, dfs(mask));
	}
	return 0;
}

