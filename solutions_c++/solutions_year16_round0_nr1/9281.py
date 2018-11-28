#include<iostream>
#include<vector>
#include<conio.h>

using namespace std;

int main() {
	int T, i = 0;
	cin >> T;
	unsigned long n;
	unsigned long N[100], R[100];

	for (i = 0; i < T; i++) {
		cin >> n;
		N[i] = n;
	}

	for (i = 0; i < T; i++) {
		if (N[i] == 0) {
			R[i] = 0;
			continue;
		}

		short f[10] = { -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 };

		unsigned int multi = 0;

		while (!(f[0] == 0 && f[1] == 1 && f[2] == 2 && f[3] == 3 && f[4] == 4
			&& f[5] == 5 && f[6] == 6 && f[7] == 7 && f[8] == 8 && f[9] == 9)) {
			multi++;
			unsigned long product = multi * N[i];
			
			while (product) {
				int digit = product % 10;
				product = product / 10;
				
				switch (digit) {
				case 0: f[0] = 0; break;
				case 1: f[1] = 1; break;
				case 2: f[2] = 2; break;
				case 3: f[3] = 3; break;
				case 4: f[4] = 4; break;
				case 5: f[5] = 5; break;
				case 6: f[6] = 6; break;
				case 7: f[7] = 7; break;
				case 8: f[8] = 8; break;
				case 9: f[9] = 9; break;
				default:  break;
				}
			}
		}
		if (multi > 4294967295)
			R[i] = 0;
		else
			R[i] = multi*N[i];
	}
	for (i = 0; i < T; i++) {
		if (R[i] == 0)
			cout << "Case #" << i+1 << ": " << "INSOMNIA" << endl;
		else
			cout << "Case #" << i+1 << ": " << R[i] << endl;
	}
	_getche();
	return 0;
}