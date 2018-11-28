#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

const int MAXN = 100 + 10;

int n;
double V, T;
double r[MAXN], t[MAXN];

int main(){
	int cas;
	scanf("%d", &cas);
	for (int casi = 1; casi <= cas; ++casi){
		printf("Case #%d: ", casi);
		scanf("%d%lf%lf", &n, &V, &T);
		for (int i=0;i<n;++i)
			scanf("%lf%lf", &r[i], &t[i]);

		if (n == 1){
			if (T != t[0])
				puts("IMPOSSIBLE");
			else
				printf("%.12lf\n", V / r[0]);
		}
		else if (n == 2){
			if ((t[0] > T && t[1] > T) || (t[0] < T && t[1] < T))
				puts("IMPOSSIBLE");
			else if (t[0] == t[1])
				printf("%.12lf\n", V / (r[0] + r[1]));
			else{
				double v0 = V * abs(t[1] - T) / abs(t[0] - t[1]);
				double v1 = V * abs(t[0] - T) / abs(t[0] - t[1]);
				printf("%.12lf\n", max(v0 / r[0], v1 / r[1]));
			}
		}
	}
	return 0;
}
