#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()

const double EPS = 1e-9;
const ll INF = 1e17;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(nullptr);
	cout.tie(nullptr);

	freopen("file.in", "r", stdin);
	freopen("file.out", "w", stdout);

	int t;
	cin >> t;


	for (int testNum = 1; testNum <= t; testNum++) {
		int n;
		cin >> n;

		vector<int> cnt(n);
		multiset<int> nums;
		int sm = 0;

		for (int i = 0; i < n; i++) {
			cin >> cnt[i];
			nums.insert(-cnt[i]);
			sm += cnt[i];
		}

		cout << "Case #" << testNum << ": ";

		while (sm > 0) {
			for (int i = 0; i < n; i++) {
				bool success = 0;

				for (int j = i; j <= n; j++) {
					if (j == n && cnt[i]) {
						nums.erase(nums.find(-cnt[i]));
						cnt[i]--;
						nums.insert(-cnt[i]);
						sm--;

						if (-(*nums.begin()) > sm / 2) {
							nums.erase(nums.find(-cnt[i]));
							cnt[i]++;
							nums.insert(-cnt[i]);
							sm++;
						} else {
							cout << char(i + 'A') << " ";
							success = 1;
							break;
						}
					} else if ((cnt[i] && cnt[j] && i != j) || (i == j && cnt[i] > 1)) {
						nums.erase(nums.find(-cnt[i]));
						cnt[i]--;
						nums.insert(-cnt[i]);
						nums.erase(nums.find(-cnt[j]));
						cnt[j]--;
						nums.insert(-cnt[j]);
						sm -= 2;

						if (-(*nums.begin()) > sm / 2) {
							nums.erase(nums.find(-cnt[j]));
							cnt[j]++;
							nums.insert(-cnt[j]);
							nums.erase(nums.find(-cnt[i]));
							cnt[i]++;
							nums.insert(-cnt[i]);
							sm += 2;
						} else {
							cout << char(i + 'A') << char(j + 'A') << " ";
							success = 1;
							break;
						}
					}
				}

				if (success) break;
			}
		}

		cout << "\n";
		cerr << "Case #" << testNum << " completed\n";
	}

	return 0;
}
