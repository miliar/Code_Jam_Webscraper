#include <iostream>
#include <cstdio>
#include <string.h>
using namespace std;

int alphabet[26][10];
char nums[10][6] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

bool isPerfect(int * letters) {
	for (int i = 0; i < 26; i++) {
		if (letters[i] != 0) return false;
	}
	return true;
}

bool isValid(int * letters) {
	for (int i = 0; i < 26; i++) {
		if (letters[i] < 0) return false;
	}
	return true;
}

void adjustLetters(int * letters, int num, int offset) {
	for (int i = 0; i < 26; i++) {
		letters[i] += alphabet[i][num] * offset;
	}
}

void printAns(int * numbers) {
	for (int i = 0; i < 10; i++) {
		for (int j = 0; j < numbers[i]; j++) {
			printf("%d", i);
		}
	}
	printf("\n");
}

bool search(int *letters, int *numbers, int curr) {
	
	// printf("search, curr = %d\n", curr);
	// for (int i = 0; i < 10; i++) {
	// 	printf("%d", numbers[i]);
	// }
	// printf("\n");
	
	if (curr >= 10) {
		if (isPerfect(letters)) {
			//printf("isPerfect!\n");
			printAns(numbers);
			return true;
		} else {
			return false;
		}
	}
	bool valid = true;
	while (valid) {
		if (search(letters, numbers, curr + 1)) {
			// printf("search returns true, curr = %d, num = %d\n", curr, numbers[curr]);
			return true;
		}
		for (int i = curr + 1; i < 10; i++) {
			adjustLetters(letters, i, numbers[i]);
			numbers[i] = 0;
		}
		numbers[curr]++;
		adjustLetters(letters, curr, -1);
		if (!isValid(letters)) {
			// printf("notValid, curr = %d, num = ", curr, numbers[curr]);
			// for (int i = 0; i < 10; i++) {
			// 	printf("%d", numbers[i]);
			// }
			// printf("\n");
			
			adjustLetters(letters, curr, 1);
			numbers[curr]--;
			valid = false;
		}

	}
	return false;
}

// pushes letter into alphabet
void p(int num, char letter) {
	alphabet[((int)letter) - 65][num]++;
}

int main() {
	memset(alphabet, 0, sizeof(alphabet));
	//nums[0] = "ZERO";
	for (int i = 0; i < 10; i++) {
		for (int j = 0; j < strlen(nums[i]); j++) {
			p(i, nums[i][j]);
		}
	}
	
	int T;
	scanf("%d", &T);
	for (int cases = 1; cases <= T; cases++) {
		char s[2010];
		scanf("%s", &s);
		int letters[26];
		memset(letters, 0, sizeof(letters));
		int numbers[10];
		memset(numbers, 0, sizeof(numbers));
		for (int i = 0; i < strlen(s); i++) {
			letters[((int)s[i]) - 65]++;
		}
		printf("Case #%d: ", cases);
		search(letters, numbers, 0);
	}
	
	return 0;
}