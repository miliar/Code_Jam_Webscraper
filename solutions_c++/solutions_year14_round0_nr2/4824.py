#include <stdio.h>
#include <iostream>
using namespace std;

double ReturnTime(int totalFarm, double a, double b, double c){
	int farmN = 0;
	double farmTime = 0;
	double totalTime = 0;
	
	while(farmN < totalFarm){
		farmTime = farmTime + (a / (2 + farmN * b));
		farmN++;
	}
	totalTime = farmTime + (c / (2 + farmN * b));
	return totalTime;
}

int main() {
	int n;
	cin >> n;
	for(int i = 0; i < n; i++){
		double a, b, c, totalTime = 0, bestTime = 0;
		
		scanf("%lf %lf %lf", &a, &b, &c);
		
		totalTime = ReturnTime(0, a, b, c);
		bestTime = totalTime;
		
		int j = 1;
		while(totalTime <= bestTime){
			totalTime = ReturnTime(j, a, b, c);
			j++;
			if(totalTime < bestTime){
				bestTime = totalTime;
			}
		}
		
		printf("Case #%d: %.7lf \n", i+1, bestTime);
	}
	return 0;
}