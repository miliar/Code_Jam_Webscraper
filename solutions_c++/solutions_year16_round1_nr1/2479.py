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
		string S;
		cin >> S;

		string result = S.substr(0, 1);
		for (size_t i = 1; i < S.size(); i++) {
			char c = S[i];
			if (c + result > result + c) {
				result = c + result;
			} else {
				result = result + c;
			}
		}

		cout << "Case #" << i + 1 << ": " << result << endl;
	}

	return 0;
}
