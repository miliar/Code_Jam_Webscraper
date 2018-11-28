#include <stdio.h>
#include <vector>
using namespace std;

int main() {
	int t;
	scanf("%d", &t);
	double rate, farm, upgrade, end, answer, time, aux;
	
	for(int test=1; test<=t; test++) {
		rate = 2;
		scanf("%lf %lf %lf", &farm, &upgrade, &end);
		answer = end/rate;
		time = 0;
		
		do {
			time += farm/rate;
			rate += upgrade;
			aux = time+(end/rate);
			answer = min(answer, aux);
		} while(rate <= end*100);
		
		printf("Case #%d: %.7lf\n", test, answer);
	}
}
