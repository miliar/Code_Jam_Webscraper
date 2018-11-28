#include <iostream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;
class Solution {
public:
	void findJamCoins(int n, int j)
	{
		string curJamCoin(n, '0');
		curJamCoin[0] = '1';
		curJamCoin[n - 1] = '1';
		int coinsCount = 0;
		do{
			vector<int> nonTrivialDivs;
			bool isJamCoin = true;
			for (int i = 2; i <= 10; ++i) {
				if (!isPrimeNumber(getInterpretation(i, curJamCoin), nonTrivialDivs)) {
					isJamCoin = false;
					break;
				}
			}
			if (isJamCoin) {
				cout << curJamCoin;
				for(auto &it : nonTrivialDivs) {
					cout << " " << it;
				}
				cout << endl;
				coinsCount++;
			}
		} while (coinsCount < j && binaryIncrement(curJamCoin));
	}
	bool isPrimeNumber(unsigned long long num, vector<int> &nonTrivialDivs) {
		for (unsigned long long i = 2; i <= sqrt(num); ++i) {
			if (num % i == 0) {
				nonTrivialDivs.push_back(i);
				return true;
			}
		}
		return false;
	}
	unsigned long long getInterpretation(int base, string value) {
		int length = value.size();
		unsigned long long result = 0;
		for (int pos = length - 1; pos >= 0; --pos) {
			int power = (length - 1) - pos;
			if (value[pos] == '1')
				result += pow(base, power);
		}
		return result;
	}
	bool binaryIncrement(string &value) {
		int carry = 1;
		for (int pos = value.size() - 2; pos > 0 && carry != 0; --pos) {
			if (value[pos] == '1' && carry == 1) {
				value[pos] = '0';
				carry = 1;
			}
			else {
				value[pos] = '1';
				carry = 0;
			}
		}
		if (carry == 1) {
			return false;
		}
		return true;
	}
};
void readInput() {
	int t, n, j;
	Solution s;
	cin >> t;
	cin >> n >> j;
	cout << "Case #1: " << endl;
	s.findJamCoins(n, j);
}
int main(int argc, char *argv[]) {
	readInput();
}