#include <iostream>
#include <string.h>
#include <cstdio>
using namespace std;

char m[50000][51 + 1];
char q[50000][102 + 1];
int c[50000];
int s[50 + 1];
char A[102+1];
char B[102+1];
int n;


int count_Large() {
	int cnt = 0;

	int Alen = strlen(A);
	int Blen = strlen(B);
	memmove(A+ 102 - Alen, A, Alen+1);
	memmove(B+ 102 - Blen, B, Blen+1);
	memset(A, '0', 102 - Alen);
	memset(B, '0', 102 - Blen);

	for(int i=0; i<n; i++) {
		if (strcmp(A, q[i]) <= 0 && strcmp(q[i], B) <= 0) {
			cnt++;
		}
	}
	return cnt;
}

int main() {

	s[1] = 1;
	memcpy(m[1], "1", sizeof("1"));
	memcpy(m[2], "2", sizeof("2"));
	memcpy(m[3], "3", sizeof("3"));
	c[1] = 1;
	c[2] = 4;
	c[3] = 9;


	s[2] = 4;
	memcpy(m[4], "11", sizeof("11"));
	memcpy(m[5], "22", sizeof("22"));
	c[4] = 2;
	c[5] = 8;

	s[3] = 6;
	memcpy(m[6], "101", sizeof("101"));
	memcpy(m[7], "111", sizeof("111"));
	memcpy(m[8], "121", sizeof("121"));
	memcpy(m[9], "202", sizeof("202"));
	memcpy(m[10], "212", sizeof("212"));
	c[6] = 2;
	c[7] = 3;
	c[8] = 6;
	c[9] = 8;
	c[10] = 9;

	n = 11;

	for (int i = 4; i <= 50; i+=2) {
		s[i] = n;
		for (int j = s[i-2]; j < s[i-1]; j++) {
			strcpy(m[n], m[j]);
			memmove(m[n] + (i/2) + 1, m[n] + (i/2) - 1, (i/2) - 1);
			memset(m[n] + (i/2) - 1, '0', 2);
			c[n] = c[j];
			n++;

			if (c[j] + 2 < 10) {
				strcpy(m[n], m[j]);
				memmove(m[n] + (i/2) + 1, m[n] + (i/2) - 1, (i/2) - 1);
				memset(m[n] + (i/2) - 1, '1', 2);
				c[n] = c[j] + 2;
				n++;
			}
		}

		s[i+1] = n;
		for (int j = s[i]; j < s[i+1]; j++) {
			strcpy(m[n], m[j]);
			memmove(m[n] + (i/2) + 1, m[n] + (i/2), (i/2));
			memset(m[n] + (i/2), '0', 1);
			c[n] = c[j];
			n++;

			if (c[j] + 1 < 10) {
				strcpy(m[n], m[j]);
				memmove(m[n] + (i/2) + 1, m[n] + (i/2), (i/2));
				memset(m[n] + (i/2), '1', 1);
				c[n] = c[j] + 1;
				n++;
			}

			if (c[j] + 4 < 10) {
				strcpy(m[n], m[j]);
				memmove(m[n] + (i/2) + 1, m[n] + (i/2), (i/2));
				memset(m[n] + (i/2), '2', 1);
				c[n] = c[j] + 4;
				n++;
			}
		}

	}

	for (int k = 1; k < n; k++) {
		int l = strlen(m[k]);
		for (int i = 0; i < l; i++) {
			for (int j = 0; j < l; j++) {
				q[k][i + j] += ((m[k][i] - '0') * (m[k][j] - '0'));
			}
		}

		for (int j = 0; j < 2 * l - 1; j++) {
			q[k][j] += (char) '0';
		}

		q[k][l * 2] = '\0';
		memmove(q[k]+ 102 - (l*2-1) , q[k], (l*2));
		memset(q[k], '0', 102 - (l*2-1));
	}

	int T;
	cin >> T;
	for (int i=1; i<=T; i++) {
		cin >> A >> B;
		cout << "Case #" << i << ": " << count_Large() << endl;
	}

	return 0;
}
