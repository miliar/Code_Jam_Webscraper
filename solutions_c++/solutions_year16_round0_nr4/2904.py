#include <iostream>
#include <cmath>
using namespace std;

int main() {
	int T, K, C, S;
	cin >> T;
	for(int ix = 1; ix <= T; ix++) {
		cin >> K >> C >> S;
		int diff = (pow(K, C)-(K-1)) - (K-1);
		if(diff < S && S != K)
			cout << "Case #" << ix << ": IMPOSSIBLE" << endl;
		else if(K == S) {
			cout << "Case #" << ix << ":";
			for(int iy = 1; iy <= S; iy++)
				cout << " " << iy;
			cout << endl;
		}
		else {
			cout << "Case #" << ix << ":";
			for(int iy = 0; iy < S; iy++)
			cout << " " << (pow(K, C-1)-C)*(iy+1);
			cout << endl;
		}
	}

	return 0;
}
