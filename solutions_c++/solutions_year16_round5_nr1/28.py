#include<vector>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;

const int N = 20005;

int n;

char s[N];

int main() {
	int T;
	scanf("%d", &T);
	while (T--) {
		static int id = 0;
		printf("Case #%d: ", ++id);
		scanf("%s", s);
		vector<char> stack;
		int ans = 0;
		n = strlen(s);
		for (int i = 0; i < n; ++i) {
			if (stack.size() > 0 && stack.back() == s[i]) {
				ans += 10;
				stack.pop_back();
			} else {
				stack.push_back(s[i]);
			}
		}
		ans += stack.size() / 2 * 5;
		printf("%d\n", ans);
	}
	return 0;
}
