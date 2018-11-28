#include <iostream>
#include <string>
#include <set>
#include <sstream>
using namespace std;

using ull = unsigned long long;

string SolveA(ull x) {
	if (x == 0)
		return "INSOMNIA";
	set<int> remaining_digits = { 0,1,2,3,4,5,6,7,8,9 };
	int i = 0;
	ull result;
	while(!remaining_digits.empty()) {
		++i;
		result = x*i;
		ull y = result;
		while (y > 0) {
			int d = y % 10;
			remaining_digits.erase(d);
			y /= 10;
		}
	}
	stringstream ss;
	ss << result;
	return ss.str();
}