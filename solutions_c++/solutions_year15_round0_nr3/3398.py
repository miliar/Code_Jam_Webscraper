#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

#define LMAX 10005
#define SMAX 10005

int l, x;
char str[SMAX];
int dp[SMAX];

int multiply(int a, int b) {
	if (a < 0 && b < 0)
		return multiply(abs(a), abs(b));
	else if (a < 0 || b < 0)
		return -1 * multiply(abs(a), abs(b));

	if (a == 1) {
		if (b == 1)
			return 1;
		else if (b == 2)
			return 2;
		else if (b == 3)
			return 3;
		else
			return 4;
	}
	else if (a == 2) {
		if (b == 1)
			return 2;
		else if (b == 2)
			return -1;
		else if (b == 3)
			return 4;
		else
			return -3;
	}
	else if (a == 3) {
		if (b == 1)
			return 3;
		else if (b == 2)
			return -4;
		else if (b == 3)
			return -1;
		else
			return 2;
	}
	else if (a == 4) {
		if (b == 1)
			return 4;
		else if (b == 2)
			return 3;
		else if (b == 3)
			return -2;
		else
			return -1;
	}
}

int d(int i) {
	char c = str[i];
	if (c == 'i')
		return 2;
	if (c == 'j')
		return 3;
	return 4;
}

bool solve() {
	memset(dp, -1, sizeof dp);

	int current = 1;
	for (int i = 0; i < l * x; i++) {
		current = multiply(current, d(i));
	}

	if (current != -1)
		return false;

	current = 1;
	for (int i = l * x - 1; i >= 0; i--) {
		current = multiply(d(i), current);
		dp[i] = current;
	}

	bool res = false;
	int currenti = 1;
	for (int i = 0; i < l * x && !res; i++) {
		currenti = multiply(currenti, d(i));

		if (currenti == 2) {
			int currentj = 1;
			for (int j = i + 1; j < l * x + 1 && !res; j++) {
				currentj = multiply(currentj, d(j));

				if (currentj == 3 && dp[j + 1] == 4) {
					res = true;
				}
			}
		}
	}

	return res;
}

int main() {
	int t;
	scanf("%d", &t);
	for (int ctest = 1; ctest <= t; ctest++) {
		scanf("%d %d %s", &l, &x, str);
		for (int k = 1; k < x; k++) {
			for (int i = 0; i < l; i++) {
				str[l * k + i] = str[i];
			}
		}
		str[l * x] = '\0';

		printf("Case #%d: %s\n", ctest, solve() ? "YES" : "NO");
	}
	
	return 0;
}
