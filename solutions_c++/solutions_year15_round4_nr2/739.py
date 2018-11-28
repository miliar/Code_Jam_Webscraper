#include <cstdio>
#include <algorithm>
const double eps = 1e-12;
const int N = 110;
int T, n;
double V, X, R[N], C[N], t1, t2;
double abs(double x){
	return x >= 0 ? x : -x;
}
int main(){
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	scanf("%d", &T);
	for (int Ti = 1; Ti <= T; ++Ti){
		scanf("%d%lf%lf", &n, &V, &X);
		for (int i = 1; i <= n; ++i)
			scanf("%lf%lf", &R[i], &C[i]);
		printf("Case #%d: ", Ti);
		if (n == 1){
			if (abs(X - C[1]) < eps) printf("%.10f\n", V / R[1]);
			else printf("IMPOSSIBLE\n");
		}
		else{
			if (std::max(C[1], C[2]) >= X && std::min(C[1], C[2]) <= X){
				if (abs(C[1] - C[2]) < eps){
					printf("%.10f\n", V / (R[1] + R[2]));
				}
				else{
					t1 = V * (X - C[1]) / (R[2] * (C[2] - C[1]));
					t2 = V * (X - C[2]) / (R[1] * (C[1] - C[2]));
					printf("%.10f\n", std::max(t1, t2));
				}
			}
			else printf("IMPOSSIBLE\n");
		}
	}
	return 0;
}
