#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <limits.h>
using namespace std;

int counting_sheep(const int n) {
	if(n == 0) {
		return 0;
	}

	int val = n;
	vector<int> tbl(10);
	iota(tbl.begin(), tbl.end(), 0);

	int max = INT_MAX;
	for(int i = 1; i < max; i++) {
		if(count(tbl.begin(), tbl.end(), 1) == 10) {
			return val;
		}
		val = n*i;
		int cpy_val = val;
		while(cpy_val > 0) {
			int digit = cpy_val%10;
			tbl[digit] = 1;
			cpy_val/=10;
		}
	} 
}

int main(int argc, char *argv[]) {
	int t;
	cin >> t;

	int n;
	for(int i = 1; i <= t; i++) {
		cin >> n;
		int res = counting_sheep(n);
		if(res == 0) {
			cout << "Case #" << i << ": " << "INSOMNIA" << endl;
		}
		else {
			cout << "Case #" << i << ": " << res << endl;
		}
	}



	return 0;
}
