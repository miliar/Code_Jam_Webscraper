#include<cstdio>
using namespace std;

int main(){
	int maxtcnt;
	scanf("%d", &maxtcnt);
	for(int tcnt = 1; tcnt <= maxtcnt; tcnt++){
		double C, F, X; // C : cost, F : rate, X : target
		scanf("%lf %lf %lf", &C, &F, &X);
		
		double mintime = X / 2.0;
		double beftime = mintime;
		double farmgentime = 0;
		int farmcnt = 1;

		while(true){
			// assume that we use farmcnt!
			double newfarmgentime = farmgentime + C / (2 + (farmcnt - 1) * F);
			double lasttime = X / (2 + farmcnt * F);

			double newtime = lasttime + newfarmgentime;
			if(newtime > beftime) break;
			if(newtime < mintime)
				mintime = newtime;
			
			farmgentime = newfarmgentime;
			beftime = newtime;
			farmcnt++;
		}
		printf("Case #%d: %.8lf\n", tcnt, mintime);
	}
	return 0;
}
