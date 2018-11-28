#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

double C,F,X,cookies_second,time_min,farms;
int c;

void calculate_time(double time) {
	double time1;

	c++;
	time = time + (C / cookies_second);
	time1 = ((X - C)/cookies_second) + time;
	if (time1 < time_min) {
		time_min =  time1;
	}
	if (time < time_min && c<130838) {
		farms++;
		cookies_second = 2 + F*farms;
		calculate_time(time);
	}
}		

int main() {
	int cases;
	double time;

	cin >> cases;
	cin.ignore();
	for (int i=0; i<cases; i++) {
		c=0;
		cin >> C;
		cin >> F;
		cin >> X;
		cookies_second = 2;
		farms = 0;
		time = 0;
		time_min = X/2;
		calculate_time(time);

		// Out
		cout << "Case #" << i+1 << ": ";
		printf("%.7f",time_min);
		cout << endl;
	}
	return 0;
}

