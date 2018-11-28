#include <algorithm>
#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
	int t = 0;
	cin >> t;
	for (int cur = 0; cur < t; cur++) {
		double c,f,x;
		cin >> c >> f >> x;

		double sum = 0;
		double last = x/2;
		for (int i = 0; ; i++) {
			sum += c / (2+i*f);
			double time = sum + x/(2+(i+1)*f);
			if (time > last) {
				break;
			}
			last = time;
		}
		cout << "Case #" << cur + 1 << ": " << fixed << std::setprecision(7) << last << endl;
	}
	return 0;
}
