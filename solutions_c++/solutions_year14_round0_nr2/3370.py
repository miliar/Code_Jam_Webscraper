#include <cstdio>
#include <cstring>

double c, f, x, mini;

/*void sol(double tac, double fac) {
	if(tac > mini) return;
	double toend = tac + (x / fac);
	if(toend < mini) {
		mini = toend;
	}
	sol(tac + (c / fac), fac + f);
}*/

void sol2() {
	double tac = 0.0, fac = 2.0;
	double toend;
	while(tac < mini) {
		toend = tac + (x / fac);
		if(toend < mini) {
			mini = toend;
		}
		tac += (c / fac);
		fac += f;
	}
}

int main() {
	int t, tc;
	
	scanf("%d",&tc);
	for(t=1;t<=tc;t++) {
		scanf("%lf %lf %lf",&c,&f,&x);
		mini = x / 2.0;
		//sol(0.0, 2.0);
		sol2();
		printf("Case #%d: %.7lf\n",t,mini);
	}
	return 0;	
}
