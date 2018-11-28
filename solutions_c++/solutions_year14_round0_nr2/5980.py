#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
//#include <ctime>
#include <map>
using namespace std;

void solve() {
	double C;
	double F;
	double X;

	cin >> C;
	cin >> F;
	cin >> X;

	double curr = 0;
	double extra = 0;
	double time = 0.0;
	if (X <= C) {
		cout << X/2.0 << endl;
		return;
	}
	time = C/2.0;
	curr = C;
	while (true) {
		if ((X-curr) / (2+extra) < X / (2+extra+F)) {
			time += (X-curr) / (2+extra);
			cout << time << endl;
			break;
		} else {
			extra += F;
			time += C/(2+extra);
		}
	}

}

int MAIN() {
	int numTestCases;
	cin >> numTestCases;
	for (int i = 1; i <= numTestCases; i++) {
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	cout << fixed << setprecision(7);
	return MAIN();
}



