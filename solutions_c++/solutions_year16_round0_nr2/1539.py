#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include <iomanip>
#include <vector>
#include <algorithm>
using namespace std;

void update(int n, vector<int>& k) {
	while (n > 0) {
		auto it = find(k.begin(), k.end(), n%10);
		// check that there actually is a 3 in our vector
		if (it != k.end()) {
			k.erase(it);
		}
		n /= 10;
	}
}
int main() {
	int t;
	fstream input, output;
	input.open("input.txt", ios::in);
	output.open("output.txt", ios::out);
	input >> t;
	for (int i = 0; i < t; i++) {
		string line;
		input >> line;
		int num = 0;;
		while (count(line.begin(), line.end(), '-') > 0) {
			int k = line.find('-');
			//cout << k << endl;
			while (k != line.size() && line[k] == '-') {
				k++;
			}
			k--;
			for (int j = 0; j <= k; j++) {
				line[j] = (line[j] == '-' ? '+' : '-');
			}
			num++;
		}
		output << "Case #" << i+1 << ": " << num << endl;
	}
}

