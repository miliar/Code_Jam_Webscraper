#include <algorithm>
#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

double calcTime(double costFarm, double farmProd, double goal) {
	if (goal < costFarm) {
		return goal / 2.0F;
	}
	double cookieP = 2.0F;
	double timeProd = (goal - costFarm) / cookieP;
	double timeToGoal = goal / (cookieP + farmProd);
	double currentTime = 0.0F;
	while(timeProd > timeToGoal) {
		//printf("(%lf, %lf, %lf), ", cookieP, timeProd, timeToGoal);
		currentTime += costFarm / cookieP;
		cookieP += farmProd;
		timeProd = (goal - costFarm) / cookieP;
		timeToGoal = goal / (cookieP + farmProd);
	}
	//printf("(%lf, %lf, %lf), ", cookieP, timeProd, timeToGoal);
	currentTime += goal / cookieP;
	return currentTime;
}

int main(void) {
	double C, F, X;
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++) {
		scanf("%lf%lf%lf", &C, &F, &X);
		printf("Case #%d: %.7lf\n", t, calcTime(C, F, X));
	}
	return 0;
}