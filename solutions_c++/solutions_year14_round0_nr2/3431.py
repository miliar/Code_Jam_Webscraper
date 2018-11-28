#include<iostream>
#include <iomanip>
#include<stdio.h>
using namespace std;

int main() {
	int t;
	double c,f,x;
	cin >> t;
	int i;

	for (int i = 0 ;i < t; i++) {
		double totalTime = 0;
		cin >> c >> f >> x;
		double rate = 2;
		double currentTime = x/2;
		double cookieFarmTime = c/2 + x/(f+rate);
		while (currentTime > cookieFarmTime) {
			totalTime += c/rate;
			rate += f;
			currentTime = x/rate;
			cookieFarmTime = c/rate + x/(f+rate);
		}	
		totalTime += currentTime;
		cout << "Case #" << (i+1) << ": ";

		printf("%0.7lf\n",totalTime);
		}

	
	return 0;
}
