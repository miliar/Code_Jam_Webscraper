#include <iostream>
#include <cstdio>
using namespace std;

int main() {
	int ncase;
	double c, f, x;
	int num=0;
	cin >> ncase;
	while (ncase--) {
		scanf("%lf%lf%lf", &c, &f, &x);
		double ans=x/2;
		int g=f*x/c-3.0;
		g=max(0, g);
		g+=3;
		
		double time=0.0;
		double h=2.0, w=2.0+f, t=0.0;
		for (int i=0; i<g; i++) {
			t+=c/h;
			time=t+x/w;
			h=w;
			w+=f;
			if (time<ans) ans=time;
		}
		printf("Case #%d: %.7lf\n",++num,ans);
		
		printf("\n");
	}
	return 0;
}
