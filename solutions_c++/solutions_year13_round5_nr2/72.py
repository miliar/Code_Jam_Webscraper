#include <stdio.h>
#include <string.h>
#include <cmath>
#include <algorithm>
using namespace std;

int v[11];
int N;

const int MAXN = 1000;
const double eps = 1e-8, PI = atan2(0, -1);
inline double sqr(double x) {
return x * x;
}
inline bool zero(double x) {
return (x > 0 ? x : -x) < eps;
}
inline int sgn(double x) {
return (x > eps ? 1 : (x + eps < 0 ? -1 : 0));
}

struct point {
double x, y;
point(double x, double y):x(x), y(y) {}
point() {}
bool operator == (const point &a) const {
return sgn(x - a.x) == 0 && sgn(y - a.y) == 0;
}
bool operator != (const point &a) const {
return sgn(x - a.x) != 0 || sgn(y - a.y) != 0;
}
bool operator < (const point &a) const {
return sgn(x - a.x) < 0 || sgn(x - a.x) == 0 && sgn(y - a.y) < 0;
}
point operator + (const point &a) const {
return point(x + a.x, y + a.y);
}
point operator - (const point &a) const {
return point(x - a.x, y - a.y);
}
point operator * (const double &a) const {
return point(x * a, y * a);
}
point operator / (const double &a) const {
return point(x / a, y / a);
}
double operator * (const point &a) const {
return x * a.y - y * a.x; //xmult
}
double operator ^ (const point &a) const {
return x * a.x + y * a.y; //dmult
}
double length() const {
return sqrt(sqr(x) + sqr(y));
}
point trunc(double a) const {
return (*this) * (a / length());
}
point rotate(double ang) const {
point p(sin(ang), cos(ang));
return point((*this) * p, (*this) ^ p);
}
point rotate(const point &a) const {
point p(-a.y, a.x);
p = p.trunc(1.0);
return point((*this) * p, (*this) ^ p);
}
};

bool isConvex(int n, const point *p) {
int i, s[3] = {1, 1, 1};
for(i = 0; i < n && /*s[1] && */ s[0] | s[2]; i++)
s[sgn((p[(i + 1) % n] - p[i]) * (p[(i + 2) % n] - p[i])) + 1] = 0;
return /*s[1] && */ s[0] | s[2];
} //去掉注释即不允许相邻边共线
bool insideConvex(const point &q, int n, const point *p) {
int i, s[3] = {1, 1, 1};
for(i = 0; i < n && /*s[1] && */ s[0] | s[2]; i++)
s[sgn((p[(i + 1) % n] - p[i]) * (q - p[i])) + 1] = 0;
return /*s[1] && */ s[0] | s[2];
} //去掉注释即严格在形内
inline bool dotsInline(const point &p1, const point &p2, const point &p3) {
return zero((p1 - p3) * (p2 - p3));
} //三点共线
inline int decideSide(const point &p1, const point &p2, const point &l1, const point &l2\
) {
return sgn((l1 - l2) * (p1 - l2)) * sgn((l1 - l2) * (p2 - l2));
} //点 p1 和 p2, 直线 l1-l2,-1 表示在异侧,0 表示在线上,1 表示同侧
inline bool dotOnlineIn(const point &p, const point &l1, const point &l2) {
return zero((p - l2) * (l1 - l2)) && (l1.x - p.x) * (l2.x - p.x) < eps && (l1.y - p.\
y) * (l2.y - p.y) < eps;
} //判点是否在线段及其端点上
inline bool parallel(const point &u1, const point &u2, const point &v1, const point &v2)\
{
return zero((u1 - u2) * (v1 - v2));
} //判直线平行
inline bool perpendicular(const point &u1, const point &u2, const point &v1, const point\
&v2) {
return zero((u1 - u2) ^ (v1 - v2));
} //判直线垂直
inline bool intersectIn(const point &u1, const point &u2, const point &v1, const point &\
v2) {
if(!dotsInline(u1, u2, v1) || !dotsInline(u1, u2, v2))
return decideSide(u1, u2, v1, v2) != 1 && decideSide(v1, v2, u1, u2) != 1;
else
return dotOnlineIn(u1, v1, v2) || dotOnlineIn(u2, v1, v2) || dotOnlineIn(v1, u1,\
u2) || dotOnlineIn(v2, u1, u2);
} //判两线段相交, 包括端点和部分重合
inline bool intersectEx(const point &u1, const point &u2, const point &v1, const point &\
v2) {
return decideSide(u1, u2, v1, v2) < 0 && decideSide(v1, v2, u1, u2) < 0;
} //判两线段相交, 不包括端点和部分重合

int graham(int n, point *p, point *ch, bool comEdge = false) {
if(n < 3) {
for(int i = 0; i < n; i++) ch[i] = p[i];
return n;
}
const double e1 = comEdge ? eps : -eps;
int i, j, k;
sort(p, p + n);
ch[0] = p[0];
ch[1] = p[1];
for(i = j = 2; i < n; ch[j++] = p[i++]) while(j > 1 && (ch[j - 2] - ch[j - 1]) * (p[\
i] - ch[j - 1]) > e1) j--;
ch[k = j++] = p[n - 2];
for(i = n - 3; i > 0; ch[j++] = p[i--]) while(j > k && (ch[j - 2] - ch[j - 1]) * (p[\
i] - ch[j - 1]) > e1) j--;
while (j > k && (ch[j - 2] - ch[j - 1]) * (ch[0] - ch[j - 1]) > e1) j--;
return j;
} //求凸包,p 会被打乱顺序,ch 为逆时针,comEdge 为 true 时保留共线点, 重点会导致不稳定

point a[12], p[12], ch[12];
int path[12];
double maxarea;

int flag;

void dfs(int depth, int m, double area) {
	v[m] = 1;
	if (flag) return;
	// for (int i = 0; i < depth; i++) printf(" %d", path[i]); puts("");
	
	if (depth == N) {
		int u = 1;
		for (int j = 1; j < depth - 2; j++) {
			if (intersectIn(a[path[j]], a[path[j+1]], a[m], a[0])) {
				u = 0;
				break;
			}
		}
		if (u == 1) {
			area += a[m] * a[0];
			area = abs(area);
			// printf("depth = %d, m = %d area = %f\n", depth, m, area);
			if (area > 0.5 * maxarea) {
				for (int i = 0; i < depth; i++) {
					printf(" %d", path[i]);
				}
				flag = 1;
			}
		}
		v[m] = 0;
		return;
	}
	for (int i = 0; i < N; i++) {
		int u = 1;
		for (int j = 0; j < depth - 2; j++) {
			if (intersectIn(a[path[j]], a[path[j+1]], a[m], a[i])) {
				u = 0;
				break;
			}
		}
		if (u && v[i] == 0) {
			path[depth] = i;
			// printf("depth = %d, m = %d area = %f\n", depth, m, area + a[m] * a[i]);
			dfs(depth + 1, i, area + a[m] * a[i]);
		}
	}
	v[m] = 0;
}

int main() {
	int T;
	freopen("x.txt", "r", stdin); freopen("w.txt", "w", stdout); 
	scanf("%d", &T);
	for (int re = 1; re <= T; re++) {
		scanf("%d", &N);
		for (int i = 0; i < N; i++) {
			scanf("%lf%lf", &a[i].x, &a[i].y);
			p[i] = a[i];
		}
		int num = graham(N, p, ch);
		maxarea = 0;
		for (int i = 0; i < num; i++) {
			// printf("(%f %f)\n", ch[i].x, ch[i].y);
			maxarea += ch[i] * ch[(i+1) % num];
		}
		maxarea = abs(maxarea);
		// printf("%f\n", maxarea);
		flag = 0;
		memset(v, 0, sizeof(v));
		path[0] = 0;
		printf("Case #%d:", re);
		dfs(1, 0, 0);
		puts("");
	}
}
