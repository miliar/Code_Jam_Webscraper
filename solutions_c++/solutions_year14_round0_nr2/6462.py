// Cookie.cpp: определяет точку входа для консольного приложения.
//

#include <iostream>
using namespace std;
#include <stdio.h>
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T; int i;
	double C, F, X;
	cin >> T;
	
	for (i = 0; i < T; i++) {
		cin >> C >> F >> X;
		double speed = 2.0;
		double COOKIE = 0.0;
		double time = 0.0;
		while (1) {
			if (X / speed <= (C / speed) + (X / (speed + F))) {
				time += X / speed;
				break;
			}
			else {
				time += C / speed;
				COOKIE += time*speed;
				if (COOKIE >= C) {
					COOKIE -= C;
					speed += F;
				}
			}
		}
		printf("Case #%d: %.7f\n", i+1, time);
	}
	return 0;
}

