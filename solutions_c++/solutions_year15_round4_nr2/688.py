#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int MAXN = 105;
const double EPS = 1e-6;

double A[MAXN], B[MAXN];
double V, R;
int T, N;

inline bool equ(double x, double y){
	double v = x - y;
	if(v < 0) v = -v;
	if(v <= EPS) return true;
	else return false;
}

int main(){
	scanf("%d", &T);
	for(int xx = 1; xx <= T; ++xx){
		scanf("%d%lf%lf", &N, &V, &R);
		for(int i = 0; i < N; ++i)
			scanf("%lf%lf", &A[i], &B[i]);
		printf("Case #%d: ", xx);
		if(N == 1){
			if(equ(R, B[0])) printf("%.10lf\n", V / A[0]);
			else puts("IMPOSSIBLE");
		} else {
			if(equ(B[0], R) || equ(B[1], R)){
				if(equ(B[0], R) && equ(B[1], R)){
					printf("%.10lf\n", V / (A[0] + A[1]));
				} else {
					if(equ(B[0], R))
						printf("%.10lf\n", V / A[0]);
					else
						printf("%.10lf\n", V / A[1]);
				}
			} else{
				double f1 = B[0] - R;
				double f2 = R - B[1];
				double f3 = f2 / f1;
				double v1 = V / (f3 + 1);
				double v0 = V - v1;
				//printf("v0=%.10lf, v1=%.10lf\n", v0, v1);
				if(v0 < 0 || v1 < 0) 
					puts("IMPOSSIBLE");
				else
					printf("%.10lf\n", max(v0 / A[0], v1 / A[1]));
			}
		}
	}
}
