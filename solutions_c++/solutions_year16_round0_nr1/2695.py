#include <iostream>
#include <cmath>

using namespace std;

const unsigned short flip [10] = {1,2,4,8,16,32,64,128,256,512};
int tentothe (int n) {
	int result = 1;
	for (; n>0; n-- ) result *= 10;
	return result;
}

int main() {
	unsigned short check = 0;

	int T;
	int N;

	cin >> T;
	for (int t = 1; t <= T; t++) {
		check = 0;
		cin >> N;		
		int Nnew = 0;

		cout << "Case #" << t << ": ";

		if (N == 0) cout << "INSOMNIA\n";
		else {
			while ( check != 1023 ) {
				Nnew += N;
				int Ncopy = Nnew;
				int n = floor(log10(Ncopy));
				while (n >= 0) {
					check = check | flip[Ncopy/tentothe(n)];
					Ncopy = Ncopy%tentothe(n);
					n--;
				}
			}
			cout << Nnew << '\n';
		}
	}
}
