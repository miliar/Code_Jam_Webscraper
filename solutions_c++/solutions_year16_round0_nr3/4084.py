#include <iostream>

using namespace std;

long long int pw[11][32];
char notprime[101010];
long long int primear[50101];

void printbit(long long int bit) {
	if (bit) {
		printbit(bit >> 1);
		cout << bit % 2;
	}
}

int main() {
	freopen("C-small-attempt2.in", "r", stdin);
	freopen("C-small-attempt2.out", "w", stdout);
	for (int i = 2; i <= 10; i++) pw[i][0] = 1;
	for (int i = 2; i <= 10; i++) {
		for (int j = 1; j < 32; j++) {
			pw[i][j] = pw[i][j - 1] * i;
		}
	}
	for (int i = 2; i < 101010; i++) {
		if (notprime[i] == 0) {
			for (int j = i * 2; j < 101010; j += i) {
				notprime[j] = 1;
			}
		}
	}
	int primecnt = 0;
	for (int i = 2; i < 101010; i++) {
		if (notprime[i] == 0) {
			primear[primecnt++] = i;
		}
	}
	int tc;
	cin >> tc;
	for (int i = 1; i <= tc; i++) {
		cout << "Case #" << i << ":" << endl;
		int n, j;
		cin >> n >> j;
		long long int bit = ((long long int)1 << (n - 1)) + 1;

		for (long long int i = 0; j; i++) {
			long long int coin = bit | (i << 1);
			long long int div[11];
			bool flag = true;
			for (int base = 2; base <= 10; base++) {
				long long int num = 0;
				long long int digit = 0;
				long long int cp_coin = coin;
				while (cp_coin) {
					if (cp_coin % 2) {
						num += pw[base][digit];
					}
					digit++;
					cp_coin >>= 1;
				}

				bool fflag = false;
				for (int i = 2; i < primecnt; i++) {
					if (num % primear[i] == 0 && num > primear[i]) {
						div[base] = primear[i];
						fflag = true;
					}
				}
				if (fflag == false) {
					flag = false;
				}
			}

			if (flag) {
				j--;
				printbit(coin);
				cout << " ";
				for (int i = 2; i <= 10; i++) {
					cout << div[i] << " ";
				}
				cout << endl;
			}
		}
	}
}