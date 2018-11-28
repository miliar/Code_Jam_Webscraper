#include <iostream>
#include <vector>
#include <math.h>
using namespace std;

bool isPal(int num) {
	int rev = 0, dig = 0, n = num;
	while (num > 0)
	{
	      dig = num % 10;
	      rev = rev * 10 + dig;
	      num = num / 10;
	}
	if (n == rev) return true;
	else return false;
}

int main() {
	int n;
	cin >> n;
	for (int i = 0; i < n; ++i) {
		int a, b;
		cin >> a >> b;
		int c = 0;
		for (int j = a; j <= b; ++j) {
			float dd = sqrt(j);
			int d = sqrt(j);
			if (isPal(j) && !fmod(dd, 1) && isPal(d)) ++c;
			//cout << "Num is: " << j << " " << isPal(j) << endl;
			//cout << "Sqr is: " << d << " " << isPal(d) << endl;
		}

		cout << "Case #" << i+1 << ": ";
		cout << c; 
		cout << endl;
	}
}