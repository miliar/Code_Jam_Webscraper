#include <iostream>
#include <string>

#define rep(i, n) for (int i = 0; i < n; i++)

using namespace std;

int main(void)
{
	int t;
	cin >> t;
	rep(f, t) {
		string s;
		cin >> s;
		char a = 'A';
		int max = (int)a;
		string ans = "";
		int size = (int)s.length();
		rep(i, size) {
			if (max <= (int)s[i]) {
				ans = s[i] + ans;
				max = (int)s[i];
			}
			else ans = ans + s[i];
		}
		cout << "Case #" << f + 1 << ": " << ans << endl;
	}
	return 0;
}


