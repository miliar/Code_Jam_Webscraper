# include <stdio.h>
# include <string.h>
# include <stdlib.h>
# include <deque>

using namespace std;

int main() {
	freopen("a.txt", "r", stdin);
	freopen("b.txt", "w", stdout);

	int t;
	scanf("%d", &t);

	for (int kase = 1; kase <= t; kase ++) {
		printf("Case #%d: ", kase);

		char s[1005];

		scanf("%s%*c", s);

		int len = strlen(s);

		deque<char> dq;

		dq.push_front(s[0]);
		for (int i = 1; i < len; i ++) {
			if (s[i] < dq.front()) {
				dq.push_back(s[i]);
			} else {
				dq.push_front(s[i]);
			}
		}

		while (!dq.empty()) {
			printf("%c", dq.front());
			dq.pop_front();
		}

		printf("\n");
	}
}