#include <iostream>
#include <vector>

using namespace std;

int main() {
	int t; cin >> t;
	for (int o = 1; o <= t; o++) {
		double c, f, x; cin >> c >> f >> x;
		
		double time = 0.0, a = 0.0, b=0.0;
		double currentSpeed = 2.0;

		while (1) {
			a = x/currentSpeed;
			b = c/currentSpeed + x/(currentSpeed+f); 
			if (a <= b) {
				time += a;
				cout << "Case #" << o << ": ";
				printf("%.7f\n", time);  
				break;
				
			} else {
				time += c/currentSpeed;
				currentSpeed += f;
			}
				
		}
	}

}
