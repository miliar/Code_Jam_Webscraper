#include <cstdio>
using namespace std;

int main() {
	double C, F, X, n;
	double sumatoria, anterior, tiempo;
	int T;
	scanf("%d", &T);
	for(int idx = 1; idx <= T; idx++){
		scanf("%lf %lf %lf", &C, &F, &X);
		sumatoria = 0;
		anterior = X / 2;
		for(int i = 1; ; i++ ){
			sumatoria += C / (2+(i-1)*F);
			tiempo = sumatoria + X/(2+i*F);
			//printf("%.7f %.7f %.7f\n", sumatoria, (X/(2+i*F)), anterior);
			if(tiempo - anterior > 0.0000001)
				break;
			anterior = tiempo;
		}
		printf("Case #%d: %.7f\n", idx, anterior);
	}
	return 0;
}