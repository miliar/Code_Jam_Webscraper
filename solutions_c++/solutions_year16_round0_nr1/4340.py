#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

inline bool all_appeared(bool* appeared) {
	for (int i = 0; i < 10; i++)
		if (!appeared[i]) return false;
	return true;
}

inline void calculate_digits(bool* appeared, int n) {
	while (n > 0) {
		appeared[n%10] = true;
		n /= 10;
	}
}

int main() {


	freopen("A-large.in", "r", stdin);
	freopen("sol.out", "w", stdout);

	int T; cin >> T;
	for (int test = 1; test <= T; test++) {
		int n; cin >> n;
		if (n == 0) {
			cout << "Case #" << test << ": INSOMNIA" << endl;
			continue;
		}
		bool appeared[10];
		memset(appeared, 0, sizeof(appeared));

		int i;
		for (i = 1; !all_appeared(appeared); i++) 
			calculate_digits(appeared, i * n);

		cout << "Case #" << test << ": " << (i-1)* n << endl;
	}
}