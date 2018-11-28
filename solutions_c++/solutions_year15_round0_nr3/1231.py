#include <fstream>
#include <string>
#include <sstream>

// Dijkstra

class quat {
public:
	int sign;
	char c;

	quat() {
		sign = 1;
		c = '1';
	}
	quat (int _s, int _c) {
		sign = _s;
		c = _c;
	}

	void reset() {
		sign = 1;
		c = '1';
	}

	void times(char q2) {
		quat result = getProduct(c, q2);
		sign *= result.sign;
		c = result.c;
	}

	bool is(char _c) {
		return sign == 1 && c == _c;
	}

	quat getProduct(char c1, char c2) {
		int sign = 1;
		char c;
		if (c1 == '1') {
			if (c2 == '1') {
				c = '1';
			} else if (c2 == 'i') {
				c = 'i';
			} else if (c2 == 'j') {
				c = 'j';
			} else {
				c = 'k';
			}
		} else if (c1 == 'i') {
			if (c2 == '1') {
				c = 'i';
			} else if (c2 == 'i') {
				sign = -1;
				c = '1';
			} else if (c2 == 'j') {
				c = 'k';
			} else {
				sign = -1;
				c = 'j';
			}
		} else if (c1 == 'j') {
			if (c2 == '1') {
				c = 'j';
			} else if (c2 == 'i') {
				sign = -1;
				c = 'k';
			} else if (c2 == 'j') {
				sign = -1;
				c = '1';
			} else {
				c = 'i';
			}
		} else {
			if (c2 == '1') {
				c = 'k';
			} else if (c2 == 'i') {
				c = 'j';
			} else if (c2 == 'j') {
				sign = -1;
				c = 'i';
			} else {
				sign = -1;
				c = '1';
			}
		}
		return quat(sign, c);
	}

};

int main() {

	std::ifstream file("input.in");
	std::ofstream out("output.txt");
	int t;
	file >> t;
	int count = 1;

	while (t-- > 0) {
		bool possible = false;
		long L, X;
		std::string str;
		file >> L;
		file >> X;
		file >> str;
		quat q;
		int i = 0;

		{ // build complete string
			std::ostringstream os;
			for (long n = 0; n < X; n++)
				os << str;
			str = os.str();
		}

		int L4 = L*4;
		int L8 = L*8;
		int L12 = L*12;

		bool _continue = false;

		while (i < L4 && !_continue) {
			char c = str[i++ % L];
			q.times(c);
			if (q.is('i'))
				_continue = true;
		}

		if (_continue) {
			_continue = false;
			q.reset();
			while (i < L8 && !_continue) {
				char c = str[i++ % L];
				q.times(c);
				if (q.is('j'))
					_continue = true;
			}

			if (_continue) {
				_continue = false;
				q.reset();
				while (i < L12 && !_continue) {
					char c = str[i++ % L];
					q.times(c);
					if (q.is('k'))
						_continue = true;
				}

				if (_continue && X > (i-1) / L) {
					q.reset();
					while (i % L > 0) {
						char c = str[i++ % L];
						q.times(c);
					}
					int r = X-1;
					r -= (i-1) / L;
					r %= 4;
					r *= L;
					while (r-- > 0) {
						char c = str[i++ % L];
						q.times(c);
					}

					if (q.is('1'))
						possible = true;
				}
			}
		}

		out << "Case #" << count++ << ": " << (possible ? "YES" : "NO") << std::endl;
	}

	return 0;
}