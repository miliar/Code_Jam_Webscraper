#include <stdio.h>
#include <list>
#define maxTest 100
#define maxSize 1001

using namespace std;

int T;
char input[100][maxSize];
char result[100][maxSize];
list<char> S;


int main() {
	scanf("%d", &T);

	for (int tc = 0; tc < T; tc++) {
		// init
		scanf("%s", &input[tc]);
		
		for (int i = 0; i < maxSize && input[tc][i] != '\0'; i++) {
			char front;

			if (S.size() != 0) {
				front = S.front();
			}
			else {
				front = input[tc][i];
			}

			if (front > input[tc][i]) {
				S.push_back(input[tc][i]);
			}
			else {
				S.push_front(input[tc][i]);
			}
		}

		int size = S.size();
		for (int i = 0; i < size; i++) {
			result[tc][i] = S.front();
			S.pop_front();
		}
		result[tc][size] = '\0';

		// S.clear;

		// printf("%s", &input[tc]);
		// memset(S, '0', maxSSize);
	}

	FILE *fp = fopen("output.txt", "w");

	// print
	for (int tc = 0; tc < T; tc++) {
		fprintf(fp, "Case #%d: %s\n", (tc + 1), result[tc]);
	}
}