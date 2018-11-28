#include <stdio.h>

void solve(){
	double c, f, x;
	double rate=2.0, time=0.0;
	scanf("%lf %lf %lf", &c, &f, &x);

	while(true){
		time += c/rate;
		if(x/(rate+f) < (x-c)/rate)
			rate += f;
		else {
			time += (x-c)/rate;
			break;
		}
	}

	printf("%.7lf", time);
}

int main(int argc, char *argv[]){
	int i, t;
	scanf("%d", &t);
	for(i=0;i<t;i++){
		printf("Case #%d: ", i+1);
		solve();
		printf("\n");
	}
	return 0;
}
