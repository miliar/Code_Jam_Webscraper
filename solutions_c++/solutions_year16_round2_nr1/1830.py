#include <iostream>
#include <string>
#include <vector>

using namespace std;

string produce_answer(const vector<int> result) {
	string rs = "";
	for (int i = 0; i < result.size(); ++i) {
		for (int c = 0; c < result[i]; ++c) {
			rs += '0' + i;
		}
	}
	return rs;
}

template<typename T>
void print_answer(int case_idx, const T& answer) {
	cout << "Case #" << case_idx << ": " << answer << endl;
	cerr << "Case #" << case_idx << ": " << answer << endl;
}

vector<int> extraction_order{6, 8, 4, 5, 7, 0, 2, 3, 1, 9};
vector<char> unique_letter{'Z', 'O', 'W', 'H', 'U', 'F', 'X', 'V', 'G', 'I'};
vector<string> names{"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

void remove_entries(vector<int>& histo, int digit, int count) {
	const string& name = names[digit];
	for (int i = 0; i < name.size(); ++i) {
		histo[name[i] - 'A'] -= count;
	}
}

int process_digit(vector<int>& histo, int digit) {
	int result = histo[unique_letter[digit] - 'A'];
	remove_entries(histo, digit, result);
	return result;
}

void process_case(int case_idx) {
	string input_string;
	cin >> input_string;
	vector<int> histo(26, 0);
	for (int i = 0; i < input_string.size(); ++i)
		++histo[static_cast<int>(input_string[i]) - 'A'];

	vector<int> result(10, 0);
	for (int i = 0; i < extraction_order.size(); ++i) {
		int digit = extraction_order[i];
		result[digit] = process_digit(histo, digit);
	}

	print_answer(case_idx, produce_answer(result));
}

int main() {
	int test_count;
	cin >> test_count;
	for (int i = 1; i <= test_count; ++i) {
		process_case(i);
	}

	return 0;
}