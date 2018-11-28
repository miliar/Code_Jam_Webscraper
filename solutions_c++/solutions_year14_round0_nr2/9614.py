#include <iostream>
#include <iomanip>

using namespace std;

double solve(double C, double F, double X, double rate)
{
	double best = X/rate;
	double time = 0, total_time = 0;
	int can_improve = true;

	for(;;) {
		time += C/rate;
		rate += F;
		total_time = time + X/rate;
		if (total_time - best >= 0.00000001)
			break;
		else
			best = total_time;
	}
	return best;
}

int main(void)
{
	int T, i;
	double C, F, X, rate = 2.0;
	
	cin >> T;
	for (i = 0; i < T; i++) {
		cin  >> C >> F >> X;
		
		cout <<"Case #"<<i+1<<": "<<std::fixed<<std::setprecision(7)<<solve(C, F, X, rate)<<endl;
	}

	return 0;
}
