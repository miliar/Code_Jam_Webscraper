#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int it = 1; it <= T; ++it) {
		int n;
		cin >> n;
		string S;
		cin >> S;
		int cur = 0;
		int add = 0;
		for (int i = 0; i < S.size(); ++i) {
			if (cur < i) {
				add += i - cur;
				cur = i;
			}
			cur += S[i] - '0';
		}
		printf("Case #%d: %d\n", it, add);
	}
}
