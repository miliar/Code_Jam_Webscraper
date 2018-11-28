#include <bits/stdc++.h>
using namespace std;
void iosInit() {ios_base::sync_with_stdio(false); cin.tie(nullptr);}

bool isok(char* s) {
	while (*s) {
		if (*s++ == '-') return false;
	}
	return true;
}

char toreverse(char c) {
	return c == '+' ? '-' : '+';
}

void flip_pancakes(char* begin, char* end) {
	for (char *p = begin; p < end; ++p) {
		*p = toreverse(*p);
	}
	reverse(begin, end);
}

char* find_gap(char* s) {
	++s;
	while (*(s - 1) == *s) ++s;
	return s;
}

int solve(char* S) {
	int res = 0;
	while (!isok(S)) {
		flip_pancakes(S, find_gap(S));
		++res;
	}
	return res;
}

int main() {
	int T;
	char S[101];
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i) {
		scanf("%s", S);
		printf("Case #%d: %d\n", i, solve(S));
	}
	return 0;
}
