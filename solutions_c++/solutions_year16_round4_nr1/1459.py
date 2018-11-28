#include <cassert>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <queue>
#include <utility>

using namespace std;

inline char getWinner(char a, char b)
{
	assert(a != b);

	if (a > b) {
		swap(a, b);
	}

	if (a == 'P' && b == 'R') {
		return 'P';
	}

	if (a == 'P' && b == 'S') {
		return 'S';
	}

	if (a == 'R' && b == 'S') {
		return 'R';
	}

	assert(false);
	return '\0';
}

bool isOk(char *line)
{
	static char state[4100];
	strcpy(state, line);
	int count = strlen(state);

	while (count > 1) {
		for (int i = 0; i < (count / 2); i++) {
			if (state[i*2] == state[i*2+1]) {
				return false;
			}

			state[i] = getWinner(state[i*2], state[i*2+1]);
		}

		count /= 2;
	}

	return true;
}

char line[4100];

int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		printf("Case #%d: ", t);
		int N, R, P, S;
		scanf("%d%d%d%d", &N, &R, &P, &S);
		int p = 0;
		for (int i = 0; i < P; i++) {
			line[p++] = 'P';
		}
		for (int i = 0; i < R; i++) {
			line[p++] = 'R';
		}
		for (int i = 0; i < S; i++) {
			line[p++] = 'S';
		}
		line[p] = '\0';
		bool possible = false;
		do {
			if (isOk(line)) {
				possible = true;
				break;
			}
		} while (next_permutation(line, line+p));
		if (possible) {
			printf("%s\n", line);
		} else {
			printf("IMPOSSIBLE\n");
		}
	}
	return 0;
}
