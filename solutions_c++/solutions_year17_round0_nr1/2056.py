#include <iostream>
#include <string>

using namespace std;

#define REP(i, n) for(int i(0); i < (int)(n); i++)
#define FOR(i, a, b) for (int i(a); i <= (int)(b); i++)

void Work(int casen) {
	string ans = "IMPOSSIBLE";
	string s;
	int k;
	cin >> s >> k;
	int cnt = 0;
	for (int i = 0; i < s.length() && i + k <= (int)s.length(); i++) {
		if (s[i] == '+') continue;
		for (int j = 0; j < k; j++) s[i + j] = '+' - (int)s[i + j] + '-';
		cnt++;
	}
	if (s.find('-') == string::npos)
		ans = to_string(cnt);
	cout << "Case #" << casen << ": " << ans << endl;
}

int main() {
	int n;
	cin >> n;
	FOR(i, 1, n) {
		Work(i);
	}
	return 0;
}