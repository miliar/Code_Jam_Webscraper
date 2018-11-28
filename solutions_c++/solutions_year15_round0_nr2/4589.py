#pragma region includes
#include <algorithm>
#include <cmath>
#include <fstream>
#include <iomanip> // out << setprecision(n) << fixed; // set to show n decimal places
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <unordered_set>
#include <vector>
using namespace std;
#pragma endregion

// B. Infinite House of Pancakes

#pragma region files
//string infile = "sample.txt";
string infile = "B-small-attempt5.in";
//string infile = "B-large.in";
string outfile = "output.txt";

ifstream in(infile);
ofstream out(outfile);
#pragma endregion

long long best(map<long long, long long> &count);
long long guess(map<long long, long long> count, long long d) {
	auto it = count.rbegin();
	auto highest = it->first;
	auto n = it->second;
	auto m = highest % d;
	count.erase(highest);
	if (m) {
		count[highest / d + 1] += m * n;
	}
	count[highest / d] += (d - m) * n;
	return min(highest, (d - 1) * n + best(count));
}

long long best(map<long long, long long> &count) {
	auto it = count.rbegin();
	auto highest = it->first;
	auto n = it->second;
	if (highest <= 3) {
		return highest;
	}
	auto d = (long long) sqrt(highest);
	long long y = guess(count, d);
	for (auto i = 2; i < d; ++i) {
		y = min(y, guess(count, i));
	}
	return y;
}

int main() {
	int T;
	in >> T;
	for (int test = 1; test <= T; ++test) {
		map<long long, long long> count;
		long long D;
		long long P;
		in >> D;
		for (auto i = 0; i < D; ++i) {
			in >> P;
			++count[P];
			//cout << P << " ";
		}
		//cout << endl;
		auto y = best(count);
		out << "Case #" << test << ": " << y << endl;
	}
	return 0;
}