#include <iostream>
#include <algorithm>

using namespace std;

void flip(string &s)
{
	char top = s[0];
	for (int i = 0; i < s.length() && s[i] == top; i++) {
		s[i] = (top == '+') ? '-' : '+';
	}
}

void trim(string &s)
{
	while (s.length() > 0 && s[s.length() - 1] == '+')
		s.pop_back();
}

int main()
{
	int T;
	string S;
	cin >> T;
	for (int caseN = 1; caseN <= T; caseN++) {
		cin >> S;
		trim(S);
		int ans = 0;
		while (S.length() > 0) {
			flip(S);
			trim(S);
			ans++;
		}
		cout << "Case #" << caseN << ": " << ans << endl;
	}
	return 0;
}