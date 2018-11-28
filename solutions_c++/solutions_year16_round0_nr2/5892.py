#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

int main() {
	int T;
	cin >> T;
	getchar();

	for (int ct = 1; ct <= T; ct++) {
		string s;
		getline(cin, s);

		int sz = s.size();
		int result = 0; 
		for (int i = 0; i < sz - 1; i++) {
			if (s[i] != s[i + 1])
				result++;
		}
		if (s[sz - 1] == '-')
			result++;

		cout << "Case #" << ct << ": " << result << endl;
	}

	return 0;
}