#include <iostream>
#include <iomanip> 
using namespace std;


int T, t = 1;
double C, F, X;

struct Cookieverse {
	double time;
	double cps;
	int farms;
	Cookieverse() : time(0), cps(2), farms(0) {

	}
	void calculate () {
		this->time += X/this->cps;
	}
	void get_farm () {
		this->time += C/this->cps;
		++this->farms;
		this->cps += F;
	}
};

int main () {

	/*
		2 cookies per second,
		C: farm cost,
		F: farm production,
		X: cookie goal
	*/

	
	cout << std::fixed << std::setprecision(7);

	cin >> T;

	while (t <= T) {

		cin >> C >> F >> X;

		double best_time;
		double last_time = 0;

		Cookieverse current;
		Cookieverse branch = current;

		current.calculate();
		best_time = current.time;

		while (last_time == 0 || last_time == best_time) {

			current = branch;
			current.get_farm();
			branch = current;

			current.calculate();
			last_time = current.time;
			if (last_time < best_time) best_time = last_time;

		}

		cout << "Case #" << t << ": " << best_time << endl;

		++t;

	}
}