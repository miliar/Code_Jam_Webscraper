//1�����̋�Ԃ̂����ł��傫����Ԃ�I��łЂ����肩����
#include <iostream>
#include <string>
using namespace std;

int solve(string s) {
	int ans = 0;
	for (int i = 0; i < (int)s.length() - 1; i++)
		ans += (s[i] != s[i+1]);
	ans += (s[s.length() - 1] == '-');
	return ans;
}

int main() {
	int t; string s;
	cin >> t;
	for (int id = 1; id <= t; id++) {
		cin >> s;
		cout << "Case #" << id << ": ";
		cout << solve(s) << endl;
	}
	return 0;
}