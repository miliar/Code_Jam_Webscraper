#include <iostream>
#include <cmath>
using namespace std;

int main() {
	int n;
	int caseCount = 0;

	cin >> n;
	while (n--) {
		int r, t, ring;
		int ringCount = 0;

		cin >> r >> t;
		ring = pow(r + 1, 2) - pow(r, 2);
		while (t >= ring) {
			t -= ring;
			ringCount++;
			ring += 4;
		}
		cout << "Case #" << ++caseCount << ": " << ringCount << endl;
	}

    return 0;
}
