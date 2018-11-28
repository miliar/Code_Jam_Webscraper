#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>
#include <queue>
#include <cassert>

using namespace std;

int B, M;
int adj[6][6];
int nums[6];

bool check() {
	int count = 0;
	int qum[6][6], qum_[6][6];
	for (int r = 0; r < B; ++r) {
		for (int c = 0; c < B; ++c) {
			adj[r][c] = (nums[r] & (1 << c)) ? 1 : 0;
			qum[r][c] = adj[r][c];
			//cout << adj[r][c];
		}
		//cout << '\n';
	}
	for (int length = 1; length <= B; ++length) {
		count += qum[0][B - 1];
		for (int r = 0; r < B; ++r)
			for (int c = 0; c < B; ++c) {
				qum_[r][c] = 0;
				for (int k = 0; k < B; ++k) {
					qum_[r][c] += qum[r][k] * adj[k][c];
				}
			}
		for (int r = 0; r < B; ++r)
			for (int c = 0; c < B; ++c)
				qum[r][c] = qum_[r][c];
	}
	return count == M;
}

bool search_row(int r) {
	if (r == B - 1) {
		// Last row - only zeros, check it
		return check();
	}
	for (int mask = 0; mask < 1 << (B - r - 1); ++mask) {
		nums[r] = mask << (r + 1);
	    if (search_row(r + 1))
		    return true;
    }
	return false;
}

bool search() {
	return search_row(0);
}

int main()
{
	int T;
	cin >> T;
	for (auto casen = 1; casen <= T; ++casen) {
		cin >> B >> M;
		assert(B > 0 && B < 7);
		if (search()) {
			cout << "Case #" << casen << ": POSSIBLE\n";
			for (int r = 0; r < B; ++r) {
				for (int c = 0; c < B; ++c) {
					cout << adj[r][c];
				}
				cout << '\n';
			}

		}
		else {
			cout << "Case #" << casen << ": IMPOSSIBLE\n";
		}
	}

	return 0;
}

