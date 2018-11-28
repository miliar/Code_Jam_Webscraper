#include<stdio.h>
#include<vector>
#include<cmath>
#include<memory.h>
#include<algorithm>
#define ep 0e-3
using namespace std;
int N;
double V,X, r[110], c[110], n1[110],n2[110];
bool equ(double a, double b){
	double c = a-b;
	if(-0.00000001 < c && c < 0.00000001)
		return true;
	return false;
}
int main()
{
	freopen("B-small-attempt4.in","r",stdin);
	freopen("B-output.txt","w",stdout);
	int T;
	scanf("%d", &T);
	for(int tc = 1; tc <= T; tc++){
		memset(r,0,sizeof(r));
		memset(c,0,sizeof(c));
		memset(n1,0,sizeof(n1));
		memset(n2,0,sizeof(n2));
		printf("Case #%d: ", tc);
		scanf("%d%lf%lf", &N,&V,&X);
		for(int i = 0; i < N; i++){
			scanf("%lf%lf", &r[i], &c[i]);
		}
		if(N == 1){
			if(equ(c[0], X))
				printf("%.8lf\n", V/r[0]);
			else
				printf("IMPOSSIBLE\n");
			continue;
		}
		if((X-c[0])*(X-c[1])>0){
			printf("IMPOSSIBLE\n");
			continue;
		}
		for(int i = 0; i < N; i++){
			n2[i] = r[i];
		}
		for(int i = 0; i < N; i++){
			if(equ(c[i],X)) n1[i] = 0;
			else n1[i] = r[i] - r[i]*c[i]/X;
		}
		if(equ(n1[0], 0) && equ(n1[1],0)){
			double l = 0, r = 10000000, m;
			for(int i = 1; i <= 100; i++){
				m = (l+r)/2;
				if((n2[0]+n2[1]) * m > V) r=m;
				else l=m;
			}
			printf("%.8lf\n", l);
			continue;
		}
		double x1 = -n1[1]*V/(n1[0]*n2[1]-n1[1]*n2[0]);
		double x2 = n1[0]*V/(n1[0]*n2[1]-n1[1]*n2[0]);
		if(min(x1,x2) < 0)
			printf("IMPOSSIBLE\n");
		else
			printf("%.8lf\n", max(x1,x2));
	}

	return 0;
}

