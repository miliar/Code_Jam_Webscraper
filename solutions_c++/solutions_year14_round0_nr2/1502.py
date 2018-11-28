#include<cstdio>

double C, F, X;

double tenta(int f, double g) {
	if(f ==0)
		return X/g;
	return C/g + tenta(f-1, g + F); 
}



int main(){
	int t;
	scanf("%d", &t);
	for(int c = 1; c<=t; c++) {
		scanf("%lf %lf %lf", &C, &F, &X);
		int l=0, r= 50000;
		while(r-l < 20) {
			int m1 = (2*l + r)/3;
			int m2 = (l + 2*r)/3;
			double g1 = tenta(m1, 2.0);
			double g2 = tenta(m2, 2.0);
			printf("%d %.7f %d %.7f\n",m1,g1,m2,g2);
			if(g1< g2)
				r = m2;
			else l=m1;
		}
		double ret;
		for(int i=l;i<r; i++) {
			double r = tenta(i, 2.0);
			if (i && r > ret) break; 			
			ret = r;
		}
		printf("Case #%d: %.7f\n", c, ret); 
	}
	return 0;
}
