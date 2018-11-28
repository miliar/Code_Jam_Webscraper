#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>

using namespace std;

string solve(double C, double F, double X) {
	double answer = 0.0;
	double rate = 2.0;
	ostringstream ss;
	ss << fixed;
	ss.precision(7);

	//Solution start
	double time_without_purchase, time_with_purchase;
	while(true) {
		time_without_purchase = X/rate;
		time_with_purchase = C/rate + X/(F + rate);
		if(time_with_purchase < time_without_purchase) {
			answer += C/rate;
			rate += F;
		} else {
			break;
		}
	}
	answer += time_without_purchase;
	//Solution end

	ss << answer;
	return ss.str();
}

int main(void) 
{
	int TC;
	cin >> TC;
	for(int tc = 0; tc < TC; tc++) {
		double C, F, X;
		cin >> C >> F >> X;
		cout << "Case #" << (tc + 1) << ": " << solve(C, F, X) << endl;
	}
	return 0;
}
