#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;

class fairandsquare
{
	private:
		class bignum
		{
			private:
				string digits;

			public:
				bignum() : digits("0") {}

				bignum(int num) : digits("") {
					ostringstream oss;
					oss << num;
					digits = oss.str();
				}

				bignum(string nr) : digits(nr) {}

				bignum palindromize(bool dupmid) const {
					string revdigits(digits, 0, digits.size() - (dupmid? 0 : 1));
					reverse(revdigits.begin(), revdigits.end());
					return bignum(digits + revdigits);
				}

				bool ispalindrome() {
					for (unsigned int f = 0; f < digits.size() / 2; ++f) {
						if (digits.at(f) != digits.at(digits.size() - 1 - f)) {
							return false;
						}
					}
					return true;
				}

				bignum operator+(const bignum &other) const {
					bignum result(*this);
					if (result.digits.size() < other.digits.size()) {
						result.digits = string(other.digits.size() - result.digits.size(), '0') + result.digits;
					}
					int carry = 0;
					int f, g;
					for (f = result.digits.size() - 1, g = other.digits.size() - 1; f >= 0; --f, --g) {
						int ld = result.digits.at(f) - '0';
						int rd = (g >= 0)? other.digits.at(g) - '0' : 0;
						int cres = carry + ld + rd;
						result.digits.at(f) = '0' + (cres % 10);
						carry = cres /= 10;
						if ((g < 0) && (carry == 0)) break;
					}
					if (carry > 0) {
						result.digits = string(1, '0' + (carry % 10)) + result.digits;
					}
					return result;
				}

				bignum& operator+=(const bignum &other) {
					bignum cc(*this);
					(*this) = cc + other;
					return *this;
				}

				bignum multiply(char digit) const {
					int dm = digit - '0';
					if (dm == '0') {
						return bignum("0");
					}
					bignum result(*this);
					int carry = 0;
					for (int f = result.digits.size() - 1; f >= 0; --f) {
						int cres = carry + dm * (result.digits.at(f) - '0');
						result.digits.at(f) = '0' + (cres % 10);
						carry = cres /= 10;
					}
					if (carry > 0) {
						result.digits = string(1, '0' + (carry % 10)) + result.digits;
					}
					return result;
				}

				bignum mult10(int pow10) const {
					return bignum(digits + string(pow10, '0'));
				}

				bignum operator*(const bignum &other) const {
					bignum result("0");
					vector<bignum> multdres(10);
					for (int f = 0; f < 10; ++f) {
						multdres.at(f) = this->multiply('0' + f);
					}
					int c10m = 0;
					for (int f = other.digits.size() - 1; f >= 0; --f) {
						result += multdres.at(other.digits.at(f) - '0').mult10(c10m++);
					}
					return result;
				}

				bignum& operator*=(const bignum &other) {
					bignum cc(*this);
					(*this) = cc * other;
					return *this;
				}

				bignum square() const {
					return (*this) * (*this);
				}

				bool operator<(const bignum &other) const {
					return !((*this) >= other);
				}

				bool operator<=(const bignum &other) const {
					if (digits.size() < other.digits.size()) return true;
					if (digits.size() > other.digits.size()) return false;
					return (digits <= other.digits);
				}

				bool operator>(const bignum &other) const {
					return !((*this) <= other);
				}

				bool operator>=(const bignum &other) const {
					if (digits.size() > other.digits.size()) return true;
					if (digits.size() < other.digits.size()) return false;
					return (digits >= other.digits);
				}

				bool operator==(const bignum &other) const {
					return (digits == other.digits);
				}

				bool operator!=(const bignum &other) const {
					return !((*this) == other);
				}

				string tostring() const {
					return digits;
				}
		};

		bignum A, B;

	public:
		void input() {
			string ins;
			cin >> ins;
			A = bignum(ins);
			cin >> ins;
			B = bignum(ins);
		}

		int solve() {
			int sol = 0;
			bignum one("1");
			bignum cb("1");
			int ctr = 0;
			while (true) {
				++ctr;
				bignum palsym = cb.palindromize(true).square();
				bignum palasy = cb.palindromize(false).square();
				if (palasy > B) break;
				if ((A <= palasy) && (palasy <= B) && (palasy.ispalindrome())) {
					++sol;
				}
				if ((A <= palsym) && (palsym <= B) && (palsym.ispalindrome())) {
					++sol;
				}
				cb += one;
			}
			return sol;
		}
};

int main(void) {
	int nt = 1;
	cin >> nt;
	for (int znj = 0; znj < nt; ++znj) {
		fairandsquare task;
		task.input();
		cout << "Case #" << (znj + 1) << ": " << task.solve() << endl;
	}
	return 0;
}
