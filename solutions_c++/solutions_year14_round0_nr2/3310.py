#include <iostream>
#include <iomanip>
using namespace std;

int main() {
	int T;
	cin >> T;
	for(int c=1;c<=T;c++) {
		double C,F,X;
		cin >> C >> F >> X;
		cout << "Case #" << c << ": ";
		double total = X / 2, speed = 2.0;
		if(X <= C) {
			cout << fixed << setprecision(7) << total << endl;
		} else {
			double pre = 0;
			double temp;
			double newspeed;
			while(true) {
				temp = C / speed;
				newspeed = speed + F;
				//cout << X/newspeed + temp << " " << X / speed << endl;
				if(X/newspeed + temp < X/speed) {
					pre += temp;
					speed = newspeed;
				} else {
					pre += X / speed;
					break;
				}
			}
			cout << fixed << setprecision(7) << pre << endl;
		}
	}
	return 0;
}