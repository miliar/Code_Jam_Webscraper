#include <iostream>
#include <limits>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int T;

	cin >> T;
	for (int tc = 1; tc <= T; tc++) {

		vector<int> V;
		int D;
		cin >> D;
		for (int i = 0; i < D; i++){
			int tmp;
			cin >> tmp;
			V.push_back(tmp);
		}
		sort(V.begin(), V.end(), std::greater<int>());
		int massimo = V[0];
		long ans = std::numeric_limits<int>::max();
		for (int M = 1; M <= massimo; M++) {
			long ret = 0;
			for (int i = 0; i < V.size(); i++) {
				if (V[i] == M) ret+=0;
				else if (V[i] % M == 0) ret+=V[i]/M-1;
				else ret += V[i]/M;
			}
			ans = min(ans, ret+M);
		}

		cout << "Case #" << tc << ": " << ans << endl;
	}

	return 0;
}