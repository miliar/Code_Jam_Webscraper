//g++ --std=c++14 -Wall -Wno-sign-compare -Os -march=native
#include <iostream>
#include <iterator>
#include <algorithm>
#include <limits>
#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <numeric>
#include <iomanip>
#include <cmath>
using namespace std;

void gcjmain() {
	int N;
	cin >> N;
	set<int> seen;
	if (N) {
		int i = 1;
		while (seen.size() != 10) {
			int n = i*N;
			while (n) {
				seen.insert(n%10);
				n /= 10;
			}
			i++;
		}
		cout << (i-1)*N << endl;
	} else {
		cout << "INSOMNIA" << endl;
	}
}

int main() {
	int T;
	cin >> T;
	for(int t = 1; t < T+1; t++) {
		cerr << "Case: " << t << '/' << T << endl;
		cout << "Case #" << t << ": ";
		gcjmain();
	}
}
