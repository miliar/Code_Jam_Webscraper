#include <iostream>
using namespace std;

int main() {
	int tt;
	cin >> tt;
	for (int t = 1; t <= tt; t++) {
		int a;
		cin >> a;
		int ar[a];
		for (int i = 0; i < a; i++) {
			cin >> ar[i];
		}
		int ansa = 0, ansb = 0;
		int mk = 0;
		for (int i = 1; i < a; i++) {
			if (ar[i] < ar[i-1]) {
				ansa += ar[i-1]-ar[i];
				mk = max(ar[i-1]-ar[i], mk);
			}
		}
		for (int i = 0; i < a-1; i++) {
			ansb += min(ar[i], mk);
		}
		cout << "Case #" << t << ": " << ansa << " " << ansb << endl;
	}
	return 0;
}