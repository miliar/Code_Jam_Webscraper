#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int cases;
	cin >> cases;

	for (int test = 1; test <= cases; ++test) {
		int s_max;
		cin >> s_max;
		string s;
		cin >> s;

		int stand = 0, answer = 0;
		for (int i = 0; i < s.size(); ++i) {
			int cur = (int)s[i] - 48;
			if (!cur)
				continue;
			if (i <= stand) {
				stand += cur;
			}
			else {
				int need = (i - stand);
				answer += need;
				stand += (need + cur);
			}
		}

		cout << "Case #" << test << ": " << answer << endl;
	}

	return 0;
}