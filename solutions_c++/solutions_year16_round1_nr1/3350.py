#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string build(const string& s, int pos, string cur)
{
	if (pos == s.length()) {
		return cur;
	}
	if (s[pos] >= cur[0]) {
		return build(s, pos + 1, s[pos] + cur);
	} else {
		return build(s, pos + 1, cur + s[pos]);
	}
}

string solve(const string& s)
{
	return build(s, 0, "");
}

int main()
{
	int c;
	cin >> c;
	for (int i = 1; i <= c; i++) {
		int n;
		string s;
		cin >> s;
		cout << "Case #" << i << ": " << solve(s) << endl;
	}
}
