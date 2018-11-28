
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
	// Parse input
	int test_case_count;
	cin >> test_case_count;

	vector<vector<int>> test_cases;
	test_cases.resize(test_case_count);
	for (int i = 0; i < test_case_count; i++) {
		int s_max;
		cin >> s_max;

		string s_string;
		cin >> s_string;

		for (auto s_n : s_string) {
			auto s_n_int = atoi(&s_n);
			test_cases[i].push_back(s_n_int);
		}
	}

	// Solve
	int solve_case_count = 1;
	for (auto test_case : test_cases) {
		int clap_count = 0;
		int s_level = 0;
		int extra_audience = 0;
		for (auto s_n : test_case) {
			++s_level;
			if (clap_count < s_level - s_n) {
				int new_extra_audience = s_level - s_n - clap_count;
				clap_count += new_extra_audience + s_n;
				extra_audience += new_extra_audience;
			} else {
				clap_count += s_n;
			}
		}

		// Print solution
		cout << "Case #" << solve_case_count << ": " << extra_audience << endl;
		++solve_case_count;
	}

	return 0;
}