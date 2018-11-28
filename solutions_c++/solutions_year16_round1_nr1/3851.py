#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <queue>
#include <vector>
#include <bitset>
#include <time.h>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <assert.h>

using namespace std;

int t;
string s;
string result;

void find_last_word(int first_index, int last_index) {
	if (first_index >= last_index) {
		return;
	}
	int max_index = first_index;
	char max = result[first_index];
	for (int i = first_index + 1; i <= last_index; ++i) {
		if (result[i] >= max) {  // TODO check
			max = result[i];;
			max_index = i;
		}
	}
	find_last_word(first_index, max_index - 1);
	//find_last_word(max_index + 1, last_index);
	for (int i = max_index; i > first_index; --i) {
		result[i] = result[i - 1];
	}
	result[first_index] = max;
}

int main() {
	ifstream fin("A-large.in", ifstream::in);  // TODO
	ofstream fout("result.out", ofstream::out);
	fin >> t;
	//cin >> t;
	for (int i = 0; i < t; ++i) {
		fin >> s;
		//cin >> s;
		result = string(s);
		find_last_word(0, s.size() - 1);
		cout << "Case #" << (i + 1) << ": " << result << endl;
		fout << "Case #" << (i + 1) << ": " << result << endl;
	}
	return 0;
}
