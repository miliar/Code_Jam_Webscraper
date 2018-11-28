
#define _CRT_SECURE_NO_WARNINGS


//source here
#include <iostream>
#include <string>
#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
	//freopen("B-large.in", "r", stdin);
	//freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int Case = 0; Case < T; Case++)
	{
		double C, F, X;
		scanf("%lf%lf%lf", &C, &F, &X);
		double speed = 2;
		double time = 0;
		while (X / (speed + F)<(X - C) / speed&&X>C){
			time += C / speed;
			speed += F;
		}
		time += X / speed;
		printf("Case #%d: %.7f\n",Case+1, time);
	
	}
	return 0;
}