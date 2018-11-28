#include <bits/stdc++.h>
using namespace std;

#define fo(x,y,z) for(int x=y;x<z;x++)
#define A first
#define B second
#define eps 1e-6
typedef long long ll;
typedef pair<int, int> pp;

bool eq(double a, double b){
	return abs(a-b) < eps;
}

int tc, n;
double v, x, r[105], c[105];

int main(){
	scanf("%d", &tc);
	double a = 100.0000, b = 70.0263;
	fprintf(stderr, "%.10lf", a/b);
	fo(iz,1,tc+1){
		printf("Case #%d: ", iz);
		scanf("%d %lf %lf", &n, &v, &x);
		int done = 0, pos = 1;
		double ta = 1e10;
		fo(i,0,n){
			scanf("%lf %lf", &r[i], &c[i]);
			if(eq(c[i],x)){
				if(v/r[i] + eps < ta) ta = v/r[i];
				done++;
			}
		}
		if(n == 1){
			if(done) printf("%.10lf\n", ta);
			else printf("IMPOSSIBLE\n");
			continue;
		}
		else{
			if(done == 1){
				printf("%.10lf\n", ta);
				continue;
			}
			else if(done == 2){
				printf("%.10lf\n", v/(r[0]+r[1]));
				continue;
			}
			if(c[0] < x-eps && c[1] < x-eps) pos = 0;
			if(c[0] > x+eps && c[1] > x+eps) pos = 0;
			if(c[0] < x-eps){
				double tr = r[0], tcc = c[0];
				r[0] = r[1]; c[0] = c[1];
				r[1] = tr; c[1] = tcc;
			}
			if(!pos){
				printf("IMPOSSIBLE\n");
				continue;
			}

			double t = -1;
			double calc = v * (x - c[1]) / (c[0] - c[1]);
			t = max(t, calc/r[0]);
			t = max(t, (v-calc)/r[1]);
			printf("%.10lf\n", t);
		}
	}
	return 0;
}

