#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

struct point{
	int x; int y; int z;
}p[1111];

struct edge {
	int u, v; double d;
}e[1111*1111];

double d(int x, int y){
	double a = p[x].x - p[y].x;
	double b = p[x].y - p[y].y;
	double c = p[x].z - p[y].z;
	return sqrt(a *a + b * b + c * c);
}

bool cmp(edge x, edge y){
	return x.d < y.d;
}

int fa[1111];

int getf(int x){
	if (fa[x] == x)
		return x;
	else return fa[x] = getf(fa[x]);
}

int merge(int x, int y){
	int u = getf(x), v = getf(y);
	fa[u] = v;
}

int main(){
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);

	int t; scanf("%d", &t);
	for (int cas = 1; cas <= t; cas++) {
		printf("Case #%d: ", cas);
		int n, s;
		scanf("%d%d", &n, &s);
		for (int i = 0; i < n; i++) {
			scanf("%d%d%d", &p[i].x, &p[i].y, &p[i].z);
			scanf("%*d%*d%*d");
			//printf("%d %d %d\n", p[i].x, p[i].y, p[i].z);
		}
		for (int i = 0; i < n; i++)
			fa[i] = i;
		int es = 0;
		for (int i = 0 ; i < n; i++)
			for (int j = 0; j < n; j++) {
				e[es].u = i;
				e[es].v = j;
				e[es].d = d(i ,j);
				es++;
			}
		sort(e, e + es, cmp);
		for (int i = 0; i < es; i++) {
			merge(e[i].u, e[i].v);
			if (getf(0) == getf(1)) {
				printf("%f\n", e[i].d);
				break;
			}
		}
	}
}