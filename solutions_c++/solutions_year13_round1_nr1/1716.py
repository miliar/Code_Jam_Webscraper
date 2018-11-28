#include <iostream>
#include <cstdio>
#include <cstdlib>


void alg() {
	int radius, limitMilli; 
	int totalMilli = 0;
	int cycleCount = 0;
	int oneMilli;

	scanf("%d %d", &radius, &limitMilli);
	int startRadius = radius + 1;
	while(1) {
		oneMilli = (startRadius * startRadius) - (startRadius-1)*(startRadius-1);
		//printf("outter %d\n", startRadius * startRadius);
		//printf("inner %d\n", (startRadius-1) * (startRadius-1));
		totalMilli += oneMilli;
		//printf("space %d\n", oneMilli);
		if (totalMilli > limitMilli) {
			break;
		}
		cycleCount += 1;
		startRadius += 2;
	}
	static int case_no = 0;
	printf("Case #%d: %d\n", ++case_no, cycleCount);
}

using namespace std;

int main() {
	int d;
	scanf("%d", &d);
	while (d--) {
		alg();
	}
}
