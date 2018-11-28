#include <iostream>
#include <map>
#include <sstream>	
#include <fstream>
using namespace std;

int total_digits = 10;
const char* output_file_name = "output.txt";

map<char, int> initialize_map(map<char, int> seen_digit) {
	for (int i = 0; i < total_digits; ++i) {
		stringstream ss;
		char c;
		ss << i;
		ss >> c;
		seen_digit[c] = 0;
	}
	return seen_digit;
}

void print_map(map<char, int> seen_digit) {
	for (map<char, int>::iterator it = seen_digit.begin(); it != seen_digit.end(); ++it) {
		cout << it->first << " => " << it->second << endl;
	}
}

bool if_all_digits_seen(map<char, int> seen_digit) {
	for (map<char, int>::iterator it = seen_digit.begin(); it != seen_digit.end(); ++it) {
		if (it->second == 0) return false;
	}
	return true;
}

void write_ouput_file(string tc_num, string result) {
	ofstream output_file;
	output_file.open (output_file_name, ios_base::out | ios_base::app);
	output_file << "Case #" + tc_num + ": " << result;
	output_file.close();
}

void write_next_line() {
	ofstream output_file;
	output_file.open (output_file_name, ios_base::out | ios_base::app);
	output_file << "\n";
	output_file.close();
}

int main () {
	ifstream input_file ("A-large.in");
	string line = "";
	if (input_file.is_open()) {
		// Read total num of testcases
		string num_tc = "";
		int total_tc;
		getline(input_file, num_tc);
		stringstream ss_tc; ss_tc << num_tc; ss_tc >> total_tc;
		long long num_testcases = 0;
		// solve for each input
		while (getline(input_file, line)) {
			long long fixed_N;
			long long N;
			long long mul_with = 1;
			
			stringstream set_N; set_N << line; set_N >> N; fixed_N = N;
			map<char, int> seen_digit;
			seen_digit = initialize_map(seen_digit);
			if (num_testcases != 0) write_next_line();
			++num_testcases;
			string tc_num;
			stringstream ss_num; ss_num << num_testcases; ss_num >> tc_num;
			while (true) {
				stringstream ss;
				string num;
				ss << N;
				ss >> num;

				for (int i = 0; i < num.size(); ++i) {
					seen_digit[num[i]] = 1;
				}
				if (if_all_digits_seen(seen_digit)) {
					write_ouput_file(tc_num, num);
					break;
				} else if (N == 0) {
					write_ouput_file(tc_num, "INSOMNIA");
					break;
				} else {
					++mul_with;
					N = mul_with*fixed_N;
				}
			}
		}
	}
	return 0;
}