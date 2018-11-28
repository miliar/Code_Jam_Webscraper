#include <iostream>
#include <string>

using namespace std;

template<typename T>
void print_answer(int case_idx, T answer) {
	cout << "Case #" << case_idx << ": " << answer << endl;
	cerr << "Case #" << case_idx << ": " << answer << endl;
}

void process_case(int case_idx) {
	string input_string;
	cin >> input_string;
	string pancakes = input_string + '+';

	int result = 0;
	for (int i = 0; i < input_string.size(); ++i) {
		result += static_cast<int>(pancakes[i] != pancakes[i + 1]);
	}

	print_answer(case_idx, result);
}

int main() {
	int test_count;
	cin >> test_count;
	for (int i = 1; i <= test_count; ++i) {
		process_case(i);
	}

	return 0;
}