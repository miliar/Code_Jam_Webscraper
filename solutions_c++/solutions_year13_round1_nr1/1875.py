#include <iostream>

#define PI 3.14159265359

using namespace std;

long long getPow(long long i) {
	if (i>1500000000) return -1;
	return i*i;
}

int main() {
	int ti;
	cin >> ti;

	for (int tii=0; tii<ti; ++tii) {
		unsigned long long r, t, w=0, r2;
		cin >> r >> t;

		do {
			w++;
			/*r2 = getPow(r+1);
			if (r2<0) break;
			t -= r2;

			r2 = getPow(r);
			if (r2<0) break;
			t += r2;*/

			if (2*r+1 > t) break;
			t -= 2*r+1;

			r += 2;
		} while (t>=0);

		w--;

		cout << "Case #" << tii+1 << ": " << w << endl;
	}

	//system("PAUSE");
	return 0;
}