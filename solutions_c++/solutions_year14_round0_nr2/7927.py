#include <iostream>
#include <iomanip>
using namespace std;

// C is cost, F is rate, X is target
void cookie(double cost, double farmRate, double target);
bool shouldBuy(double &cookiesLeft, double &rate, double cost, double farmRate, double &time);

int main() {
	int numCases;
	double C, F, X;
	cin >> numCases;
	cout << setprecision(7);
	cout << fixed;
	
	for (int i = 0; i < numCases; ++i) {
		cin >> C; cin >> F; cin >> X;
		cout << "Case #" << i + 1 << ": ";
		cookie(C, F, X);
	}
}

void cookie(double cost, double farmRate, double target) {
	double cookiesLeft = target;
	double rate = 2;
	double time = 0;
	while (shouldBuy(cookiesLeft, rate, cost, farmRate, time));
	cout << time << '\n';
}

bool shouldBuy(double &cookiesLeft, double &rate, double cost, double farmRate, double &time) {
	//cout << "\ncookies left: " << cookiesLeft << '\n';
	//cout << "rate: " << rate << '\n';
	//cout << "time: " << time << '\n';
	double time1, time2;
	time1 = cookiesLeft / rate;
	time2 = (cost / rate) + cookiesLeft / (rate + farmRate);
	if (time1 < time2) {
		time += time1;
		return false;
	} else {
		time += cost / rate;
		rate += farmRate;
		return true;
	}
}

