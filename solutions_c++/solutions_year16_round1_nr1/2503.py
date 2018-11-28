#define A

#ifdef A
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <algorithm>
#include <set>
#include <string>
#include <vector>

using namespace std;

int main() {
	//freopen("in.txt", "rt", stdin);
	freopen("A-large.in", "rt", stdin);
	freopen("out.txt", "wt", stdout);

	int T;
	scanf("%d\n", &T);

	for (int i = 1; i <= T; i++) {
		string str;
		getline(cin, str);
		string res("");
		res += str[0];
		for (int j = 1; j < str.length(); j++) {
			if (res[0] > str[j]) {
				res = res + str[j];
			}
			else {
				res = str[j] + res;
			}
		}

		printf("Case #%d: %s\n", i, res.c_str());
	}

	return 0;
}

#endif