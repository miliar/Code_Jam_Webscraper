#include <iostream>
#include <algorithm>
#include <iomanip>

using namespace std;

int main() {
	int T;
	cin >> T;
	cout << setprecision(15);
	for(int count = 1; count <= T; count++) {
		double C, F, X;
		cin >> C >> F >> X;
		double time = X / 2.0;
		double p = 0.0;
		int n = 0;
		while(true) {
			p += C / (2.0 + n*F);
			double buy = p + X / (2.0 + ++n*F);
			if(buy < time) {
				time = buy;
			}
			else {
				cout << "Case #" << count << ": " << time << endl;
				break;
			}
		}
	}
}
