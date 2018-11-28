#include <bits/stdc++.h>

using namespace std;

int TC;
char word[1010];

int main() {
	scanf("%d", &TC);
	for (int T = 1; T <= TC; T++) {
		scanf("%s", word);
		deque<char> ans;
		ans.push_back(word[0]);
		for (int i = 1; i < strlen(word); i++) {
			char front = ans.front();
			if (word[i] >= front) {
				ans.push_front(word[i]);
			} else {
				ans.push_back(word[i]);
			}
		}

		printf("Case #%d: ", T);
		for (int i = 0; i < strlen(word); i++) {
			printf("%c", ans.front()); ans.pop_front();
		}
		printf("\n");
	}
	return 0;
}