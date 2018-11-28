#include <iostream>
#include <string>

using namespace std;

void solve(int i, string& pc) {
	int flips = 0;
	char st = '+';
	for (int i = pc.size() - 1; i >= 0; --i) {
		if (st != pc[i]) {
			++flips;
			st = pc[i];
		}
	}
	cout << "Case #" << i << ": " << flips << endl;
}

int main() {
	int T = 0;	
	cin >> T;

	for (int i = 0; i < T; ++i) {
		string pc;
		cin >> pc;
		solve(i + 1, pc);
	}

	return 0;
}
