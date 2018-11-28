#include <bits/stdc++.h>
#include <stdint.h>
using namespace std;

typedef uint8_t byte;
typedef int16_t i16;
typedef uint16_t ui16;
typedef int32_t i32;
typedef uint32_t ui32;
typedef int64_t i64;
typedef uint64_t ui64;

#define MOD 1000000007
#define ADD_MOD(a, b) (((a) + (b)) % MOD)
#define MUL_MOD(a, b) i32((i64(a) * i64(b)) % MOD)
#define SUB_MOD(a, b) ((a) >= (b) ? (a) - (b) : (a) + MOD - (b))

struct quat {
	char c = 1;
	int sign = 1;

	quat() {}

	quat(char c, int sign)
		: c(c)
		, sign(sign) {}

	void mul(quat &a) {
		sign *= a.sign;

		if (a.c == 1) {
			return;
		}

		switch (c) {
		case 1:
			c = a.c;
			return;

		case 'i':
			switch (a.c) {
			case 'i':
				c = 1;
				sign *= -1;
				return;
			case 'j':
				c = 'k';
				return;
			case 'k':
				c = 'j';
				sign *= -1;
				return;
			}
			break;

		case 'j':
			switch (a.c) {
			case 'i':
				c = 'k';
				sign *= -1;
				return;
			case 'j':
				c = 1;
				sign *= -1;
				return;
			case 'k':
				c = 'i';
				return;
			}
			break;

		case 'k':
			switch (a.c) {
			case 'i':
				c = 'j';
				return;
			case 'j':
				c = 'i';
				sign *= -1;
				return;
			case 'k':
				c = 1;
				sign *= -1;
				return;
			}
			break;
		}
		throw 1;
	}

	bool check(char c, int sign) {
		return this->c == c && this->sign == sign;
	}
};

bool contains(vector<int>& v, int val) {
	return binary_search(v.begin(), v.end(), val);
}

bool check_sign(string &s, size_t l, size_t len, int i) {
	quat acc;
	for (; i < len; ++i) {
		quat ch(s[i % l], 1);
		acc.mul(ch);
	}
	return acc.sign == 1;
}

int main() {
	ios_base::sync_with_stdio(false);

	size_t testCount;
	cin >> testCount;

	for (size_t testIndex = 0; testIndex < testCount; ++testIndex) {
		size_t l, x;
		cin >> l >> x;

		string s;
		cin >> s;

		size_t len = l * x;

		vector<int> is;
		vector<int> ks;

		quat acc;
		for (size_t i = 0; i < len; ++i) {
			quat ch(s[i % l], 1);
			acc.mul(ch);

			if (acc.check('i', 1)) {
				is.push_back(i);
			}
		}

		acc.c = 1; acc.sign = 1;
		for (int i = len - 1; i >= 0; --i) {
			quat ch(s[i % l], 1);
			acc.mul(ch);

			if (acc.c == 'k' && check_sign(s, l, len, i)) {
				ks.push_back(i);
			}
		}
		reverse(ks.begin(), ks.end());

		cout << "Case #" << testIndex + 1 << ": ";
		if (is.size() == 0 || ks.size() == 0) {
			cout << "NO" << endl;
		} else {
			bool found = false;

			for (int i : is) {
				acc.c = 1; acc.sign = 1;
				for (i = i + 1; i < len; ++i) {
					quat ch(s[i % l], 1);
					acc.mul(ch);

					if (acc.check('j', 1) && contains(ks, i + 1)) {
						found = true;
						break;
					}
				}
			}

			cout << (found ? "YES" : "NO") << endl;
		}
	}

	return 0;
}
