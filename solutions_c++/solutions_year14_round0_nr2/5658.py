#include<iostream>
#include<fstream>
#include<cstdio>
using namespace std;
double solve(double C, double F, double X) {
	double time = 0;
	double now = 2.0;
	while (X/now > X/(now+F)+C/now) {
		time += C / now;
		now = now + F;
	}
	time += X / now;
	return time;
}
int main()
{
	//ifstream cin("C:\\Users\\swcandy\\Downloads\\B-large.in");
	//freopen("C:\\Users\\swcandy\\Downloads\\B-large.out","w",stdout);
	int t;
	double C,F,X;
	cin >> t;
	for (int T = 1; T <= t; T++) {
		cin >> C >> F >> X;
		printf("Case #%d: %.7lf\n",T,solve(C,F,X));
	}
	return 0;
}
		