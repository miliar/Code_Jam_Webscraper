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

string solve(string in) {
	reverse(in.begin(), in.end());
	string out = string(1, in.back());
	in.pop_back();
	while(in.size() > 0) {
		char temp = in.back();
		if(temp >= out.front()) {
			out.insert(0, string(1, temp));
		} else {
			out.push_back(temp);
		}
		in.pop_back();
	}
	return out;
}

int main()
{
	int t;
	string in;
	cin >> t;
	for(int i = 1;i <= t;i++) {
		cin >> in;
		cout << "Case #" << i << ": " << solve(in) << endl;
	}
	return 0;
}
