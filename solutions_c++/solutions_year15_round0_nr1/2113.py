#include <iostream>

using namespace std;

int main() {
	int T, S, ret;
	string str;

	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		

		cin >> S;
		cin >> str;
		ret = 0;
		int people = 0;
		for (int i = 0; i <= S; i++) {
			if (str[i] != '0') {
				if (people >= i)
					people+=(str[i]-'0');
				else {
					ret += (i-people);
					people += (str[i]-'0') + (i-people);
				}
			}	
		}
		cout << "Case #" << tc << ": ";
		cout << ret << endl;
	}
	return 0;
}