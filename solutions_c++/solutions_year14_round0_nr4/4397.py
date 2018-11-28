#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t) {
		int n;
		cin >> n;
		vector<double> v1(n), v2(n);
		
		for(int i = 0; i < n; ++i) {
			cin >> v1[i];
		}

		for(int i = 0; i < n; ++i) {
			cin >> v2[i];
		}

		sort(v1.begin(), v1.end());
		sort(v2.begin(), v2.end());

		int ans1 = 0, ans2 = 0;

		for(int i = n - 1, j = n - 1; i >= 0 && j >= 0;) {
			if(v1[j] > v2[i]) {
				ans1++;
				i--;
				j--;
			} else {
				i--;
			}
		}	

		for(int i = n - 1, j = n - 1; i >= 0 && j >= 0;) {
			if(v2[j] > v1[i]) {
				ans2++;
				i--;
				j--;
			} else {
				i--;
			}
		}

		cout << "Case #" << t << ": " << ans1 << ' ' << n - ans2 << endl;

	}
}
