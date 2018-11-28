#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <vector>
#include <algorithm>
#include <sstream>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

std::vector<int> num_to_digits (int num) {
	std::vector<int> digits;
	do {
		int digit = num % 10;
		digits.push_back(digit);
		num /= 10;
	} while (num > 0);
	return digits;

}

bool contains_value(std::vector<int> accumulate_values, int possible_value) {
	return std::find(accumulate_values.begin(),accumulate_values.end(), possible_value)!=accumulate_values.end();
}


int TOTAL_POSSIBLE_VALUES_DIFS = 10;
int counting_sheep (int input_value) {
	bool finish = false;
	int mult = 1;
	std::vector<int> accumulate_values;
	int mult_value = -1;
	while (!finish) {
		mult_value = mult * input_value;
		std::vector<int> values = num_to_digits(mult_value);
		std::vector<int> values_to_add;
		for (auto possible_value: values) {
			if  (!contains_value(accumulate_values,possible_value) && !contains_value(values_to_add,possible_value)) {
				values_to_add.push_back(possible_value);
			}
		}
		accumulate_values.insert(accumulate_values.end(),values_to_add.begin(),values_to_add.end());
		values_to_add.clear();
		
		finish = ((int)accumulate_values.size() == TOTAL_POSSIBLE_VALUES_DIFS);
		mult++;
		
	}

	return mult_value;	
}



void main() {
	int t, n, m;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
		cin >> n;

		if (n == 0) {
			cout << "Case #" << i << ": " << "INSOMNIA" << endl;
			continue;
		}
	
		m = counting_sheep(n);
		cout << "Case #" << i << ": " << m << endl;

	}
}
