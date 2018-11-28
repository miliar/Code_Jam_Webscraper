#include <iostream>
#include <set>
#include <string>

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	long long T;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		string s;
		cin >> s;
		s += '+';
		int answer = 0;
		for (int i = 0; i < s.size() - 1; ++i) {
			if (s[i] != s[i + 1]) {
				++answer;
			}
		}
		cout << "Case #" << t + 1 << ": " << answer << endl;
	}
	return 0;
}