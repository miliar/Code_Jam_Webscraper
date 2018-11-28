#include <iostream>
#include <iomanip>
#include <cstdio>
using namespace std;
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test;
	cin >> test;
	for (int t = 1; t <= test; ++t) {
		double c, f, x;
		double time = 1111111111;
		cin >> c >> f >> x;
		for (int n = 0; n < 10000; ++n) {
			double sum = 0;
			for (int i = 0; i < n; ++i)
				sum += c / (2 + i * f);
			sum += x / (2 + n * f);
			time = min(time, sum);
		}	 
		cout << "Case #" << t << ": ";
		cout << setprecision(20) <<  fixed << time << endl;
	}
	return 0;
}