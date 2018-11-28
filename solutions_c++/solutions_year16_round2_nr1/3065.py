#include <cassert>
#include <cctype>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <memory>
#include <sstream>
#include <string>
#include <vector>

#include <boost/multiprecision/cpp_int.hpp>

#define all_of(seq) begin(seq), end(seq)

using namespace std;
using namespace boost::multiprecision;

const uint8_t letter_to_prime_table[] = {
	5, 71, 37, 31, 2, 47, 59, 23, 11, 89, 79, 29, 43,
	13, 7, 53, 97, 19, 17, 3, 41, 73, 61, 83, 67, 101
};

const string digit_strings[] = {
	"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
};

cpp_int digit_products[10];

int digit_order[] = { 0, 2, 4, 6, 7, 8, 5, 3, 9, 1 };

inline cpp_int get_letter_product(const string& word)
{
	cpp_int product = 1;
	for (const char& letter : word) {
		product *= letter_to_prime_table[letter - 'A'];
	}
	return product;
}

void init_digit_products()
{
	for (int i = 0; i < 10; ++i) {
		digit_products[i] = get_letter_product(digit_strings[i]);
	}
}

string solve(string& input)
{
	istringstream ssin(input);
	ostringstream ssout;
	string s;
	ssin >> s;
	cpp_int product = get_letter_product(s);
	for (int i = 0; i < 10; ++ i) {
		int k = digit_order[i];
		while ((product % digit_products[k]) == 0) {
			ssout << k;
			product /= digit_products[k];
		}
	}
	assert(product == 1);
	string the_digits(ssout.str());
	sort(all_of(the_digits));
	return the_digits;
}

int main(int argc, char *argv[])
{
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	init_digit_products();
	unique_ptr<ifstream> in_p;
	if (argc > 1) {
		in_p.reset(new ifstream(argv[1]));
		cin.rdbuf(in_p->rdbuf());
	}
	int numCases;
	cin >> numCases;
	cin.ignore();
	vector<string> lines;
	lines.reserve(numCases);
	string line;
	while (getline(cin, line)) {
		lines.push_back(line);
	}
	vector<string> input(numCases);
	int linesPerCase = int(lines.size()) / numCases;
	for (int i = 0; i < int(lines.size()); ++i) {
		input[i / linesPerCase] += lines[i];
	}
	vector<string> output(numCases);
	#pragma omp parallel for
	for (int i = 0; i < numCases; ++i) {
		output[i] = solve(input[i]);
	}
	for (int i = 0; i < numCases; ++i) {
		cout << "Case #" << i + 1 << ':';
		if (!isspace(output[i][0])) {
			cout << ' ';
		}
		cout << output[i] << '\n';
	}
}
