#include<iostream>
#include<cstring>
#include<cmath>
#include<vector>
#include<map>
#include<queue>
#include<algorithm>

using namespace std;

int a[3000];

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL), cout.precision(15);
	int T; cin >> T;
	for (int t = 1; t <= T; t++) {
		int N; cin >> N;
		for (int i = 0; i < 3000; i++) a[i] = 0;
		for (int i = 0; i < 2*N-1; i++) {
			for (int k = 0; k < N; k++) {
				int h; cin >> h;
				a[h]++;
			}
		}
		vector<int> res;
		for (int k = 1; k <= 2500; k++) {
			if (a[k] % 2 != 0) res.push_back(k);
		}
		cout << "Case #" << t << ":";
		for (int i = 0; i < res.size(); i++) cout << " " << res[i];
		cout << "\n";
	}

	return 0;
}
