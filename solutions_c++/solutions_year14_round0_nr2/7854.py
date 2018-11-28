#include <bits/stdc++.h>

using namespace std;

int main() {
	freopen("input.in", "rt", stdin);
	freopen( "output.txt" , "wt" , stdout );
	int t;
	double c, f, x;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cin >> c >> f >> x;
		double avg = 2, time = 0, minTime = 1e100;
		while (true) {
			double res = time + (x / avg);
			if (minTime > res)
				minTime = res;
			else
				break;
			time += (c / avg), avg += f;
		}
		cout << "Case #" << i << ": " << fixed << setprecision(7) << minTime
				<< endl;
	}
	return 0;
}
