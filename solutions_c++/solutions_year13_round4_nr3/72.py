#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <cassert>
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

const int maxn = 2005;

VI adj[maxn];
int degree[maxn], n, lis[maxn], lds[maxn];
int answer[maxn];

inline void add(int a, int b)
{
	adj[a].PB(b);
	++ degree[b];
}

int main()
{
	int T, test = 1;
	for (scanf("%d", &T); test <= T; ++ test) {
		scanf("%d", &n);
		for (int i = 0; i < n; ++ i) {
			adj[i].clear();
			degree[i] = 0;
		}
		for (int i = 0; i < n; ++ i) {
			scanf("%d", &lis[i]);
			for (int j = i - 1; j >= 0; -- j) {
				if (lis[j] + 1 == lis[i]) {
					add(i, j); // a[i] > a[j];
					break;
				}
			}
			for (int j = i - 1; j >= 0; -- j) {
				if (lis[j] >= lis[i]) {
					add(j, i); // a[j] > a[i]
				}
			}
		}
		for (int i = 0; i < n; ++ i) {
			scanf("%d", &lds[i]);
		}
		for (int i = n - 1; i >= 0; -- i) {
			for (int j = i + 1; j < n; ++ j) {
				if (lds[j] + 1 == lds[i]) {
					add(i, j); // a[i] > a[j]
					break;
				}
			}
			for (int j = i + 1; j < n; ++ j) {
				if (lds[j] >= lds[i]) {
					add(j, i); // a[j] > a[i]
				}
			}
		}
		
		for (int i = n; i > 0; -- i) {
			int maxi = -1;
			for (int u = 0; u < n; ++ u) {
				if (degree[u] == 0) {
					maxi = u;
				}
			}
			assert(maxi != -1);
			answer[maxi] = i;
			degree[maxi] = -1;
			FOR (v, adj[maxi]) {
				-- degree[*v];
			}
		}
		printf("Case #%d:", test);
		for (int i = 0; i < n ; ++ i) {
			printf(" %d", answer[i]);
		}
		puts("");
	}
	return 0;
}

