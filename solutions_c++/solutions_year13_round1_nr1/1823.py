#include <iostream>
#include <math.h>

#define PI 3.141592653589

using namespace std;

int main() {
	int r, c;
	int t;
	cin >> c;
	for (int T=1; T<=c; T++) {
		cin >> r >> t;
		cout << "Case #" << T << ": ";
		int rings=0;
		while (t>=0.0) {
			int blackRing = 2*r+1;
			if (t-blackRing<0.0) {
				break;
			}
			t-= blackRing;
			r+=2;
			rings++;
		}
		cout << rings << endl;
	}
	return 0;
}
