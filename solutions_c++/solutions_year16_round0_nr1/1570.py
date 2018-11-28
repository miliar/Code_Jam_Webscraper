#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int t;
int state = 1023; // 2^10 - 1

void clear() {
	state = 1023;
}

bool check(int current) {
	int i;
	while (current >= 10) {
		i = current % 10;
		current /= 10;
		int bit = 1 << i;
		state &= ~bit;
	}
	int bit = 1 << current;
	state &= ~bit;
	return state == 0;
}

int main() {
	ifstream fin("A-large.in", ifstream::in);
	ofstream fout("result.out", ofstream::out);
	fin >> t;
	//cin >> t;
	int n;
	for (int i = 0; i < t; ++i) {
		fin >> n;
		//cin >> n;
		if (n) {
			clear();
			int current = n;
			while (!check(current)) {
				current += n;
			}
			cout << "Case #" << (i + 1) << ": " << current << endl;
			fout << "Case #" << (i + 1) << ": " << current << endl;
		} else {
			cout << "Case #" << (i + 1) << ": INSOMNIA" << endl;
			fout << "Case #" << (i + 1) << ": INSOMNIA" << endl;
		}
	}

	return 0;
}
