#include <iostream>
#include <fstream>
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
		int n;
		input >> n;
		if (n == 0) {
			output << "Case #" << i+1 << ": INSOMNIA" << endl;
			continue;
		}
		vector<int> k;
		for (int j = 0; j < 10; j++) {
			k.push_back(j);
		}
		
		int newn = 0;
		while (k.size() > 0) {
			newn += n;
			update(newn, k);
			//cout << k.size() << endl;
		}
		output << "Case #" << i+1  << ": " << newn << endl;
	}
}

