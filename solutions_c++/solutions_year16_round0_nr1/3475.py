#include <iostream>
#include <sstream>
#include <cassert>

using namespace std;

struct Number {
	Number(size_t n) {
		while (n) {
			increment += '0' + (n % 10);
			n /= 10;
		}
		value = increment;
	}
	void operator++() {	
		for (size_t i = 0; i < increment.size(); ++i) {
			value[i] = value[i]+increment[i]-'0';
		}
		for (size_t i = 0; i < value.size(); ++i) {
			if (value[i] > '9') {
				if (i == value.size() -1) {
					value+='0';
				}
				value[i] = value[i] -10;
				value[i+1]=value[i+1]+1;
			}
		}
	}
	operator size_t() const {
		size_t n = 0;
		size_t factor = 1;
		for (size_t i = 0; i < value.size(); ++i) {
			n+=(value[i]-'0')*factor;
			factor*=10;
		}
		return n;
	}
	string increment;
	string value;
};	

struct Result {
	Result() {
		for (int i = 0; i < 10; ++i) {
			digits[i] = false;
		}
	}

	bool isComplete() const {
		bool result = true;
		for (int i = 0; i < 10; ++i) {
			result &= digits[i];
		}
		return result;
	}

	bool process(Number n) {
		for (size_t i = 0; i < n.value.size(); ++i) {
			digits[n.value[i]-'0'] = true;
		}
		return isComplete();
	}

	bool digits[10];
};

size_t process(size_t n) {
	Result result;
	Number number(n);
	while (!result.process(number)) {
		++number;
	}
	return number;
}

int main(int argc, char** argv) {
	size_t inputCount;
	cin >> inputCount;
	for (size_t inputNumber = 1; inputNumber <= inputCount; ++inputNumber) {
		size_t N;
		cin >> N;
		cout << "Case #" << inputNumber << ": ";
		if (N)
			cout << process(N);
		else
			cout << "INSOMNIA";
		cout << endl;
	}
	return 0;
}
