#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

const int N = 2e5 + 6;

char s[N];

int main() {
	int tests;
	scanf("%d", &tests);
	while (tests--) {
		scanf("%s", s + 1);
		int n = strlen(s + 1), answer = 0;
		static int testCount = 0;
		vector<char> stack;
		for (int i = 1; i <= n; i++) {
			if (stack.size() == 0 || stack.back() != s[i]) {
				stack.push_back(s[i]);
			} else {
				stack.pop_back();
				answer += 10;
			}
		}
		printf("Case #%d: %d\n", ++testCount, answer + 5 * (int)stack.size() / 2);
	}
	return 0;
}
