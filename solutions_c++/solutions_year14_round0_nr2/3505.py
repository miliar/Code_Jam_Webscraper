#include <iostream>
#include <iomanip>
using namespace std;

int main() {
	int total;
	cin >> total;
	for (int i = 0; i < total; i++) {
		double c,f,x;
		cin >> c >> f >> x;
		double rate = 2;
		bool done = false;
		double totalTime = 0;
		while (!done) {
			double dur = x/rate;
			double nextDur = (c/rate) + (x/(rate+f));
			if (dur > nextDur) {
				totalTime+=c/rate;
				rate+=f;
			} else {
				totalTime+=x/(rate);
				std::cout << std::fixed << "Case #" << i+1 << ": " << std::setprecision(7) << totalTime << std::endl;
				done = true;
			}
		}
	}
	return 0;
}