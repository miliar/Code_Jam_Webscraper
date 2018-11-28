#include <bits/stdc++.h>
using namespace std;

char S[2001];
const char *NUM[] = {
	"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
};

void fun(int n, char c, int* nums, int* latin) {
	nums[n] = latin[c - 'A'];
	for (const char* p = NUM[n]; *p; ++p) latin[*p - 'A'] -= nums[n];
}

void solve() {
	scanf("%s", S);

	int latin[26] = {0};
	for (char* p = S; *p; ++p) ++latin[*p - 'A'];

	int nums[10] = {0};

	fun(0, 'Z', nums, latin);
	fun(2, 'W', nums, latin);
	fun(4, 'U', nums, latin);
	fun(6, 'X', nums, latin);
	fun(8, 'G', nums, latin);

	fun(3, 'R', nums, latin);
	fun(5, 'F', nums, latin);
	fun(7, 'S', nums, latin);

	fun(1, 'O', nums, latin);
	fun(9, 'I', nums, latin);

	for (int i = 0; i < 10; ++i) while (nums[i]--) printf("%d", i);
	puts("");
}

int main() {
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i) {
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}
