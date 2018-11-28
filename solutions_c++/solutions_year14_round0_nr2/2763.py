#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <iomanip>

using namespace std;

double c, f, x;

double solve() {
	double speed = 2;

	double last_buy = 0;
	double last_win = x / 2;
	
	while (true) {
		double now_buy = last_buy + (c / speed);
		speed += f;
		double now_win = x / speed;
		//cout << "now " << now_buy << ' ' << now_win << endl;
		
		if (last_buy + last_win < now_buy + now_win) {
			//cout << "last was better" << endl;
			return last_buy + last_win;
		}
		//cout << "still better" << endl;
		last_buy = now_buy;
		last_win = now_win;
	}

	return x / 2;
}

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		cin >> c >> f >> x;
		
		cout << "Case #" << i+1 << ": " << fixed << setprecision(7) << solve() << endl;
	}
	return 0;
}
