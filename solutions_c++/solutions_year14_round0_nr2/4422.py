#include <cstdio>
using namespace std;

int main(){
	freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

	int t,cases;
	double c,f,x,prod,t1,t2,t3,tot;

	scanf("%d", &t);
	cases = t;
	while(t--){
		scanf("%lf %lf %lf", &c,&f,&x);
		prod = 2;
		tot = t1 = t2 = t3 = 0;
		while( true ) {
			t1 = x / prod;
			t2 = c / prod;
			t3 = x / (prod + f);
			if ( t2 + t3 < t1){		// Buy farm
				prod += f;
				tot += t2;
				//printf("t1: %.7lf - t2: %.7lf - t3: %.7lf - prod: %.7lf - tot: %.7lf\n", t1,t2,t3,prod,tot);
			}
			else {					// Don't buy
				tot += t1;
				//printf("t1: %.7lf - t2: %.7lf - t3: %.7lf - prod: %.7lf - tot: %.7lf\n", t1,t2,t3,prod,tot);
				break;
			}
		}
		printf("Case #%d: %.7lf\n", cases-t,tot);
	}
}