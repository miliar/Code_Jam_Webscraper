#include <iostream>
#include <vector>
#include <climits>
using namespace std;

int main () {
	int cases = 0;
	cin >> cases;
	for (int caseNum = 1; caseNum <= cases; caseNum++) {
		unsigned long long r = 0;
		cin >> r;
		unsigned long long t = 0;
		cin >> t;
		unsigned long long rings = 0;
		unsigned long long total = 0;
		while (true) {
			total += (2ULL * r) + (4ULL * rings) + 1ULL;
			if (total <= t)
				rings++;
			else
				break;
		}
		cout << "Case #" << caseNum << ": " << rings << endl;
	}
	return 0;
}
