#include <iostream>
#include <math.h>
#include <string>
#include <fstream>
#include <sstream>
using namespace std;

bool check(int val) {
	stringstream ss;
	ss << val;
	string wode = ss.str();

	int i = 0, j = wode.length() - 1;
	while (i <= j) {
		if (wode[i] != wode[j])
			return false;
		i++;
		j--;
	}
	return true;
}

int main() {
	int T;
	cin >> T;
	ofstream of;
	of.open("q3");
	for (int k = 0; k < T; k++) {
		int A, B;
		cin >> A >> B;
		int sum = 0;
		for (int i = A; i <= B; i++) {
			int tmp = sqrt(i);
			if (tmp * tmp == i && check(i) && check(tmp)) {
				sum++;
			}
		}
		of << "Case #" << (k + 1) << ": " << sum << endl;
	}
}

