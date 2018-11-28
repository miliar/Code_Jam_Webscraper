#include <iostream>
#include <string>

using namespace std;

#define rep(i, n) for (int i = 0; i < n; i++)

int main(void)
{
	int t;
	cin >> t;
	rep(i, t) {
		string s;
		cin >> s;
		int count = 0;
		rep(j, (int)s.length() - 1) if (s[j] != s[j + 1]) count++;
		if (s[(int)s.length() - 1] == '-') count++;
		cout << "Case #" << i + 1 << ": " << count << endl;
	}
	return 0;
}
