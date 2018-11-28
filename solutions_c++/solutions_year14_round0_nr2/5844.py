#include <cstdio>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int T; 
double C, F, X;


double calc(double rate, double time) {
	return X / rate + time;
}

void do_case(int num)
{

	cin >> C;
	cin >> F;
	cin >> X;

	double rate = 2.0f;
	double cookies = 0.0f;
	double time = 0.0f;

	double t = calc(rate, time);
	double t2 = calc(rate + F, C / rate);
	while (t2 < t) 
	{
		t = t2;
		time += C / rate;
		rate += F;

		t2 = calc(rate + F, time + C / rate);
	}

	printf("Case #%d: %.7llf\n", num + 1, t);
}

int main()
{
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
		do_case(i);
	}

	return 0;
}