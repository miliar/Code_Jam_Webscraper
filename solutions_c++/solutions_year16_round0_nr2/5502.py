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

ul solve(string line) {
	ul flips = 0;
	char p = line[0];
	char n;
	for(int i = 1;i < line.size();i++) {
		n = line[i];
		if(p != n) {
			flips += 1;
		}
		p = n;
	}
	if(p == '-') {
		flips += 1;
	}
	return flips;
}

int main()
{
	int t;
	string line;
	cin >> t;
	getline(cin, line);
	for(int i = 1;i <= t;i++) {
		getline(cin, line);
		cout << "Case #" << i << ": " << solve(line) << endl;
	}
	return 0;
}
