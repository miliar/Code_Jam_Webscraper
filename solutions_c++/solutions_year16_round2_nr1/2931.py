#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <vector>
#include <unordered_map>

using namespace std;  // since cin and cout are both in namespace std, this saves some text
void main() {
	long long int t, n;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
		char input[1500];
		cin >> input;  // read n and then m.
		int counter = 0;
		int nums[10] = {0};
		int certain_count = 0;
		unordered_map<char, int> map;
		map.insert({ {'E',0 },{ 'F',0},{ 'G',0 },{ 'H',0 },{ 'I',0 },{ 'N',0 },{ 'O',0 },{ 'R',0 },{ 'S',0 },{ 'T',0 },{ 'U',0 },{ 'V',0 },{ 'X',0 },{ 'W',0 },{ 'Z',0 } });
		while (input[counter] != '\0')
		{ 
			if (input[counter] == 'Z') {
				nums[0] += 1;
				certain_count += 4;
			}
			else if (input[counter] == 'W') {
				nums[2] += 1;
				certain_count += 3;
			}
			else if (input[counter] == 'X') {
				nums[6] += 1;
				certain_count += 3;
			}
			else if (input[counter] == 'G') {
				nums[8] += 1;
				certain_count += 5;
			}
			else if (input[counter] == 'U') {
				nums[4] += 1;
				certain_count += 5;
			}
			map[input[counter]] = map[input[counter]] + 1;
			counter++;
		}

		nums[3] = map['H'] - map['G'];
		nums[7] = map['S'] - map['X'];
		nums[5] = map['V'] - nums[7];
		nums[1] = map['O'] - nums[0] - nums[2] - nums[4];
		nums[9] = map['I'] - nums[5] - nums[6] - nums[8];

		vector<int> numbers;
		for (int j = 0; j < 10; ++j) {
			for (int k = 0; k < nums[j]; k++) {
				numbers.push_back(j);
			}
		}
	

		cout << "Case #" << i << ": ";
		for (int j = 0; j < numbers.size(); ++j) {
			cout << numbers[j];
		}
		cout << endl;
	}
}