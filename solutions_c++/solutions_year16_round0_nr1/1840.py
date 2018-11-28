#include <fstream>
#include <iostream>
#include <memory>
#include <string>
#include <vector>

using namespace std;

string solve(string& input)
{
	unsigned long long number = stoi(input);
	if (number == 0) {
		return "INSOMNIA";
	}
	int flags = 0b1111111111;
	unsigned long long last_number = 0;
	while (flags != 0) {
		last_number += number;
		if (last_number < number) {
			return "INSOMNIA";
		}
		unsigned long long temp = last_number;
		while (temp > 0) {
			int flag = 1 << (temp % 10);
			flags &= ~flag;
			temp /= 10;
		}
	}
	return to_string(last_number);
}

int main(int argc, char *argv[])
{
	unique_ptr<ifstream> in_p;
	if (argc > 1) {
		in_p.reset(new ifstream(argv[1]));
		cin.rdbuf(in_p->rdbuf());
	}
	int numCases;
	cin >> numCases;
	cin.ignore();
	vector<string> input(numCases);
	vector<string> output(numCases);
	for (int i = 0; i < numCases; ++i) {
		cin >> input[i];
		cin.ignore();
	}
	#pragma omp parallel for
	for (int i = 0; i < numCases; ++i) {
		output[i] = solve(input[i]);
	}
	for (int i = 0; i < numCases; ++i) {
		cout << "Case #" << i + 1 << ": " << output[i] << endl;
	}
}
