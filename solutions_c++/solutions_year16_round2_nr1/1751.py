# include <stdio.h>
# include <string.h>
# include <stdlib.h>
# include <deque>

using namespace std;

int main() {
	freopen("a.txt", "r", stdin);
	freopen("b.txt", "w", stdout);

	int t;
	scanf("%d", &t);

	for (int kase = 1; kase <= t; kase ++) {
		printf("Case #%d: ", kase);

		char s[2005];

		scanf("%s%*c", s);

		int len = strlen(s);
		int hash[30];
		memset(hash, 0, sizeof(hash));
		for (int i = 0; i < len; i ++) {
			hash[s[i] - 'A'] ++;
		}

		int phone[10];
		memset(phone, 0, sizeof(phone));
		// 0
		while (hash['Z' - 'A'] != 0) {
			hash['Z' - 'A'] --;
			hash['E' - 'A'] --;
			hash['R' - 'A'] --;
			hash['O' - 'A'] --;
			phone[0] ++;
		}

		// 2
		while (hash['W' - 'A'] != 0) {
			hash['T' - 'A'] --;
			hash['W' - 'A'] --;
			hash['O' - 'A'] --;
			phone[2] ++;
		}

		// 6
		while (hash['X' - 'A'] != 0) {
			hash['S' - 'A'] --;
			hash['I' - 'A'] --;
			hash['X' - 'A'] --;
			phone[6] ++;
		}

		// 8
		while (hash['G' - 'A'] != 0) {
			hash['E' - 'A'] --;
			hash['I' - 'A'] --;
			hash['G' - 'A'] --;
			hash['H' - 'A'] --;
			hash['T' - 'A'] --;
			phone[8] ++;
		}

		// 3
		while (hash['H' - 'A'] != 0) {
			hash['T' - 'A'] --;
			hash['H' - 'A'] --;
			hash['R' - 'A'] --;
			hash['E' - 'A'] --;
			hash['E' - 'A'] --;
			phone[3] ++;
		}

		// 4
		while (hash['R' - 'A'] != 0) {
			hash['F' - 'A'] --;
			hash['O' - 'A'] --;
			hash['U' - 'A'] --;
			hash['R' - 'A'] --;
			phone[4] ++;
		}

		// 5
		while (hash['F' - 'A'] != 0) {
			hash['F' - 'A'] --;
			hash['I' - 'A'] --;
			hash['V' - 'A'] --;
			hash['E' - 'A'] --;
			phone[5] ++;
		}

		// 7
		while (hash['V' - 'A'] != 0) {
			hash['S' - 'A'] --;
			hash['E' - 'A'] --;
			hash['V' - 'A'] --;
			hash['E' - 'A'] --;
			hash['N' - 'A'] --;
			phone[7] ++;
		}

		// 9
		while (hash['I' - 'A'] != 0) {
			hash['N' - 'A'] --;
			hash['I' - 'A'] --;
			hash['N' - 'A'] --;
			hash['E' - 'A'] --;
			phone[9] ++;
		}

		// 1
		while (hash['O' - 'A'] != 0) {
			hash['O' - 'A'] --;
			hash['N' - 'A'] --;
			hash['E' - 'A'] --;
			phone[1] ++;
		}

		for (int i = 0; i < 10; i ++) {
			while (phone[i]) {
				phone[i]--;
				printf("%d", i);
			}
		}

		printf("\n");
	}
}