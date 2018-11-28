#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int T;
	cin >> T;
	for(int t = 0; t < T; t++) {
		int D;
		cin >> D;
		vector<int> P;
		for(int i = 0; i < D; i++) {
			int p;
			cin >> p;
			P.push_back(p);
		}

		int res = 1024;
		for(int i = 1; i < 1024; i++) {
			int add = 0;
			for(int j = 0; j < P.size(); j++) {
				add += P[j] / i + ((P[j] % i) ? 1 : 0) - 1;
			}
			res = min(res, i + add);
		}

		cout << "Case #" << t + 1 << ": " << res << endl;
	}
}
