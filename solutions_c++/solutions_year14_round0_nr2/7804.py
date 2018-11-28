#include <iostream>
#include <iomanip>
using namespace std;

int main() {
	int T;
	cin >> T;
	for(int i=1; i<=T; i++) {
		double C, F, X;
		cin >> C >> F >> X;
		double curmin = X / 2;
		double curtime = 0;
		double curadd = 2;
		while(curtime < curmin) {
			curtime += C / curadd;
			curadd += F;
			double tmp = curtime + X / curadd;
			if(tmp < curmin)
				curmin = tmp;
		}
		cout << "Case #" << i << ": " << fixed << setprecision(7) << curmin << endl;
	}
}
