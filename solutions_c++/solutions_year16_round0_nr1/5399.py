#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

bool allSeen(bool seen[10]) {
	bool isAllSeen = true;
	for (int i = 0; i < 10; ++i) {
		if (!seen[i])
			isAllSeen = false;
	}
	return isAllSeen;
}

int getTimes(int n) {
	int number = n;
	vector<int> d;
	while (number) {
		d.push_back(number % 10);
		number /= 10;
	}
	bool seen[10] = { false, false, false, false, false, false, false, false,
			false, false };
	for (int i = 0; i < d.size(); ++i) {
		seen[d[i]] = true;
	}
	vector<int> orgD(d);
	int counter = 1;
	while (!allSeen(seen)) {
		counter++;
		for (int i = 0; i < d.size(); ++i) {
			d[i] += orgD[i];
			if (d[i] / 10 > 0 && i == d.size() - 1) {
				d.push_back(0);
				orgD.push_back(0);
			}
			d[i + 1] += d[i] / 10;
			d[i] = d[i] % 10;
			seen[d[i]] = true;
		}
	}
	return counter;
}

int main() {
	int t;
	ifstream input("input.in");
	input >> t;
	ofstream output;
	output.open("output.txt");
	for (int i = 0; i < t; ++i) {
		int n;
		input >> n;
		if (n == 0) {
			output << "Case #" << i + 1 << ": insomnia" << "\n";
		} else {
			output << "Case #" << i + 1 << ": " << n * getTimes(n) << "\n";
		}
	}
}
