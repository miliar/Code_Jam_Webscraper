#include <iostream>
#include <string>

using namespace std;

int main()
{
	int t, ct;
	freopen("a.in", "r", stdin);
	cin >> ct;
	for (t = 1; t <= ct; t++)
	{
		cout << "Case #" << t << ": ";
		string s;
		int k;
		cin >> s >> k;
		int count = 0;
		for (int i = 0; i <= s.length() - k; i++) {
			if (s[i] == '+') continue;
			for (int j = i; j < i + k; j++) {
				if (s[j] == '+')s[j] = '-';
				else s[j] = '+';
			}
			count++;
		}
		for (int i = s.length() - k; i < s.length(); i++) {
			if (s[i] == '-') {
				count = -1;
				break;
			}
		}
		if(count == -1) cout << "IMPOSSIBLE" << endl;
		else cout <<count<< endl;
	}

	return 0;
}
