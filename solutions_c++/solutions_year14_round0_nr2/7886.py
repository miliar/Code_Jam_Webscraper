#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<cstring>
#include<vector>
using namespace std;
double getMinTime(double curr_speed, double c, double f, double x) {
	double wait_time = 0, end_time = (x / curr_speed);
	double this_comp_time = 0.0;
	double next_comp_time = wait_time + end_time;
	do {

		double tmp = this_comp_time;
		this_comp_time = next_comp_time;
		next_comp_time = tmp;

		wait_time += (c / curr_speed);
		end_time = (x / (curr_speed + f));
		next_comp_time = wait_time + end_time;
		curr_speed += f;

	} while (next_comp_time < this_comp_time);
	return this_comp_time;
}
int main() {
	int t;
	scanf("%d", &t);
	for (int kase = 1; kase <= t; kase++) {
		double c, f, x;
		scanf("%lf %lf %lf", &c, &f, &x);
		printf("Case #%d: %0.7lf\n", kase, getMinTime(2.0, c, f, x));
	}
	return 0;
}
