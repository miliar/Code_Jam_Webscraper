#include <bits/stdc++.h>
using namespace std;

string num[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int p[] = {0, 2, 4, 6, 8, 1, 3, 5, 7, 9};

void solve(){
	string s;
	cin >> s;

	int mp[26] = {0};
	for (int i = 0; i < s.length(); i++) {
		mp[s[i] - 'A']++;
	}

	vector<int> ans;

	for (int i = 0; i < 10; i++) {
		int mpi[26] = {0};
		for (int j = 0; j < num[p[i]].length(); j++) {
			mpi[num[p[i]][j] - 'A']++;
		}

		while (true) {
			bool contains = true;
			for (int j = 0; j < 26; j++) {
				if (mp[j] < mpi[j]) {
					contains = false;
				}
			}
			if (!contains) {
				break;
			}
			ans.push_back(p[i]);
			for (int j = 0; j < 26; j++) {
				mp[j] -= mpi[j];
			}
		}
	}

	sort(ans.begin(), ans.end());

	for (int i = 0; i < ans.size(); i++) {
		cout << ans[i];
	}
}

int main(){
#ifdef HELTHAZAR
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int test;
	cin >> test;
	for (int t = 1; t <= test; t++) {
		//printf("Case #%d: ", t);
		cout << "Case #" << t << ": ";
		solve();
		cout << endl;
		//printf("\n");
	}
}
