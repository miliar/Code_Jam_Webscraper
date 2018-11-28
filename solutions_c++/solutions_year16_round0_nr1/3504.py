#include <iostream>

using namespace std;

int main() {
	int T;
	cin >> T;
	for(int step = 1; step <= T; step++) {
		long unsigned int N, tmp;
		cin >> N;
		bool check[10] = {0}, flag = false;
		if(N != 0) {
			int iy = 1;
			for(; !flag; iy++) {
				tmp = N*iy;
				while(tmp > 0) {
					check[tmp % 10] = true;
					tmp /= 10;
				}

				flag = true;
				for(int ix = 0; ix < 10; ix++)
					flag &= check[ix];
			}

			iy--;
			cout << "Case #" << step << ": " << N*iy << "\n";
		} else {
			cout << "Case #" << step << ": INSOMNIA\n";
		}
	}

	return 0;
}
