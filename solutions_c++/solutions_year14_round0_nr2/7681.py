#include <iostream>
#include <fstream>

using namespace std;

int main() {
	int n;
	
	ifstream in("B--large.in");
	cin.rdbuf(in.rdbuf());
	ofstream out("result-large.out");
	cout.rdbuf(out.rdbuf());
	
	cin >> n;
	cout.setf(ios::fixed);
	cout.precision(7);
	for (int i = 0; i < n; i++) {
		double C, F, X;
		cin >> C >> F >> X;
		int t = 0;
		double time = 0.0;
		double m = 2.0;
		double mintime = X / m;
		while (1) {
			double tmp = time + X / m;
			if (mintime < tmp) {
				break;
			} else {
				mintime = tmp;
			}
			t++;
			time += C / m;
			m += F;
		}
		cout << "Case #" << i + 1 << ": " << mintime << endl;
	}
}
