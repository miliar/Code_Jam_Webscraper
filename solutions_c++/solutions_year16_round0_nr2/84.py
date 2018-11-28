#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

char S[200];

void read() {
	scanf("%s", S);
}

void process() {
	int res = 0;
	char last = '+';
	for (int i = strlen(S) - 1; i >= 0; i--) {
		if (S[i] != last) {
			res++;
		}
		last = S[i];
	}
	printf("%d\n", res);
}

int main() {
	int cases;
	scanf("%d", &cases);

	for (int i = 1; i <= cases; i++) {
		printf("Case #%d: ", i);
		read();
		process();
	}
	return 0;
}