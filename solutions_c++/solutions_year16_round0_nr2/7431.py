#include <iostream>
#include <string>
using namespace std;

int T;
int res;
string str;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t, i;
	cin >> T;
	for (t = 1; t <= T; t++) {
		cin >> str;
		str += '+';

		res = 0;
		int len = str.size();
		for (i = 1; i < len; i++) {
			if (str[i - 1] != str[i]) res++;
		}
		cout << "Case #" << t << ": " << res << endl;
	}
	return 0;
}