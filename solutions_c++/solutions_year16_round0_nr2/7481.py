#include <stdio.h>
#include <string>
#include <stack>

#define maxSSize 101
#define maxTSize 100

using namespace std;

int T;
int result[maxTSize];
char S[maxSSize];
char temp[maxSSize];
char flipS[maxSSize];

int index;

bool isAllMinus(char S[], int size);
bool isAllPlus(char S[], int size);
int flip(char S[], int end, int flag);
void flipAll(int size);
char charReverse(char c);

int algoritm(char S[], int size);

int main() {
	scanf("%d", &T);

	for (int tc = 0; tc < T; tc++) {
		// init
		memset(S, '0', maxSSize);
		memset(flipS, '0', maxSSize);
		memset(temp, '0', maxSSize);
		int size = 0;

		scanf("%s", &S);

		for (int i = 0; i < maxSSize && S[i] != '\0'; i++) {
			size++; // st.push(S[i]);
			flipS[i] = S[i];
		}

		flipAll(size);

		int count = 0;
		int flip_count = 0;

		count = algoritm(S, size);
		flip_count = algoritm(flipS, size);
		flip_count++;

		if (count > flip_count) {
			result[tc] = flip_count;
			//printf("flip");
		}
		else {
			result[tc] = count;
			//printf("normal");
		}
	}

	for (int tc = 0; tc < T; tc++) {
		printf("Case #%d: %d\n", (tc + 1), result[tc]);
	}
}

int algoritm(char S[], int size) {
	int count = 0;

	if (isAllMinus(S, size)) {
		count = 1;
	}
	else {
		while (!isAllPlus(S, size)) {
			if (isAllMinus(S, size)) {
				count++;
				return count;
			}

			if (size == 1) {
				if (S[0] == '-') {
					count = 1;
					break;
				}
			}
			else {
				for (int i = 0; i < size; i++) {
					if (S[i] == '+'&&S[i + 1] == '-') {
						count += flip(S, i, 1);
						break;
					}
					else if (S[i] == '-'&&S[i + 1] == '+') {
						count += flip(S, i, 2);
						break;
					}
				}
			}

			/*
			for (int i = 0; i < size; i++) {
				printf("%s::%d", S, count);
			}
			*/
		}
	}

	return count;
}

bool isAllMinus(char S[], int size) {
	bool isAllMinus = true;

	for (int i = 0; i < size; i++) {
		if (S[i] == '+') {
			isAllMinus = false;
			break;
		}
	}

	return isAllMinus;
}

bool isAllPlus(char S[], int size) {
	bool isAllPlus = true;

	for (int i = 0; i < size; i++) {
		if (S[i] == '-') {
			isAllPlus = false;
			// index = i;
			break;
		}
	}

	return isAllPlus;
}

void flipAll(int size) {
	int x = size - 1;

	for (int i = x; i >= 0; i--) {
		temp[x - i] = charReverse(flipS[i]);
	}

	for (int i = 0; i < size; i++) {
		flipS[i] = temp[i];
	}
}

// flag 1 :: +-
// flag 2 :: -+
int flip(char S[], int end, int flag) {
	if (flag == 1) {
		//printf("flag1");

		for (int i = 0; i <= end; i++) {
			S[i] = charReverse(S[i]);
		}

		return 1;
	}
	else {
		//printf("flag2");

		for (int i = 0; i <= end; i++) {
			S[i] = charReverse(S[i]);
		}

		return 1;
	}
}

char charReverse(char c) {
	if (c == '+') {
		return '-';
	}
	else {
		return '+';
	}
}