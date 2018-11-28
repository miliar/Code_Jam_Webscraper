#include<iostream>

using namespace std;

int main () {
	int test; cin >> test;
	for (int t = 0; t < test; t++) {
		double x, f, c;
		cin >> c >> f >> x;
		
		double speed = 2, count = 0, result = 0;
		while (1) {
			if (count >= x) {
				cout << "Case #" << t << ": " << result << endl;
				break;
			} else if (count < min(x, c)) {
				result += (min(x, c) - count) / speed;
				count = min(x, c);
			} else {
				if ((x - count) / speed <= (x - count + c) / (speed + f)) {
					result += (x - count) / speed;
					count = x;
				} else {
					count -= c;
					speed += f;
				}
			}
		}
	}
	return 0;
}