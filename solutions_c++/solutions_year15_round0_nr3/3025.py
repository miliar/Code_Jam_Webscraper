#include <iostream>
using namespace std;
int I = 2, J = 3, K = 4;

int decode(char c) {
	if (c == 'i')
		return I;
	if (c == 'j')
		return J;
	return K;
}

int times(int a, int b) {
	int sign = a < 0 ? -1 : 1;
	a = abs(a);
	if (a == 1) {
		if (b == I)
			return sign * I;
		if (b == J)
			return sign * J;
		return sign * K;
	} else if (a == I) {
		if (b == I)
			return sign * -1;
		else if (b == J)
			return sign * K;
		else return -sign * J;
	} else if (a == J) {
		if (b == I) return -sign * K;
		else if (b == J) return -sign;
		else return sign * I;
	} else {
		if (b == I) return sign * J;
		else if (b == J) return -sign * I;
		else return -sign;
	}
}

int main() {
	int cs;
	cin >> cs;
	for (int cc = 1; cc <= cs; cc++) {
		int l, x;
		string o;
		cin >> l >> x >> o;
		string s;
		for (int i = 0; i < x; i++)
			s += o;
		int r = 1;
		int p = 0;
		bool f = true;
		//cout << s << "\n";
		for (; p < s.size(); p++) {
			r = times(r, decode(s[p]));
			if (r == I) {
				p++;
				break;
			}
		}
		//cout << p << "\n";
		if (p >= s.size())
			f = false;
		r = 1;
		for (; p < s.size(); p++) {
			r = times(r, decode(s[p]));
			if (r == J) {
				p++;
				break;
			}
		}
		//cout << p << "\n";
		if (p >= s.size())
			f = false;
		r = 1;
		for (; p < s.size(); p++) {
			r = times(r, decode(s[p]));
		}
		if (r != K)
			f = false;
		cout << "Case #" << cc << ": " << (f ? "YES" : "NO") << "\n";
	}
}
