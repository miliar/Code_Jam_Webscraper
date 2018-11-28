#include <iostream>
#include <iomanip>
using namespace std;

int main() {
	int caseNum;

	cin >> caseNum;
	for (int i=1; i<=caseNum; i++) {
		double c, f, x;
		double minSec = -1;
		double buyFarmSec = 0;
		double cookiePerSec = 2;

		cin >> c >> f >> x;
		while (true) {
			double sec = buyFarmSec + x / cookiePerSec;

			if (minSec == -1 || sec < minSec)
				minSec = sec;
			else
				break;
			buyFarmSec += c / cookiePerSec;
			cookiePerSec += f;
		}
		cout << "Case #" << i << ": ";
		cout << setprecision(7) << fixed << minSec << endl;
	}

	return 0;
}
