#include <bits/stdc++.h>
using namespace std;

void handle_case(int case_num) {
	while (true) {
		char c = fgetc(stdin);
		if (c == '-' || c == '+') {
			ungetc(c, stdin);
			break;
		}
	}

	char last = 0;
	char curr = 0;
	int n_sign_changes = 0; // Excluding a tail of '+'.
	while (true) {
		last = curr;
		curr = fgetc(stdin);

		if (curr != '-' && curr != '+') {
			ungetc(curr, stdin);
			break;
		}

		if (last != 0 && curr != last) {
			n_sign_changes++;
		}
	}

	if (last == '+')
		n_sign_changes--;

	printf("%d", n_sign_changes + 1);
}

int main(void) {
	int n_cases;
	scanf(" %d", &n_cases);
	for (int case_num = 1; case_num <= n_cases; case_num++) {
		printf("Case #%d: ", case_num);
		handle_case(case_num);
		printf("\n");
	}

	return 0;
}
