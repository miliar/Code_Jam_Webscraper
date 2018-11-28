#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <vector>

using namespace std;

string case_value(int N);
set<int> int_decomp(int x);

int main()
{
	// Initialize: open file for read, create variables, etc.
	ifstream f_in("input.txt");
	ofstream f_out("output.txt");
	string str_buf;

	// Read first line and fetch number of test cases.
	getline(f_in, str_buf);
	int T = atoi(str_buf.c_str());

	// Read each line; find output and print.
	for (int i = 0; i < T; ++i) {
		getline(f_in, str_buf);
		int N = atoi(str_buf.c_str());
		f_out << "Case #" << i + 1 << ": ";
		f_out << case_value(N) << endl;
	}

	// Cleanup: close files.
	f_in.close();
	f_out.flush();
	f_out.close();

    return 0;
}



string case_value(int N)
{
	bool didSleep = false;
	int N_i = N;
	set<int> pool{0,1,2,3,4,5,6,7,8,9};

	if (N != 0) {
		while (!pool.empty()) {
			set<int> found = int_decomp(N_i);
			for (int found_i : found) {
				pool.erase(found_i);
			}
			if (pool.empty()) {
				didSleep = true;
				break;
			}
			N_i += N;
		}
	}

	string output = didSleep ? to_string(N_i) : "INSOMNIA";
	return output;
}



set<int> int_decomp(int x)
{
	set<int> output;

	// Without this first line, 0 skips the insert loop entirely.
	if (x == 0) output.insert(0);
	while (x > 0) {
		int digit = x % 10;
		output.insert(digit);
		x -= digit;
		x /= 10;
	}
	
	return output;
}