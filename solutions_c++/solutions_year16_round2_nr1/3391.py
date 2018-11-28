//https://code.google.com/codejam/contest/11254486/dashboard
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <functional>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <limits>
#include <sstream>
#include <typeinfo>
#include <iterator>

using namespace std;

vector<string> digits;

//greedy
string solve(string S)
{
	sort(S.begin(), S.end());

	multiset<char> ans;

	auto f = [&S,&ans](vector<int> ds) {
		for (int i = 0; i < (int)ds.size(); i++) {
			while (!S.empty()) {
				string result;
				auto it = set_difference(S.begin(), S.end(), digits[ds[i]].begin(), digits[ds[i]].end(), back_inserter(result));
				if (result.size() + digits[ds[i]].size() == S.size()) {
					ans.insert('0' + ds[i]);
					S = result;
				} else {
					break;
				}
			}
		}
	};

	{
		// step1: find Z=0, W=2, U=4, X=6, G=8
		const vector<int> ds = { 0, 2, 4, 6, 8 };
		f(ds);
	}
	{
		// step2: find O=1, T=3, S=7
		const vector<int> ds = { 1, 3, 7 };
		f(ds);
	}
	{
		// step3: find V=5, N=9
		const vector<int> ds = { 5, 9 };
		f(ds);
	}
	return string(ans.begin(), ans.end());
}


int main() {
	string digit[] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
	for (auto& s : digit) {
		sort(s.begin(), s.end());
		digits.push_back(s);
	}

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		string S;
		cin >> S;
		auto ans = solve(S);
		cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}
