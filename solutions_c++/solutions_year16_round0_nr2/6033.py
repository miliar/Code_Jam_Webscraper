#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <stack>

using namespace std;

int flips(stack<char> pancakes);
stack<char> str_to_stack(string str);

int main()
{
	// Initialize: open file for read, create variables, etc.
	ifstream f_in("input.txt");
	ofstream f_out("output (B-).txt");
	string str_buf;

	// Read first line and fetch number of test cases.
	getline(f_in, str_buf);
	int T = atoi(str_buf.c_str());

	// Read each line; find output and print.
	for (int i = 0; i < T; ++i) {
		getline(f_in, str_buf);
		f_out << "Case #" << i + 1 << ": ";
		f_out << flips(str_to_stack(str_buf)) << endl;
	}

	// Cleanup: close files.
	f_in.close();
	f_out.flush();
	f_out.close();

    return 0;
}



int flips(stack<char> pancakes)
{
	int flip_num = 0;
	char pancake_top = pancakes.top();
	char pancake_prev = pancake_top;
	pancakes.pop();

	while (!pancakes.empty()) {
		char pancake = pancakes.top();
		pancakes.pop();
		if (pancake != pancake_prev)
			{ ++flip_num; }

		pancake_prev = pancake;
	}

	if (pancake_prev == '-')
		{ ++flip_num; }

	return flip_num;
}



stack<char> str_to_stack(string str)
{
	stack<char> output;
	for (auto itr = str.rbegin(); itr != str.rend(); ++itr)
		{ output.push(*itr); }

	return output;
}
