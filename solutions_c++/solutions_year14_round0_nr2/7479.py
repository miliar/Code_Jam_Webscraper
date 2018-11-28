#include <iostream>
using namespace std;

double GetTime(double time, const double price_of_factory, double rate,
			const double inc_rate, double target, double time_to_next_factory, double eta,
			double last_eta) {
				if (time + eta > last_eta)
					return last_eta;
				return GetTime(time+time_to_next_factory, price_of_factory, rate + inc_rate, inc_rate,
				target, price_of_factory/(rate + inc_rate), target/(rate + inc_rate), time + eta);
			}

int main() {
freopen("output.txt","w",stdout);
freopen("input.txt","r",stdin);
	int testcases;
	cin>>testcases;
	double price, rate, target;
	for (int i=0; i<testcases; i++) {
		cin>>price;
		cin>>rate;
		cin>>target;
		printf("Case #%d: %.7f\n", i+1, GetTime(0, price, 2, rate, target,
									price/2, target/2, target/2));
	}
	return 0;
}
