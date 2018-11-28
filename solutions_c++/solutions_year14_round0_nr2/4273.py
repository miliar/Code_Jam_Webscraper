#include<cstdio>
#define EPS 1e-19
int T;
double C, F, X, tmp, ans, SPD1, SPD2;
int main(){
	freopen("GCJ14_QR_Blarge.in","r",stdin);
	freopen("GCJ14_QR_Blarge.out","w", stdout);
	
	scanf("%d",&T);
	for (int t = 0; t < T; t++){
		scanf("%lf%lf%lf", &C, &F, &X);
		tmp = 0.0; ans = X/2;  SPD1 = 0.5, SPD2 = (double)2+F; 
		while (tmp < ans+EPS){
			if (tmp > EPS) ans = tmp;
			tmp = C*SPD1 + X/SPD2;
			SPD1 += 1/SPD2; SPD2 += F;
		}
		printf("Case #%d: %.10lf\n", t+1, ans);
	}
	scanf("\n");
	return 0;
}
