#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

string digits[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int order[] = {0, 2, 6, 7, 4, 5, 1, 9, 8, 3};
int amount[300];
char S[3000];
int res[30];

void read(){
	scanf("%s", S);
}

void process() {
	memset(amount, 0, sizeof(amount));

	for (int i = 0; S[i]; i++) {
		amount[S[i]]++;
	}

	for (int i = 0; i < 10; i++) {
		int digit = order[i];
		res[digit] = 0;

		bool failed = false;
		while (!failed) {
			for (int j = 0; j < digits[digit].size(); j++) {
				if (amount[digits[digit][j]] > 0) {
					amount[digits[digit][j]]--;
				} else {
					failed = true;
					for (int k = 0; k < j; k++) {
						amount[digits[digit][k]]++;
					}
					break;
				}
			}
			if (!failed) {
				res[digit]++;
			}
		}
	}
	for (int i = 0; i < 10; i++) {
		while (res[i] > 0) {
			printf("%d", i);
			res[i]--;
		}
	}
	printf("\n");
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