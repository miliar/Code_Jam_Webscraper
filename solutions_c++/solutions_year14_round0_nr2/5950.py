#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <vector>
#include <set>

using namespace std;

int main(){
	freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);
	int t;
	scanf("%d", &t);
	for (int tt = 0; tt < t; tt++){
		double c, f, x;
		scanf("%lf %lf %lf", &c, &x, &f);
		double time = f / 2.;
		if (f <= c){
			printf("Case #%d: %llf\n", tt + 1, time);
			continue;
		}
		double newtime = f / 2.;
		double tmp = c / 2;
		double d = 2.;
		do{
			time = newtime;
			//double aaa = c / d;
			d += x;
			
			newtime = tmp +  f / d;
			tmp = tmp + c / d;

		} while (newtime < time);
		printf("Case #%d: %llf\n", tt + 1, time);
	}
}