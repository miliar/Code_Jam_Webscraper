#include <bits/stdc++.h>
using namespace std;

struct Quad {
	static const char mulVal[4][4];
	static const bool mulNeg[4][4];
	bool isNegative;
	char val;
	Quad() : val('h'), isNegative(false) {}
	Quad(char c) : val(c), isNegative(false) {}
	Quad(char c, bool pos) : val(c), isNegative(pos) {}
	Quad operator*(const Quad &q) const {
		char a = this->val - 'h', b = q.val - 'h';
		return Quad(Quad::mulVal[a][b], Quad::mulNeg[a][b] ^ this->isNegative ^ q.isNegative);
	}
	bool operator==(const Quad &q) const {
		return this->val == q.val && this->isNegative == q.isNegative;
	}
};

const char Quad::mulVal[4][4] = {{'h', 'i', 'j', 'k'},
								{'i', 'h', 'k', 'j'},
								{'j', 'k', 'h', 'i'},
								{'k', 'j', 'i', 'h'}};
const bool Quad::mulNeg[4][4] = {{0, 0, 0, 0},
								{0, 1, 0, 1},
								{0, 1, 1, 0},
								{0, 0, 1, 1}};

Quad binexp(Quad q, int x) {
	if (x == 1) {
		return q;
	}
	Quad r = binexp(q, x / 2);
	r = r * r;
	if (x & 1) {
		r = r * q;
	}
	return r;
}

int main() {
	int T, t;
	int l, x;
	string s;
	cin.tie(0);
	ios_base::sync_with_stdio(0);
	cin >> T;
	for (t = 1; t <= T; t++) {
		cin >> l >> x >> s;
		Quad q, r;
		//My head hurts. I promise to do this properly later.
		int i = 0;
		string u;
		while (x--) {
			u += s;
		}
		for (char c : u) {
			q = q * Quad(c);
			if (i == 0) {
				if (q == Quad('i')) {
					i++;
				}
			} else if (i == 1) {
				if (q == Quad('i') * Quad('j')) {
					i++;
				}
			}
		}
		r = q;
		/*
		for (char c : s) {
			q = q * Quad(c);
		}
		/*
		while (x--) {
			r = r * q;
		}
		r = binexp(q, x); 
		*/
		cout << "Case #" << t << ": " << (i == 2 && r == (Quad('i') * Quad('j') * Quad('k')) ? "YES\n" : "NO\n");
	}
	return 0;
}