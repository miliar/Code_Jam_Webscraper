#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>


using namespace std;


int main() {
	int T; int counter = 1;
	double C; double F; double X; int cookieCount = 0; double answer;
	cin >> T;

	while (counter != T+1) {
		/*X - (2+F*y)*sec = 0; 
		x/(2+f*y) + c/(2+F*(y-1)) + c/(2+F*(y-2)) ... c/(2+f*(y-y)) = ??? */
		cin >> C >> F >> X;
		answer = X/2;
		while (1) {
			if (answer - X/(2+F*cookieCount) + C/(2+F*cookieCount) + X/(2+F*(cookieCount+1)) <= answer)
				answer = answer - X/(2+F*cookieCount) + C/(2+F*cookieCount) + X/(2+F*(cookieCount+1));
			else if (answer - X/(2+F*cookieCount) + C/(2+F*cookieCount) + X/(2+F*(cookieCount+1)) > answer) {
				cout.setf(ios::fixed);
				cout << "Case #" << counter << ": " << setprecision(7) << answer << endl;
				break;
			}
			cookieCount++;
		}
		cookieCount = 0;
		counter++;
	}
	return 0;
}