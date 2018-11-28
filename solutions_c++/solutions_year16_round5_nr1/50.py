#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<string>
#include <vector>
using namespace std;

const int MAX_N = 20000 + 10;

int main() {
	int T;
	cin >> T;
	for (int nc = 1; nc <= T; ++nc) {
		string S;
		cin >> S;
		vector<char> stack;

		int n = S.size();
		int ans = 0;
		for (int i = 0; i < n; ++i) {
			if (!stack.empty() && stack.back() == S[i]) {
				ans += 10;
				stack.pop_back();
			} else {
				stack.push_back(S[i]);
			}
		}

		ans += stack.size() / 2 * 5;

		printf("Case #%d: %d\n", nc, ans);
	}
	return 0;
}
