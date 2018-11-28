#include <fstream>
using namespace std;

int t;
double c, f, x;

int main () {
	ifstream filein("bin.txt");
	ofstream fileout("bout.txt");

	filein >> t;
	for (int i = 1; i <= t; i ++) {
		filein >> c >> f >> x;

		double notBuyTime;
		double buyTime;
		double saveMoneyTime;
		double rate = 2;
		double time = 0;
		while (true) {
			notBuyTime = time + x / rate;

			saveMoneyTime = c / rate;
			buyTime = time + saveMoneyTime + x / (rate + f);

			if (notBuyTime < buyTime) {
				break;
			} else {
				rate = rate + f;
				time = time + saveMoneyTime;
			}
		}

		fileout.setf(ios::fixed);
		fileout.precision(7);
		fileout <<"Case #"<<i<< ": " << notBuyTime << endl;
	}
	return 0;
}
