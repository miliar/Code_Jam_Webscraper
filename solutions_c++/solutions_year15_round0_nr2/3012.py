#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <stdlib.h>
using namespace std;

int main() {
	freopen("B-large.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int T; cin >> T;
	for(int t = 1; t <= T; t++) {
		int n; cin >> n;
		vector<int> ar(n);
		for(int i = 0; i < n; i++)
			cin >> ar[i];
		int me = *max_element(ar.begin(), ar.end());
		int ans = me;
		for(int b = 1; b <= me; b++) {
			int a = b;
			for(int i = 0; i < n; i++)
				a += (ar[i] - 1) / b;
			ans = min(ans, a);
		}
		cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}