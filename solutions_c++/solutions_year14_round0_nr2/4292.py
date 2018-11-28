#include <iostream>
#include <iomanip>
#include <cstdio>

using namespace std;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("outB_large.txt", "w", stdout);

	int T;

	cin >> T;
	double g = 20.0 / 3;
	
 	std::cout.precision(7);
	std::cout << std::fixed;

	for (int i = 0; i < T; i++) {

		double c, f, x;
	
		cin >> c >> f >> x;
	
		double t = 0.0;
		double k = 2.0;
	
		while (1) {
			double t1 = c / k + x / (k + f);
			double t2 = x / k;
	
			if (t2 < t1) {
				t += t2;
				break;
			} else {
				t += c / k;
				k += f;
			}
		}
		cout << "Case #" << i + 1 << ": " << t << endl;
	}
	
	return 0;
}
