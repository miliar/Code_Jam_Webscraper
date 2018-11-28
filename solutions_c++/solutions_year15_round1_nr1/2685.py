#include<iostream>
using namespace std;
int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		int N;
		cin >> N;
		int m[10010];
		int maxi = 0;
		long long int ans1 = 0, ans2 = 0;
		for (int j = 0; j < N; j++) {
			cin >> m[j];
			if (j > 0 && m[j] < m[j-1]) {
				ans1 += (m[j-1] - m[j]);
				if ((m[j-1] - m[j]) > maxi)
					maxi = m[j-1] - m[j];
			}
		}
		for (int j = 0; j < N - 1; j++)
			if (m[j] > maxi)
				ans2 += maxi;
			else
				ans2 += m[j];
		cout << "Case #" << i << ": " << ans1 << " " << ans2 << endl;
	}
	return 0;
}
