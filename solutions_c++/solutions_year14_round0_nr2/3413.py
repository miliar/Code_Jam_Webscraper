#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main(){
	int T, n;
	double x, c, f, result, speed;

	cin >> T;

	for (int i1 = 0; i1 < T; i1++){
		cin >> c >> f >> x;
		result = 0;
		speed = 2;
		n = floor((x*f/c - f - 2.0)/f);

		for (int i = 0; i <= n; i++){
			result += c/(2 + i * f);
			speed += f;
		}
		result += x/speed;

		cout << "Case #" << i1+1 << ": " << fixed << setprecision(7) << result << endl;
	}
	return 0;
}