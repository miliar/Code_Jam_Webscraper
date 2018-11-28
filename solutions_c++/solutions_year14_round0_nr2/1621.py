#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#define MAX 101000

using namespace std;

int main(){
	int T, t;
	scanf("%d", &T);
	for(t = 1; t <= T; t++){
		double C, F, X;
		scanf("%lf%lf%lf", &C, &F, &X);
		double resp = X / 2.0;
		double tim = 0.0;
		for(int i = 0; i < 2*X; i++){
			double tmp = X / (i*F + 2.0);
			if(tim + tmp < resp)
				resp = tim + tmp;
			tim += C / (i*F + 2.0);
		}
		printf("Case #%d: %.7f\n", t, resp);
	}
	return 0;
}
