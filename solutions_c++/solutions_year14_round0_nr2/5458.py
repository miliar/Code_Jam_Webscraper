# include <string>
# include <fstream>
# include <algorithm>
# include <vector>
using namespace std;




int main() {
	ifstream cin("input.txt");
	ofstream cout("output.txt");

	int tests;
	cin >> tests;

	for (int test = 1; test <= tests; test++) {
		double c, f, x;
		cin >> c >> f >> x;
		
		double ans = x / 2.0;
		double eps = 1e-9;
		double cookiesPerSecond = 2;
		double elapsed = 0;
		while (c / cookiesPerSecond + (x / (cookiesPerSecond + f)) <= x / (cookiesPerSecond)) {
			double needTime = c / cookiesPerSecond;
			ans = min(ans, elapsed + needTime + (x / (cookiesPerSecond + f)));
			cookiesPerSecond += f;
			elapsed += needTime;
		}

		cout.precision(7);
		cout << "Case #" << test << ": " << fixed << ans << endl;
	}


	return 0;
}