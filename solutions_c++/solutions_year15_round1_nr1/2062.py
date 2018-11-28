#include <iostream>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <utility>
#include <iterator>

using namespace std;


int main(int argc, char* argv[]) {
	int tests;
	int count = 1;

	string length;
	cin >> tests;
	getline(cin, length);

	while (count <= tests) {
		string nums;
		int entries;
		getline(cin, nums);
		getline(cin, nums);
		istringstream this_line(nums);
		istream_iterator<int> begin(this_line), end;
		vector<int> mushrooms(begin, end);

		unsigned int first = 0;
		unsigned int second = 0;
		int rate = 0;

		for (auto i = mushrooms.begin(); i != mushrooms.end() - 1; ++i) {
			if (*i > *(i+1))
				first += *i - *(i+1);
			if (*i - *(i+1) > rate)
				rate = *i - *(i+1);
		}
		for (auto i = mushrooms.begin(); i != mushrooms.end() -1; ++i) {
			int amount;
			if (*i > rate) {
				second += rate;
			}
			else {
				second += *i;
			}
		}

		cout << "Case #" << count << ": " << first << " " << second <<  endl;
		count++;
	}


	return 0;
}