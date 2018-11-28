#include <iostream>
#include <fstream>

using namespace std;

int T, K, C, S;

int main() {
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out", "w", stdout);

	cin >> T;
	for(int i = 0; i < T; i++) {
		cin >> K >> C >> S;
		cout << "Case #" << i+1 << ":";
		for(int j = 0; j < S; j++) {
			cout << " " << j+1;
		}
		cout << endl;
	}

	return 0;
}