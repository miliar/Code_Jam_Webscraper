#include<cstdio>
#include<algorithm>
using namespace std;

int T, n;
double V, X, R[111], C[111];

bool chk(double t) {
	double rem = V, lo = 0,hi=0;
	for(int i = 0;i<n && rem > 1e-10;i++){
		double v= min(rem, t * R[i]);
		rem -= v;
		lo += v * C[i];
	}
	rem = V;
	for(int i=n-1;i>=0&&rem>1e-10;i--){
		double v= min(rem, t * R[i]);
		rem -= v;
		hi += v * C[i];
	}
	double tar = V * X;
	return (tar > lo && tar < hi);
}

int main() {
	scanf("%d", &T);
	for(int _=1; _<=T; _++) {
		printf("Case #%d: ", _);
		scanf("%d%lf%lf", &n, &V, &X);
		double mi = 10000.0;
		double s = 0.0;
		double lot = 111.0, hit = -1.0;
		for(int i=0;i<n;i++) {
			scanf("%lf%lf", &R[i], &C[i]);
			s += R[i];
			mi = min(mi, R[i]);
			lot = min(lot, C[i]);
			hit = max(hit, C[i]);
		}
		if(lot > X || hit < X) {
			printf("IMPOSSIBLE\n"); continue;
		}
		if(lot == X || hit == X) {
			double tot = 0;
			for(int i=0;i<n;i++)
				if(C[i] == X) tot+=R[i];
			printf("%.10lf\n", V / tot); continue;
		}
		
		for(int i=0;i<n;i++)
			for(int j=i+1;j<n;j++)
				if(C[i] > C[j]) {
					swap(R[i], R[j]);
					swap(C[i], C[j]);
				}
		
		double l = V / s, r = V / mi;
		bool ans = false;
		for(int i = 0; i < 137; i ++) {
			double mid = (l+r) / 2;
			if (chk(mid)) {
				r = mid;ans=true;
			}else l = mid;
		}
		//if (!ans) printf("IMPOSSIBLE\n");
		printf("%.10lf\n", l);
	}
	
	return 0;
}