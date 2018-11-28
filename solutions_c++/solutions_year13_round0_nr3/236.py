#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

class BigInteger {
private:
	string integer;
public:
	BigInteger(unsigned int integer);
	BigInteger(string integer);
	void setInteger(unsigned int integer);
	void setInteger(string integer);
	unsigned int getIntValue() const;
	string toString() const;
	BigInteger addInteger(const BigInteger& integer_to_add) const;
	BigInteger addInteger(const string& integer_to_add) const;
	BigInteger multiplyInteger(const BigInteger& integer_to_multiply) const;
	BigInteger multiplyInteger(const string& integer_to_multiply) const;
	static size_t getTrimIndex(const string& integer);
	bool operator==(const BigInteger& integer) const;
	BigInteger operator+(const BigInteger& integer) const;
	BigInteger operator*(const BigInteger& integer) const;
	friend ostream& operator<<(ostream& in, BigInteger& integer);
};



vector<string> num;

bool is(string s) {
	int c = 0;
	for (int i = 0; i < s.size() - 1; i++) {
		c += (s[i] - '0') * (s[i] - '0');
	}
	return (2 * c) < 10;
}

bool iss(string s) {
	int c = 0;
	for (int i = 0; i < s.size(); i++) {
		c += (s[i] - '0') * (s[s.size() - 1 - i] - '0');
	}
	return c < 10;
}

string rev(string s) {
	for (int i = 0; i < s.size() / 2; i++) {
		int t = s[s.size() - i - 1];
		s[s.size() - i - 1] = s[i];
		s[i] = t;
	}
	return s;
}

int nn;

void f(string p) {
	if (!is(p)) return;

	if (nn % 2 == 0 && p.size() >= nn / 2) {
		string pp = p + rev(p);
		if (iss(pp)) num.push_back(pp);
		return;
	}

	if ((nn - 1) % 2 == 0 && p.size() >= (nn + 1) / 2) {
		string pp = p + rev(p.substr(0, p.size() - 1));
		if (iss(pp)) num.push_back(pp);
		return;
	}

	f(p + "0");
	f(p + "1");
	f(p + "2");
}

void gen() {
	for (int n = 1; n <= 51; n++) {
		nn = n;
		f("1");
		f("2");
		f("3");
	}
}

int compare(string a, string b) {
	if (a.size() != b.size()) return a.size() - b.size();

	for (int i = 0; i < min(a.size(), b.size()); i++) {
		if (a[i] < b[i]) return -1;
		else if (a[i] > b[i]) return 1;
	}

	return 0;
}



int main() {
	ifstream in("C-large-2.in");
	ofstream out("C-large-2.out");

	gen();
	vector<string> num_2;
	for (int i = 0; i < num.size(); i++) {
		BigInteger a = BigInteger(num[i]) * BigInteger(num[i]);
		num_2.push_back(a.toString());
	}

	int T; in >> T;
	for (int x = 1; x <= T; x++) {
		string A, B; in >> A >> B;
		long long c = 0;
		for (int i = 0; i < num_2.size(); i++) {
			if (compare(num_2[i], A) >= 0 && compare(num_2[i], B) <= 0) c++;
		}
		out << "Case #" << x << ": " << c << endl;
	}
}



BigInteger::BigInteger(unsigned int integer) {
	setInteger(integer);
}

BigInteger::BigInteger(string integer) {
	for (int i = 0; i < (int)integer.size() && integer[i] >= '0' && integer[i] <= '9'; i++) {
		this->integer += integer[i];
	}

	if (this->integer.size() == 0) {
		this->integer = "0";
	} else {
		this->integer = integer.substr(getTrimIndex(integer));
	}
}

void BigInteger::setInteger(unsigned int integer) {
	if (integer == 0) this->integer = "0";

	while (integer) {
		this->integer = (char)((integer % 10) + '0') + this->integer;
		integer /= 10;
	}
}

void BigInteger::setInteger(string integer) {
	this->integer = integer;
}

unsigned int BigInteger::getIntValue() const {
	unsigned int ret = 0;
	unsigned int biggest = 0xFFFFFFFF;
	for (int i = 0; i < (int)integer.size(); i++) {
		int unit = integer[i] - '0';
		if (ret > (biggest - unit) / 10.0) return 0;
		ret = ret * 10 + unit;
	}
	return ret;
}

string BigInteger::toString() const {
	return integer;
}

BigInteger BigInteger::addInteger(const BigInteger& integer_to_add) const {
	int a_n = max((int)(integer_to_add.toString().size() - toString().size()), 0);
	int b_n = max((int)(toString().size() - integer_to_add.toString().size()), 0);
	string a = string(a_n, '0') + toString();
	string b = string(b_n, '0') + integer_to_add.toString();

	reverse(a.begin(), a.end());
	reverse(b.begin(), b.end());

	string result; int carry = 0;

	for (int i = 0; i < (int)a.size(); i++) {
	   int sum = (a[i] - '0') + (b[i] - '0') + carry;
	   result += ((char)(sum % 10 + '0'));
	   carry = sum / 10;
	}

	if (carry != 0) result += ((char)(carry + '0'));

	reverse(result.begin(), result.end());

	return BigInteger(result.substr(getTrimIndex(result)));
}

BigInteger BigInteger::addInteger(const string& integer_to_add) const {
	return addInteger(BigInteger(integer_to_add));
}

BigInteger BigInteger::multiplyInteger(const BigInteger& integer_to_multiply) const {
	string a = integer_to_multiply.toString();
	string b = toString();

	reverse(a.begin(), a.end());
	reverse(b.begin(), b.end());

	BigInteger ret("0");

	for (int i = 0; i < (int)a.size(); i++) {
		int carry = 0; string tmp = string(i, '0');

		for (int j = 0; j < (int)b.size(); j++) {
			int mul = (a[i] - '0') * (b[j] - '0') + carry;
			tmp += ((char)(mul % 10 + '0'));
			carry = mul / 10;
		}

		if (carry != 0) tmp += (carry + '0');

		reverse(tmp.begin(), tmp.end());

		ret = ret.addInteger(tmp.substr(getTrimIndex(tmp)));
	}

	return ret;
}

BigInteger BigInteger::multiplyInteger(const string& integer_to_multiply) const {
	return multiplyInteger(BigInteger(integer_to_multiply));
}

size_t BigInteger::getTrimIndex(const string& integer) {
	size_t index = 0;
	while (integer[index] == '0' && index < integer.size() - 1) index++;
	return index;
}

bool BigInteger::operator==(const BigInteger& integer) const {
	return this->integer == integer.toString();
}

BigInteger BigInteger::operator+(const BigInteger& integer) const {
	return addInteger(integer);
}

BigInteger BigInteger::operator*(const BigInteger& integer) const {
	return multiplyInteger(integer);
}

ostream& operator<<(ostream& in, BigInteger& integer) {
	in << integer.toString();

	return in;
}
