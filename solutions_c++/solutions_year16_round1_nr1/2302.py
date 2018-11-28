#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;

int T;
string str;
string res;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t, i;
	
	scanf("%d", &T);
	for (t = 1; t <= T; t++) {
		cin >> str;
		int len = str.size();
		res = str[0];
		char lstr = str[0];
		for (i = 1; i < len; i++) {
			if (str[i] >= lstr) {
				lstr = str[i];
				res = lstr + res;
			}
			else res += str[i];
		}
		cout << "Case #" << t << ": " << res << endl;
	}
	return 0;
}
