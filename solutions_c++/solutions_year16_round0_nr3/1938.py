#include <iostream>
#include <string>
#include <vector>
#include <set>
using namespace std;

bool is_prime(int x) {
	for (int i = 2; i * i <= x; i++) {
		if (x % i == 0) {
			return false;
		}
	}
	return true;
}

int main()
{
	//freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	cin >> t;
	for (int x = 0; x < t; x++) {
		int n, u;
		cin >> n >> u;
		vector<int> primes;
		for (int i = 2; i <= (1<<(n/2+2)); i++) {
			if (is_prime(i)) {
				primes.push_back(i);
			}
		}
		int l = int(primes.size());
		cout << "Case #" << x + 1 << ":" << endl;
		int cnt = 0;
		set<vector<int>> been;
		while (cnt < u) {
			vector<int> cur;
			cur.push_back(1);
			for (int i = 1; i < n - 1; i++) {
				cur.push_back(rand() % 2);
			}
			cur.push_back(1);
			if (been.find(cur) != been.end()) {
				cerr << "Found dup." << endl;
				continue;
			}
			vector<int> ans;
			for (int d = 2; d <= 10; d++) {
				vector<int> mods(l);
				for (int i = 0; i < n; i++) {
					for (int j = 0; j < l; j++) {
						mods[j] = mods[j] * d + cur[i];
						mods[j] %= primes[j];
					}
				}
				int ind = find(mods.begin(), mods.end(), 0) - mods.begin();
				if (ind != l) {
					ans.push_back(primes[ind]);
				}
			}
			if (ans.size() == 9) {
				been.insert(cur);
				for (int i = 0; i < n; i++) cout << cur[i];
				cout << " ";
				for (int i = 0; i < 9; i++) {
					cout << ans[i] << " ";
				}
				cout << endl;
				cnt++;
			}
		}
	}
    return 0;
}

