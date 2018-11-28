#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>

using namespace std;
const int maxn = 1000 + 10;

deque<char> dq;
char s[maxn];
int main() {
	int T, kase = 0;
	scanf("%d", &T);
	while (T--) {
		printf("Case #%d: ", ++kase);
		scanf("%s", s);
		dq.push_front(s[0]);
		for (int i = 1; s[i] != '\0'; i++) {
			if (s[i] < dq.front()) {
				dq.push_back(s[i]);
			}
			else {
				dq.push_front(s[i]);
			}
		}
		int len = strlen(s);
		for (int i = 0; i < len; i++) {
			printf("%c", dq.front());
			dq.pop_front();
		}
		printf("\n");
	}
	return 0;
}
