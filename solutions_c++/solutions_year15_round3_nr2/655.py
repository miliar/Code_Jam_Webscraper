#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

int K, L, S;
char keys[101], target[101], current[101];

int countSubstrings(char *string, char *pattern, int patternLength) {
	int count = 0;

	while (*string) {
		if (strncmp(string++, pattern, patternLength) == 0) {
			count++;
		}
	}

	return count;
}

pair<int, int> solve(int pos) {
	current[pos] = 0;
	
	if (pos == S) {
		int solution = countSubstrings(current, target, L);
		return make_pair(solution, solution);
	}

	pair<int, int> solution;

	for (int i = 0; i < K; i++) {
		current[pos] = keys[i];

		pair<int, int> partial = solve(pos + 1);
		solution = make_pair(solution.first + partial.first, max(solution.second, partial.second));
	}

	return solution;
}

int main(void) {
	int numCases;

	cin >> numCases;
	for (int numCase = 1; numCase <= numCases; numCase++) {
		cin >> K >> L >> S;
		scanf("%s", keys);
		scanf("%s", target);

		pair<int, int> solution = solve(0);
		printf("Case #%d: %lf\n", numCase, solution.second - ((double)solution.first / pow(K, S)));
	}
}