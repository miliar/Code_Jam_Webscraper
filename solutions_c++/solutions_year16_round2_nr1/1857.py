#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	string str;
	int T;

	cin >> T;

	int t;
	for (int i = 1; i <= T; i++) {
		int ans[1000] = { 0 };
		t = 0;

		cin >> str;
		
		while (str.find('Z') != string::npos) {
			str.erase(str.find('Z'), 1);
			str.erase(str.find('E'), 1);
			str.erase(str.find('R'), 1);
			str.erase(str.find('O'), 1);
			ans[t++] = 0;
		}

		while (str.find('X') != string::npos) {
			str.erase(str.find('S'), 1);
			str.erase(str.find('I'), 1);
			str.erase(str.find('X'), 1);
			ans[t++] = 6;
		}

		while (str.find('G') != string::npos) {
			str.erase(str.find('E'), 1);
			str.erase(str.find('I'), 1);
			str.erase(str.find('G'), 1);
			str.erase(str.find('H'), 1);
			str.erase(str.find('T'), 1);
			ans[t++] = 8;
		}

		while (str.find('W') != string::npos) {
			str.erase(str.find('T'), 1);
			str.erase(str.find('W'), 1);
			str.erase(str.find('O'), 1);
			ans[t++] = 2;
		}

		while (str.find('H') != string::npos) {
			str.erase(str.find('T'), 1);
			str.erase(str.find('H'), 1);
			str.erase(str.find('R'), 1);
			str.erase(str.find('E'), 1);
			str.erase(str.find('E'), 1);
			ans[t++] = 3;
		}

		while (str.find('R') != string::npos) {
			str.erase(str.find('F'), 1);
			str.erase(str.find('O'), 1);
			str.erase(str.find('U'), 1);
			str.erase(str.find('R'), 1);
			ans[t++] = 4;
		}

		while (str.find('S') != string::npos) {
			str.erase(str.find('S'), 1);
			str.erase(str.find('E'), 1);
			str.erase(str.find('V'), 1);
			str.erase(str.find('E'), 1);
			str.erase(str.find('N'), 1);
			ans[t++] = 7;
		}

		while (str.find('F') != string::npos) {
			str.erase(str.find('F'), 1);
			str.erase(str.find('I'), 1);
			str.erase(str.find('V'), 1);
			str.erase(str.find('E'), 1);
			ans[t++] = 5;
		}

		while (str.find('O') != string::npos) {
			str.erase(str.find('O'), 1);
			str.erase(str.find('N'), 1);
			str.erase(str.find('E'), 1);
			ans[t++] = 1;
		}

		while (str.find('N') != string::npos) {
			str.erase(str.find('N'), 1);
			str.erase(str.find('I'), 1);
			str.erase(str.find('N'), 1);
			str.erase(str.find('E'), 1);
			ans[t++] = 9;
		}

		sort(ans, ans + t);

		printf("Case #%d: ", i);
		for (int j = 0; j < t; j++)
			cout << ans[j];
		cout << endl;
	}

	return 0;
}