#include <iostream>

int main() {
	FILE *fp = fopen("B-large.in","r");
	int T = 0;
	fscanf(fp, "%d", &T);

	for (int i=1;i<=T;i++) {
		printf("Case #%d: ",i);
		
		double C,F,X;
		fscanf(fp, "%lf %lf %lf", &C,&F,&X);

		//printf("%lf %lf %lf\n",C,F,X);

		double rate = 2;
		bool running = true;
		
		double tail=0,farm=0;
		tail = X/rate;
		farm = C/rate;
		while (running) {
			//int ttt = farm+X/(rate+F);
			if (tail>farm+X/(rate+F)) {
				tail = farm + X/(rate+F);
				rate += F;
				farm += C/rate; 
			} else {
				running =false;
			}
		}

		printf("%.7f",tail);
		if (i!=T)
			printf("\n");
	}
	
	return 0;
}