#include <iostream>
#include <vector>
#include <math.h>
#include <bitset>
#include <algorithm>
#include <string>
#include <cstdint>
#include <stdint.h>

using namespace std;

#define ul unsigned long long

string solve(ul n) {
	string out = "INSOMNIA";
	vector<int> numbers;
	for(ul i = 1;i < 1000000000000000 && n != 0;i++) {
		ul t = n * i;
		while(t > 0) {
			ul digit = t % 10;
			auto contains = find(numbers.begin(), numbers.end(), digit);
			if(contains == numbers.end()) {
				numbers.emplace_back(digit);
			}
			t /= 10;
		}
		if(numbers.size() == 10) {
			out = to_string(n * i);
			break;
		}
	}
	return out;
}

int main()
{
	int t, n;
	cin >> t;
	for(int i = 1;i <= t;i++) {
		cin >> n;
		cout << "Case #" << i << ": " << solve(n) << endl;
	}
	return 0;
}
