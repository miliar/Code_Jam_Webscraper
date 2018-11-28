#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include <utility>
#include <vector>

using namespace std;

int main() 
{
	int T; cin >> T;
	for (int t = 1; t <= T; t++) {
		double C, F, X;
		cin >> C >> F >> X;
		double res = X / 2.0;
		double curTime = 0.0;
		double curRate = 2.0;
		// built
		for (int i = 1; i <= 100000; i++) {
			// build next one
			double needTime = C / curRate;
			curTime += needTime;
			curRate += F;
			// check
			res = min(res, curTime + (X / curRate));
			if (curTime > X / 2.0) break;
		}
		cout.precision(8);
		cout << std::fixed << "Case #" << t << ": " << res << endl;
	}
	return 0;
}