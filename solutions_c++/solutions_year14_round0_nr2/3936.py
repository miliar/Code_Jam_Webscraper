#include <iostream>
#include <iomanip>

using namespace std;

int main() {
	int t;
	cin >> t;

	double b = 2.0;

	for (int i = 0; i < t; i++) {
		double c, f, x;
		double result;
		cin >> c >> f >> x;
		double time = 0; 
		double g = b;
		double y = 0;
		
		time = c / g + x / (g + f);
		if (x / g < time) {
			result = x / g;
		} else {
			double min = x / g;
			while (min > time) {
				min = time;
				g += f;
				time += c / g - x / g + x / (g + f);
			}
			result = min;
		}
		
		cout << "Case #" << i+1 << ": ";
		cout.setf(ios::fixed, ios::floatfield);
		cout.precision(7);
		cout << result << endl;
	
	}

	return 0; 
}