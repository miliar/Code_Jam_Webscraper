#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

vector<int> digits(unsigned int broj) {
	vector <int> digit;
	while (broj > 0) {
		digit.push_back(broj % 10);
		broj /= 10;
	}
	return digit;
}

int main() {

	unsigned int num, counter = 1, lastNumber, t;
	bool sleep = false, founded = false,insomnia = false;
	vector<int>allDigits;

	cin >> t;

	vector<int> nums;
	for (int m = 1; m <= t; ++m) {
		cin >> num;
		counter = 1;
		sleep = false;
		allDigits.clear();
		do {
			insomnia = false;
			lastNumber = num*counter;
			
			if (lastNumber == 0) {
				cout << "Case #" << m << ": INSOMNIA"<<endl;
				sleep = true;
				insomnia = true;
				break;
			}
			nums = digits(lastNumber);
			sort(nums.begin(), nums.end());
			sort(allDigits.begin(), allDigits.end());
			for (int i = 0; i < nums.size(); i++) {
				founded = false;
				for (int j = 0; j < allDigits.size(); j++) {
					if (nums[i] == allDigits[j]) {
						founded = true;
						break;
					}

				}
				if (!founded)
					allDigits.push_back(nums[i]);
			}

			if (allDigits.size() == 10)
				sleep = true;
			counter++;
		} while (!sleep);
		if(!insomnia)
		cout << "Case #" << m << ": " << lastNumber << endl;
	}

	system("pause>0");
	return 0;
}