#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main () {

	int iter = 0, count = 0;
	cin >> iter;
	while (count < iter) {
		double c = 500;
		double n = 0;
		double f = 4;
		double x = 2000;

		cin >> c;
		cin >> f;
		cin >> x;
		double oldtime = -1;
		bool stop = false;
		do  {
			double time = 0;
			double cookierate = 2;
			int cookies = 0;
			for (int i = 0; i < n ; i++) {
				time = time + c /(cookierate);
				cookierate += f;
			}
			time = time + x / cookierate;
			if (oldtime == -1) {
				oldtime = time;
				continue;
			}
			if (time < oldtime) {
				oldtime = time;
				stop = false;
			} else if (oldtime >= 0 &&  time > oldtime) {
				stop = true;
			}
			n++;
		} while (!stop);
		std::setprecision(9);
		cout.setf(ios::showpoint);
		cout << fixed;
		cout << "Case #" << count + 1 << ": " ;
		cout << fixed;
		cout << oldtime << endl;
		count++;
	}
	
	return 1;
}
