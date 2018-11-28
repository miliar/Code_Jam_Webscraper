
#include <iostream>

using namespace std;

const char I = 2;
const char J = 3;
const char K = 4;

char trans(char x) {
	if (x == 'i') return I;
	if (x == 'j') return J;
	if (x == 'k') return K;
}

char mul(char a, char b) {
	if (a == 1) return b;
	if (a == -1) return -b;
	if (b == 1) return a;
	if (b == -1) return -a;
	if (a == b) return -1;
	if (a == -b) return 1;

	char sa = 1, aa = a, sb = 1, bb = b;
	if (a < 0) {
		sa = -1;
		aa = -a;
	}
	if (b < 0) {
		sb = -1;
		bb = -b;
	}
	if (aa == I) {
		if (bb == J) {
			return sa * sb * K;
		} else { // b == K
			return - sa * sb * J;
		}
	} else if (aa == J) {
		if (bb == I) {
			return - sa * sb * K;
		} else { // bb == K
			return sa * sb * I;
		}
	} else { // a == K
		if (bb == I) {
			return sa * sb * J;
		} else { // bb == J
			return - sa * sb * I;
		}
	}
}

void shift(char &a, char &b, char by) {
	a = mul(a, by);
	b = mul(-by, b);
}

bool poss(const char *s, int len) {
	char beg = 1;
	char rest = 1;
	for (int i = 0; i < len; i++) rest = mul(rest, s[i]);
	
	for (int i = 0; i < len; i++) {
		shift(beg, rest, s[i]);
		//cout << "beg = " << ((int)beg) << endl;
		if (beg == I) {
			char mid = 1;
			char end = rest;
			for (int j = i+1; j < len-1; j++) {
				shift(mid, end, s[j]);
				//cout << "mid = " << ((int)mid) << endl;
				if (mid == J && end == K) {
					//cout << "possible with " << i << " " << j << endl;
					return true;
				}
			}
		}
	}
	return false;
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int L, X;
		cin >> L >> X;
		char *base = new char[L+1];
		cin >> base;
		for (int l = 0; l < L; l++) base[l] = trans(base[l]);
		char *str = new char[L*X+1];
		str[L*X] = 0;
		for (int x = 0; x < X; x++) {
			for (int l = 0; l < L; l++) {
				str[x * L + l] = base[l];
			}
		}

		cout << "Case #" << t << ": ";
		bool p = poss(str, L * X);
		if (p) cout << "YES"; else cout << "NO";
		cout << endl;
	}
}

