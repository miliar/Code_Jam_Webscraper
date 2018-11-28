#include <cstdio>
#include <cstring>
int main()
{
	//freopen("PB.txt", "r", stdin);
	
	freopen("B-large.in", "r", stdin);
	freopen("PB.out", "w", stdout);
	double C, F, X, r, n, t;
	int ca=1, TN;
	scanf("%d", &TN);
	while(TN--){
		scanf("%lf%lf%lf", &C, &F, &X);
		n=0;
		t=0;
		r=2;
		while(n<X){
			if(n>=C){
				if((X-n+C)/(r+F)<(X-n)/r){
					n-=C;
					r+=F;
				}
			}
			if(n+C<X){
				n+=C;
				t+=C/r;
			}
			else{
				t+=(X-n)/r;
				n=X;
			}

		}
		printf("Case #%d: %.7lf\n", ca++, t);
	}
	return 0;
}