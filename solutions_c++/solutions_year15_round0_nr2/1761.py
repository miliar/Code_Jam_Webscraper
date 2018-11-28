#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

const int MAXN = 1000 + 10;
int A[MAXN];
int D;


int main () {
	int cases;
	cin >> cases;

	for (int tc = 1; tc <= cases; tc ++) {
		cin >> D;
		int Dm = 0;
		for (int i = 0; i < D; i ++) {
			cin >> A[i];
			Dm = max(Dm, A[i]);
		}

		int ret = INT_MAX;
		for (int left = 1; left <= Dm; left ++) {
			int ans = left;
			for (int i = 0; i < D; i ++) {
				ans += (A[i] + left - 1) / left - 1;
			}
			ret = min(ret, ans);
		}

		cout << "Case #" << tc << ": " << ret << endl;
	}
}