#include<iostream>
using namespace std;

typedef long double ld;

const ld eps = 1e-10;

int sgn(ld a){
	if (a<-eps) return -1;
	return a>eps;
}

int n;
ld V, X, r[10], c[10];

int main(){
	ios::sync_with_stdio(0); cin.tie(0);
	int tt;
	cin >> tt;
	for (int _tt=0 ; _tt < tt ; _tt++){
		int B = 0;
		ld J = 0;
		cin >> n >> V >> X;
		r[0] = r[1] = 0;
		for (int i=0 ; i<n ; i++)
			cin >> r[i] >> c[i];
		if (n>2 || n==1 || c[0] == c[1]){
			if (sgn(c[0]-X))
				B = 1;
			else
				J = V/(r[0]+r[1]);
		}else{
			ld a = (X*V - c[1]*V) / (c[0]-c[1]);
			ld b = V - a;
			if (a<-eps || b<-eps) B = 1;
			J = max(a/r[0], b/r[1]);
		}
		printf("Case #%d: ",_tt+1);
		if (B) printf("IMPOSSIBLE\n");
		else printf("%.10lf\n", (double)J);
	}
}
