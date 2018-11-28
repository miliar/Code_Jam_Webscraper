#include <iostream>
#include <vector>
using namespace std;

using ull = unsigned long long;

vector<ull> powers;

void print_case(int case_idx) {
	cout << "Case #" << case_idx << ":";
	cerr << "Case #" << case_idx << ":";
}

void print_coords(const vector<ull>& coords) {
	for (int i = 0; i < coords.size(); ++i) {
		cout << " " << coords[i];
		cerr << " " << coords[i];
	}
}

void print_impossible() {
	cout << " IMPOSSIBLE";
	cerr << " IMPOSSIBLE";
}

void print_endl() {
	cout << endl;
	cerr << endl;

}

void print_answer(int case_idx, vector<ull> coords) {
	print_case(case_idx);
	if (!coords.empty())
		print_coords(coords);
	else
		print_impossible();
	print_endl();
}

void calc_powers(int n, int max_pow) {
	powers = vector<ull>(max_pow + 1);
	powers[0] = 1;
	for (int i = 1; i <= max_pow; ++i) {
		powers[i] = powers[i - 1] * static_cast<ull>(n);
		// cerr << "power: " << powers[i] << endl;
	}
}

void process_case(int case_idx) {
	int beads, power, students;
	cin >> beads >> power >> students;
	calc_powers(beads, power - 1);
	std::vector<ull> result;

	int b = 0;
	int level = 0;
	ull curr_pos = 1;
	while (b < beads) {
		curr_pos += static_cast<ull>(b) * (*(powers.rbegin() + level));
		++level;
		++b;
		if (level == power || b == beads) {
			result.push_back(curr_pos);
			curr_pos = 1;
			level = 0;
		}
	}

	print_answer(case_idx, result.size() <= students ? result : vector<ull>());
}

int main() {
	int test_count;
	cin >> test_count;
	for (int i = 0; i < test_count; ++i) {
		process_case(i + 1);
	}

	return 0;
}
