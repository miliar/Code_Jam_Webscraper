#include <iostream>
#include <set>
#include <vector>
using namespace std;

string add(string a, string b) {
	reverse(a.begin(), a.end());
	reverse(b.begin(), b.end());
	if (a.length() > b.length()) swap(a , b);
	int add = 0;
	string ans = "";
	for (int i = 0; i < a.length(); i++) {
		int x = a[i] - '0' + b[i] - '0' + add;
		add = x / 10;
		x %= 10;
		ans += char(x + '0');
	}
	for (int i = a.length(); i < b.length(); i++) {
		int x = b[i] - '0'+ add;
		add = x / 10;
		x %= 10;
		ans += char(x + '0');
	}
	if (add != 0) ans += '1';
	reverse(ans.begin(), ans.end());
	return ans;
}

int main() {
	int kase;
	cin >> kase;
	for (int ii = 0; ii < kase; ii++) {
		string s;
		cin >> s;
		vector<bool> vis(10, false);
		int digits = 0;
		bool exist = true;
		string curr = s;
		set<string> a;
		while (1) {
			for (auto ch : curr) {
				if (!vis[ch - '0']) {
					vis[ch - '0'] = true;
					digits++;
				}
			}
			if (digits == 10) break;
			a.insert(curr);
			curr = add(curr, s);
			if (a.find(curr) != a.end()) {
				exist = false;
				break;
			}
		}
		cout << "Case #" << ii + 1 << ": ";
		if (exist) cout << curr << endl;
		else cout << "INSOMNIA" << endl;
	}
	return 0;
}