#include <iostream>
#include <fstream>
#include <cstring>
#include <sstream>

using namespace std;

const int maxn = 0;
int t;

string toStr(char a) {
	stringstream str;
	str << a;
	return str.str();
}

int main() {
	ios_base::sync_with_stdio(0);
	ifstream cin("A.in");
	ofstream cout("A.out");
	cin >> t;
	for (int i = 0; i < t; i++) {
		cout << "Case #" << i+1 << ": ";
		string s;
		cin >> s;
		string ans;
		ans = toStr(s[0]);
		for (int j = 1; j < s.size(); j++) {
			if (s[j] >= ans[0]) {
				ans = toStr(s[j])+ans;
			} else {
				ans = ans+toStr(s[j]);
			}
		}
		cout << ans << '\n';
	}
	return 0;
}

