#include <iostream>
#include <vector>
#include <string>

using namespace std;

void main() {

	FILE *str, *abc;
	freopen_s(&str, "input.txt", "r", stdin);
	freopen_s(&abc, "out.txt", "w", stdout);

	int t;
	cin >> t;

	for (int i = 0; i < t; i++) {
		cout << "Case #" << i + 1 << ": ";
		
		string s;
		cin >> s;

		string ans = "";
		ans += s[0];

		for (int i = 1; i < s.length(); ++i)
			if (s[i] >= ans[0]) 
				ans = s[i] + ans;
			else
				ans = ans + s[i];
		cout << ans << endl;
	}
	

}