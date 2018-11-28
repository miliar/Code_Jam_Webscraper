#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

struct Node {
	int IDX;
	int idx;
};

class Solution {
public:
	const static int CHAR_MAX = 10000+10;
	long long min(long long a, long long b) {
		return a < b ? a : b;
	}
	char multiply(char m1, char m2, int &sign) {
		char table[4][4] = {
				{'1', 'i', 'j', 'k'},
				{'i', '1', 'k', 'j'},
				{'j', 'k', '1', 'i'},
				{'k', 'j', 'i', '1'}
		};
		int idx1 = get_idx(m1);
		int idx2 = get_idx(m2);
		sign = 1;
		if (idx1 == idx2 && idx1 != 0) sign = -1;
		else if (idx1 == 1 && idx2 == 3) sign = -1;
		else if (idx1 == 2 && idx2 == 1) sign = -1;
		else if (idx1 == 3 && idx2 == 2) sign = -1;
		return table[idx1][idx2];
	}
	int get_idx(char m1) {
		int idx1 = 0;
		switch(m1) {
		case '1':
			idx1 = 0; break;
		case 'i':
			idx1 = 1; break;
		case 'j':
			idx1 = 2; break;
		case 'k':
			idx1 = 3; break;
		}
		return idx1;
	}
	char divide(char x1, int x1_sign, char x2, int x2_sign, int &sign) {
		// x2 / x1

		char U[] = {'1', 'i', 'j', 'k'};
		for (int s = -1; s <= 1; s+=2) {
			for (int idx = 0; idx <= 3; idx++) {
				char ans = U[idx];
				int tmp_sign;
				if (multiply(x1, ans, tmp_sign) == x2 && tmp_sign * x1_sign * s == x2_sign) {
					sign = s;
					return ans;
				}
			}
		}
		printf("this is not possible\n");
		return '0';
	}
	void test() {
		int sign;
		char res = divide ('i', 1, 'i', -1, sign);
		printf("%c %d\n", res, sign);
	}
	bool check_right(long long X, long long L, char *str) {
		// X times repeating
		// L the length of str
		vector<long long> left, right;

		// multiply_left [0, i], multiply_right: [i, L-1];
		char multiply_left[CHAR_MAX], multiply_right[CHAR_MAX];
		int sign_left[CHAR_MAX], sign_right[CHAR_MAX];
		for (int i = 0; i < L; i++) {
			if (i == 0) {
				multiply_left[i] = str[i];
				sign_left[i] = 1;
				multiply_right[L-1-i] = str[L-1-i];
				sign_right[L-1-i] = 1;
			}
			else {
				multiply_left[i] = multiply(multiply_left[i-1], str[i], sign_left[i]);
				sign_left[i] *= sign_left[i-1];
				multiply_right[L-1-i] = multiply(str[L-1-i], multiply_right[L-1-i+1], sign_right[L-1-i]);
				sign_right[L-1-i] *= sign_right[L-1-i+1];
			}
		}
		char left_previous_char = '1';
		char right_previous_char = '1';
		int left_previous_sign = 1;
		int right_previous_sign = 1;
		for (long long i = 0; i < min(4, X) * L; i++){
			int left_s;
			left_previous_char = multiply(left_previous_char, str[i % L], left_s);
			left_previous_sign *= left_s;
			if (left_previous_sign == 1 && left_previous_char == 'i')
				left.push_back(i);

			int right_s;
			right_previous_char = multiply(str[(L*X - 1 - i)%L], right_previous_char, right_s);
			right_previous_sign *= right_s;
			if (right_previous_sign == 1 && right_previous_char == 'k')
				right.push_back(L*X - 1 -i);
		}
//		for (int i = 0; i < left.size(); i++) printf("%d ", left[i]); printf("\n");
//		for (int i = 0; i < right.size(); i++) printf("%d ", right[i]); printf("\n");
		for (int i = 0; i < left.size(); i++) {
			for (int j = 0; j < right.size(); j++) {
//				printf("i:%d, j:%d\n", i, j);
				if (left[i] >= right[j]) break;
				// check middle
				if (right[j]-1-left[i] <= L) {
					char middle = '1'; int middle_sign = 1;
//					for (int idx = left[i]+1; idx < right[j]; idx++) {
//						int s_tmp;
//						middle = multiply(middle, str[idx % L], s_tmp);
//						middle_sign *= s_tmp;
//					}
					char middle_bak = middle; int middle_sign_bak = middle_sign;

					middle = '1'; middle_sign = 1;

					char x1 = '1'; int x1_sign = 1;
					if ((left[i]+1)%L > 0) {
						x1 = multiply_left[(left[i])%L]; x1_sign = sign_left[(left[i])%L];
					}
					char x2 = '1'; int x2_sign = 1;
					if ((right[j]-1)%L > 0) {
						x2 = multiply_left[(right[j]-1)%L]; x2_sign = sign_left[(right[j]-1)%L];
					}
					middle = divide(x1, x1_sign, x2, x2_sign, middle_sign);

//					if (middle != middle_bak || middle_sign != middle_sign_bak) {
//						printf("x1:%c, x1_sign:%d, x2:%c, x2_sign:%d, middle_sign:%d\n", x1, x1_sign, x2, x2_sign, middle_sign);
//						printf("Oh shit middle_bak:%c, middle_sign_bak:%d, middle:%c, middle_sign:%d\n", middle_bak, middle_sign_bak, middle, middle_sign);
//						return false;
//					}

					if (middle_sign == 1&& middle == 'j') return true;
					else continue;
				}

				char m1 = multiply_right[(left[i]+1)%L]; int m1_sign = sign_right[(left[i]+1)%L];
				char m2 = multiply_left[(right[j]-1+L)%L]; int m2_sign = sign_left[(right[j]-1+L)%L];
				int m1_IDX = (left[i]+1)/L; int m2_IDX = (right[j]-1)/L;
				char mid = '1'; int mid_sign = 1; int mid_sign_tmp;
				mid = multiply(mid, m1, mid_sign_tmp); mid_sign *= mid_sign_tmp; mid_sign *= m1_sign;
				for (int idx=0; idx < (m2_IDX-m1_IDX-1)%4; idx++){
					mid = multiply(mid, multiply_left[L-1], mid_sign_tmp);
					mid_sign *= mid_sign_tmp;
					mid_sign *= sign_left[L-1];
				}
				mid = multiply(mid, m2, mid_sign_tmp);
				mid_sign *= mid_sign_tmp;
				mid_sign *= m2_sign;
				if (mid == 'j' && mid_sign == 1) return true;
				else continue;
			}
		}
		return false;
	}
	void solve() {
		int Tcase;
		char str[CHAR_MAX];
		long long X, L;
		scanf("%d", &Tcase);
		for (int t = 1; t <= Tcase; t++) {
			scanf("%lld%lld", &L, &X);
			scanf("%s", &str);
//			printf("%lld %lld %s\n", L, X, str);
			bool ok = check_right(X, L, str);
			printf("Case #%d: ", t);
			printf(ok ? "YES\n" : "NO\n");
		}
	}
};

class No4 {
public:
	bool win(int x, int r, int c) {
		if (x == 1) return false;
		if (x == 2) {
			if (r * c % 2 == 0) return false;
			return true;
		}
		if (x == 3) {
			if (r * c % 3 != 0) return true;
			if (r*c == 3) return true;
			if (r*c == 6) return false;
			if (r*c == 9) return false;
			if (r*c == 12) return false;
			if (r*c == 15) return false;
		}
		if (x == 4) {
			if (r*c % 4 != 0) return true;
			if (r*c == 4) return true;
			if (r*c == 8) return true;
			if (r*c == 12) {
				if (r == 3 || c == 3)
					return false;
				else return true;// r = 2, c = 6
			}
			if (r*c == 16) {
				if (r == 4 || c == 4)
					return false;
				else return true; // 2 * 8, must win
			}
		}
	}
	void solve() {
		int X, R, C;
		int Tcase;
		scanf("%d", &Tcase);
		for (int t = 1; t <= Tcase; t++) {
			scanf("%d%d%d", &X, &R, &C);
			if (win(X, R, C)) printf("Case #%d: RICHARD\n", t);
			else printf("Case #%d: GABRIEL\n", t);
		}
	}
};

int main() {
	No4 solution;
	solution.solve();
	return 0;
}
