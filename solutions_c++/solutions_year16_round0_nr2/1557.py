#include <iostream>
#include <string.h>
#include <stdint.h>
#include <vector>
#include <stack>
#include <algorithm>
#include <stdio.h>
#include <bitset>
using namespace std;

int main(int argc, char* argv[])
{
	if (argc >= 2) {
		FILE* fp = freopen(argv[1], "r", stdin);
	}

	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		string s;
		cin >> s;
		int n = 1;
		for (size_t i = 1; i < s.length(); i++) {
			if (s[i] != s[i - 1]) {
				n++;
			}
		}
		int result = 0;
		if (s[0] == '+') {
			result = n & ~1;
		} else {
			result = ((n - 1) & ~1) + 1;
		}
		cout << "Case #" << i + 1 << ": " << result << endl;
	}

	return 0;
}
