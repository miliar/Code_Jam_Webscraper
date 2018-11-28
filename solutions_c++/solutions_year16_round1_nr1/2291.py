#include <cstdio>
#include <cstring>
#include <list>

using namespace std;

void calc() {
	char in[1001];
	int i;
	list<char> ans;

	scanf("%s", in);
	for (i = 0; in[i]; i++) {
		if (i == 0 || ans.front() <= in[i]) {
			ans.push_front(in[i]);
		} else {
			ans.push_back(in[i]);
		}
	}

	for (char a : ans) {
		printf("%c", a);
	}

	printf("\n");
}

int main() {
	int tc, t;

	scanf("%d", &tc);
	for (t = 1; t <= tc; t++) {
		printf("Case #%d: ", t);
		calc();
	}

	return 0;
}