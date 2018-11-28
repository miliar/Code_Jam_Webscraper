#include <iostream>
#include <vector>
using namespace std;

int main(void) {
	vector<int> prvy(4), druhy(4);
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int P;
		cin >> P;
		for (int j = 1; j < P; j++) {
			int foo;
			cin >> foo >> foo >> foo >> foo;
		}
		cin >> prvy[0] >> prvy[1] >> prvy[2] >> prvy[3];
		for (int j = P; j < 4; j++) {
			int foo;
			cin >> foo >> foo >> foo >> foo;
		}
		
		int D;
		cin >> D;
		for (int j = 1; j < D; j++) {
			int foo;
			cin >> foo >> foo >> foo >> foo;
		}
		cin >> druhy[0] >> druhy[1] >> druhy[2] >> druhy[3];
		for (int j = D; j < 4; j++) {
			int foo;
			cin >> foo >> foo >> foo >> foo;
		}
		
		int rieseni = 0, vysledok = 0;
		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				if (prvy[j] == druhy[k]) {
					rieseni++;
					vysledok = prvy[j];
				}
			}
		}
		cout << "Case #" << i+1 << ": ";
		if (rieseni > 1) {
			cout << "Bad magician!" << endl; 
		} else if (rieseni == 1) {
			cout << vysledok << endl;
		} else {
			cout << "Volunteer cheated!" << endl; 
		}
	}
	return 0;
}
