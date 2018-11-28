#include <iostream>
#include <string>
class BigInt {
public:
	BigInt(int num)
		: m_digitLen(0)
	{
		for (int i = 0; i < 10; i++) {
			m_digits[i] = false;
		}
		do {
			m_digits[(num % 10)] = true;
			m_numString[m_digitLen++] = 48 + (num % 10);
			num /= 10;
		} while (num);
	}
	inline int getNumDigits() const {
		return m_digitLen;
	}
	inline const char* getIntString() const {
		return m_numString;
	}
	BigInt& operator+=(BigInt &b) {
		int index = b.getNumDigits();
		const char* bString = b.getIntString();
		int carry = 0;
		int current = 0;
		int digitSum = 0;
		while ((index > 0) || carry) {
			if (index) {
				digitSum = carry + (m_numString[current] - 48) + (bString[current] - 48);
			}
			else {
				if (current < m_digitLen) {
					digitSum = carry + (m_numString[current] - 48);
				}
				else {
					digitSum = carry;
					m_digitLen++;
				}

			}

			if (digitSum / 10) {
				carry = 1;
				digitSum = digitSum % 10;
			}
			else {
				carry = 0;
			}
			m_digits[digitSum] = true;
			m_numString[current] = (digitSum + 48);
			current++;
			index--;
		}
		return *this;
	}
	bool encouteredAllDigits() {
		for (int i = 0; i < 10; i++) {
			if (!m_digits[i]) {
				return false;
			}
		}
		return true;
	}
	void printDigits() {
		for (int i = m_digitLen - 1; i >= 0; i--) {
			std::cout << m_numString[i];
		}
	}
private:
	char m_numString[1024];
	int m_digitLen;
	bool m_digits[10];
};

void printFinalDigits(int num) {
	BigInt temp = num;
	BigInt final = temp;
	while (!final.encouteredAllDigits()) {
		final += temp;
	}
	final.printDigits();
}
int main()
{
	int nInputs;
	std::cin >> nInputs;
	int num;
	for (int i = 0; i < nInputs; i++) {
		std::cin >> num;
		if (num != 0) {
			std::cout << "Case #" << i + 1 << ": ";
			printFinalDigits(num);
			std::cout << std::endl;
		}
		else {
			std::cout << "Case #" << i + 1 << ": UNDEFINED" << std::endl;
		}
	}
    return 0;
}
