#include <bits/stdc++.h>
using namespace std;

#define ARRAY_LEN(array) (sizeof(array) / sizeof(*array))
#define SIZEOF_MEMBER(type, member) (sizeof(((type *) NULL)->member))

template <typename T> T gcd(T x, T y) { return y == 0 ? x : gcd(y, x % y); }
int ffs(long long x) { return __builtin_ffsll(x); } // Find First Set -- 1 + index of the rightmost 1-bit; 0 if all bits are 0.
int popcount(long long x) { return __builtin_popcountll(x); } // Count the number of 1-bits.

typedef int64_t Num;
//typedef __int128 num;
#define PRINUM PRId64
#define SCANUM SCNd64

bool debug = true;
#define DEBUG_WRAP(...) \
	do { if (debug) { \
			fflush(stdout); \
			fprintf(stderr, "[D] %s:%d:%s: ", __FILE__, __LINE__, __func__); \
			__VA_ARGS__; \
			fflush(stderr); \
		} } while(0)
#define DEBUG(fmt, ...) DEBUG_WRAP(fprintf(stderr, fmt "\n", ##__VA_ARGS__))
#define DUMP(expr) DEBUG_WRAP(cerr << #expr << " = " << (expr) << "\n")

void freqs_minus(int *freqs, const char *string) {
	for (int i = 0; i < strlen(string); i++) {
		freqs[string[i]]--;
	}
}

void handle_digit(int *letters, int *digits, int digit, char check_letter, const char *digit_str) {
	while (letters[check_letter] > 0) {
		freqs_minus(letters, digit_str);
		digits[digit]++;
	}
}

void handle_case(int case_num) {
	char line[2048];
	fgets(line, sizeof(line), stdin);

	int letters[256] = {};

	for (int i = 0; i < strlen(line); i++) {
		letters[line[i]]++;
	}

	int digits[10] = {};

	handle_digit(letters, digits, 0, 'Z', "ZERO");
	handle_digit(letters, digits, 2, 'W', "TWO");
	handle_digit(letters, digits, 4, 'U', "FOUR");
	handle_digit(letters, digits, 6, 'X', "SIX");
	handle_digit(letters, digits, 8, 'G', "EIGHT");

	handle_digit(letters, digits, 1, 'O', "ONE");
	handle_digit(letters, digits, 3, 'H', "THREE");
	handle_digit(letters, digits, 5, 'F', "FIVE");
	handle_digit(letters, digits, 7, 'S', "SEVEN");

	handle_digit(letters, digits, 9, 'I', "NINE");

	for (int digit = 0; digit < 10; digit++) {
		for (int j = 0; j < digits[digit]; j++) {
			printf("%d", digit);
		}
	}
}

int main(void) {
	char n_cases_str[64];
	fgets(n_cases_str, sizeof(n_cases_str), stdin);
	int n_cases;
	sscanf(n_cases_str, " %d ", &n_cases);

	for (int case_num = 1; case_num <= n_cases; case_num++) {
		printf("Case #%d: ", case_num);
		handle_case(case_num);
		printf("\n");
	}

	return 0;
}
