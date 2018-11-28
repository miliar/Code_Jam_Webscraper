#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef pair <LL, LL> PII;
const int MAXN = 1e6 + 7, INF = 1e9 + 7;

int main(){
	int t; scanf("%d", &t);
	for (int cas = 1; cas <= t; cas++){
		printf("Case #%d: ", cas);
		int n; double V, X;
		scanf("%d", &n); 
		scanf("%lf%lf", &V, &X);
		if (n == 1){
			double v, x;
			scanf("%lf%lf", &v, &x);
			if (x != X) puts("IMPOSSIBLE");
			else{
				printf("%.9lf\n", V/v);
			}
		}
		else{
			double v1, v2, x1, x2;
			scanf("%lf%lf%lf%lf", &v1, &x1, &v2, &x2);
			//cout << v1 << ' ' << x1 << ' ' << v2 << ' ' << x2 << endl;
			if (fabs(x1 - x2) < 1e-8){
				if (fabs(x1 - X) < 1e-8){
					double rst = V / (v1 + v2);
					printf("%.9lf\n", rst);	
				}
				else{
					puts("IMPOSSIBLE");					
				}
				continue;
			}
			double k2 = V*(X-x1)/(x2-x1);
			double k1 = V - k2;
			//cout << k2 * x1 + k1 * x2 << ' ' << V * X << endl;
			//cout << k1 << ' ' << k2 << endl;
			if (k1 < 0 || k2 < 0){
				puts("IMPOSSIBLE"); continue;
			}
			double t1 = k1 / v1;
			double t2 = k2 / v2;
			double rst = max(t1, t2);
			printf("%.9lf\n", rst);	
		}	
	}
	return 0;
}