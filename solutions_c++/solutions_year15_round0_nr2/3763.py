#include <iostream>
#include <queue>
#include <algorithm>
#include <vector>
using namespace std;

class comp {
	public:
	bool operator() (const int& lhs, const int &rhs) {
	 return (lhs < rhs);
	}
};

int main() {
	int T, D, P[1005];
	cin >> T;
	for (int test = 1; test <= T; ++test) {
		cout << "Case #" << test << ": ";
		//priority_queue<int, vector<int>, comp> queue;
		cin >> D;
		int mini = 1005;
		for (int i = 0; i < D; ++i) {
			cin >> P[i];
		}
		sort(P, P + D);
		int ans = P[D - 1];
		for (int i = 1; i <= P[D - 1]; ++i) {
			int tmp = 0;
			for (int j = 0; j < D; ++j) {
				tmp += P[j] / i;
				if (P[j] % i == 0) {
					tmp--;
				}
			}
			ans = min(ans, tmp + i);
		}
		cout << ans << "\n";
	}
	return 0;
}