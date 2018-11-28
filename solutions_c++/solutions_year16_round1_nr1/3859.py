#include <stdio.h>
#include <string>
#include <vector>

using namespace std;

void solve() {
	vector<char> ans;
	vector<char> reverse;
	char input[1001];

	scanf("%s", input);
	int len = strlen(input);
	ans.push_back(input[0]);
	char first = input[0];
	for (int i = 1; i < len; i++) {
		if (input[i] < first) {
			ans.push_back(input[i]);
		}
		else {
			reverse.push_back(input[i]);
			first = input[i];
		}
	}
	int size = reverse.size();
	for (int i = size - 1; i >= 0; i--)
		printf("%c", reverse[i]);
	size = ans.size();
	for (int i = 0; i < size; i++)
		printf("%c", ans[i]);
}
int main(void) {

	int T;
	scanf("%d", &T);

	for (int i = 0; i < T; i++) {
		printf("Case #%d: ", i + 1);
		solve();
		printf("\n");
	}
}