#include <iostream>
using namespace std;

int main () {
	int t;
	cin >> t;
	for (int i=1; i<=t; i++) {
		int n;
		cin >> n;
		if (n == 0) {
			cout << "Case #" << i << ": INSOMNIA\n";
			continue;
		}
		bool bol[10];
		for (int j=0; j<10; j++) {
			bol[j] = false;
		}
		int pocbol = 0;
		int kolko = 0;
		while (pocbol < 10) {
			kolko += n;
			int zost = kolko;
			while (zost > 0) {
				int cif = zost%10;
				pocbol += (!bol[cif]);
				bol[cif] = true;
				zost /= 10;
			}
		}
		cout << "Case #" << i << ": " << kolko << "\n";
	}
	return 0;
}
