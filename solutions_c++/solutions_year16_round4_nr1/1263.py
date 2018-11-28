#include <bits/stdc++.h>

using namespace std;

string name = "RPS";

void S(string &s, char q, int n) {
	if (n == 0){
		s += q;
		return ;
	}
	int i = 0;
	for (; i < 3 && name[i] != q; ++i);
	S(s, name[i], n - 1);
	S(s, name[(i + 3 - 1) % 3], n - 1);
}

bool F(const string &s, const vector<int> &arr) {
	vector<int> p_arr(3);
	for (int i = 0; i < s.size(); ++i) {
		for (int j = 0; j < 3; ++j) {
			if (s[i] == name[j]) {
				p_arr[j]++;
			}
		}
	}
	bool ans = true;
	for (int i = 0; i < 3; ++i) {
		ans &= arr[i] == p_arr[i];
	}
	return ans;
}

void Sort(string &s, int l, int r) {
	if (l + 1 == r) {
		return ;
	}
	int mid = (l + r) / 2;
	Sort(s, l, mid);
	Sort(s, mid, r);
	bool ans = true;
	for (int i = 0; i < mid - l; ++i) {
		if (s[l + i] != s[mid + i]) {
			if (s[l + i] > s[mid + i]) {
				ans = false;
			}
			break;
		}
	}
	if (ans == false) {
		for (int i = 0; i < mid - l; ++i) {
			swap(s[l + i], s[mid + i]);
		}
	}
}

void Solve() {
	int n;
	vector<int> arr(3);
	cin >> n;
	for (int i = 0; i < 3; ++i) {
		cin >> arr[i];
	}
	string ans;
	for (int i = 0; i < 3; ++i) {
		string s;
		S(s, name[i], n);
		if (F(s, arr)) {
			Sort(s, 0, s.size());
			if (ans == "" || ans > s) {
				ans = s;
			}
		}
	}
	if (ans == "") {
		cout << "IMPOSSIBLE";
	} else {
		cout << ans;
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	cin >> n;
	for (int i = 1; i <= n; ++i) {
		cout <<  "Case #" << i << ": ";
		Solve();
		cout << endl;
	}
	return 0;
}
