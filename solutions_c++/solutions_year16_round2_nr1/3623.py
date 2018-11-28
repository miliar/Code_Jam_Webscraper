#include <iostream>
#include <vector>
#include <array>

const std::array<std::string, 10> digits = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };

class EString
{
	private:
		std::string phoneNumber;
		std::vector<bool> check;

	public:
		EString(const std::string& str) :
			phoneNumber(str), check(str.size(), false)
		{}

		void printState()
		{
			std::cout << phoneNumber << '\n';
			for (bool c : check)
				std::cout << (c ? 'X' :  ' ') << '\n';
		}

		bool checkDigit(const std::string& digit)
		{
			std::vector<int> checked;
			checked.reserve(digit.size());

			for (int i = 0; i < digit.size(); i++) {
				bool found = false;
				for (int j = 0; j < phoneNumber.size() && !found; j++) {
					if (digit[i] == phoneNumber[j] && !check[j]) {
						checked.push_back(j);
						check[j] = true;
						found = true;
					}
				}

				if (!found) {
					for (int index : checked)
						check[index] = false;
					return false;
				}
			}

			return true;
		}

		void uncheckDigit(const std::string& digit)
		{
			for (int i = 0; i < digit.size(); i++) {
				bool found = false;
				for (int j = 0; j < phoneNumber.size() && !found; j++) {
					if (digit[i] == phoneNumber[j] && check[j]) {
						check[j] = false;
						found = true;
					}
				}

				/* if (!found) */
				/* 	std::cout << digit << " was not checked?\n"; */
			}
		}

		bool allChecked()
		{
			for (bool c : check) {
				if (!c)
					return false;
			}

			return true;
		}
};

bool solve(EString& eStr, int start, std::vector<int>& pn)
{
	if (eStr.allChecked())
		return true;

	for (int i = start; i < digits.size(); i++) {
		/* std::cout << "start " << start << ", trying " << i << '\n'; */
		if (eStr.checkDigit(digits[i])) {
			pn.push_back(i);
			if (solve(eStr, i, pn))
				return true;
			pn.pop_back();
			eStr.uncheckDigit(digits[i]);
		}
	}

	return false;
}

int main()
{
	int T;
	std::cin >> T;

	for (int i = 0; i < T; i++) {
		std::vector<int> pn;
		std::string number;
		std::cin >> number;

		EString eStr(number);
		solve(eStr, 0, pn);

		std::cout << "Case #" << i + 1 << ": ";
		for (int n : pn)
			std::cout << n;
		std::cout << '\n';
	}

	return 0;
}
