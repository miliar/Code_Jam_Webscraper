#include <iostream>

using namespace std;

int main() {
	int T, i;
	long long int r, a, f(0), o, g, c(0);
	cin >> T;
	for(i = 1; i <= T; i++) {
		c = 0;
		f = 0;
		cin >> r >> a;
		for(o = 0; o < a; o+=2) {
			g = f;
			f += ((r+o+1)*(r+o+1)-(r+o)*(r+o));
			if(f > a) {
				f -= g;
				break;
			} else c++;
		}
		cout << "Case #" << i << ": " << c << endl;
	}
	return 0;
}