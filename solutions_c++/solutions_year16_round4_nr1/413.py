#include <iostream>
#include <string>

#define MAXC 3

using namespace std;

int tests, n, c[MAXC], cnew[MAXC];
string sc[MAXC], scnew[MAXC];

int main() {
	cin >> tests;
	for (int test = 1 ; test <= tests ; test ++) {
		cout << "Case #" << test << ": ";
		cin >> n;
		//for (int i = 0 ; i < MAXC ; i ++) cin >> c[i];
		cin >> c[1] >> c[0] >> c[2];
		sc[0] = "P";
		sc[1] = "R";
		sc[2] = "S";
		bool ok = true;
		for (int j = 0 ; j < n ; j ++) {
			if (max(c[0], max(c[1], c[2])) * 2 > c[0] + c[1] + c[2]) {
				ok = false;
				cout << "IMPOSSIBLE" << endl;
				break;
			}
			for (int i = 0 ; i < MAXC ; i ++) {
				cnew[i] = (c[i] + c[(i + 1) % 3] - c[(i + 2) % 3]) / 2;
				scnew[i] = min(sc[i], sc[(i + 1) % 3]) + max(sc[i], sc[(i + 1) % 3]);
			}
			for (int i = 0 ; i < MAXC ; i ++) c[i] = cnew[i], sc[i] = scnew[i];
		}
		if (!ok) continue;
		for (int i = 0 ; i < MAXC ; i ++) if (c[i] == 1) cout << sc[i] << endl;
	}
	return 0;
}