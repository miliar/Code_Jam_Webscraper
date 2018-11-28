#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int blockCount;
		cin >> blockCount;

		vector<double> blocksNaomi(blockCount);
		vector<double> blocksKen(blockCount);
		for (double &b : blocksNaomi)
			cin >> b;
		for (double &b : blocksKen)
			cin >> b;
		sort(blocksNaomi.begin(), blocksNaomi.end());
		sort(blocksKen.begin(), blocksKen.end());

		int y = 0;
		int nh = blockCount - 1;
		int nl = 0;
		int kh = blockCount -1;
		int kl = 0; 
		for (int i = 0; i < blockCount; i++) {
			if (blocksNaomi[nh] > blocksKen[kh]) {
				y++;
				nh--;
				kh--;
			} else {
				nl++;
				kh--;
			}
		}

		int z = 0;
		kh = blockCount - 1;
		kl = 0;
		for (int i = blockCount - 1; i >= 0; i--) {
			if (blocksNaomi[i] < blocksKen[kh]) {
				kh--;
			} else {
				kl++;
				z++;
			}
		}

		printf("Case #%d: %d %d\n", t, y, z	);
	}
	return 0;
}