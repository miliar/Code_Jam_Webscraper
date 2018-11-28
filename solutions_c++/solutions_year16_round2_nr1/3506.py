#include <iostream>
#include <bitset>
#include <iomanip>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

bool fits(int n, vector<int>& v, vector<vector<int> >& nums) {
	for (int i = 0; i < 27; ++i) {
		if (v[i] < nums[n][i]) return false;
	}
	return true;
}

vector<int> countLetters(string s) {
	vector<int> v(27, 0);
	for (int i = 0; i < s.size(); ++i) v[s[i]-'A']++;
	return v;	
}

void backtrack(int n, vector<int> v, vector<vector<int> >& nums, vector<int> sol, bool& done) {
	if (done) return;
	if (n == 10) {
		bool ok = true;
		for (int i = 0; i < 27; ++i) {
			if (v[i] > 0) ok = false;
		}
		if (ok) {
			done = true;
			for (int i = 0; i < sol.size(); ++i) cout << sol[i];
			cout << endl;
		}
		return;
	}
	if (fits(n, v, nums)) {
		vector<int> v2 = v;
		sol.push_back(n);
		for (int i = 0; i < 27; ++i) v2[i] -= nums[n][i];
		backtrack(n, v2, nums, sol, done);
		sol.pop_back();
	}
	backtrack(n+1, v, nums, sol, done);
}

int main() {
	vector<vector<int> > nums;
	nums.push_back(countLetters("ZERO"));
	nums.push_back(countLetters("ONE"));
	nums.push_back(countLetters("TWO"));
	nums.push_back(countLetters("THREE"));
	nums.push_back(countLetters("FOUR"));
	nums.push_back(countLetters("FIVE"));
	nums.push_back(countLetters("SIX"));
	nums.push_back(countLetters("SEVEN"));
	nums.push_back(countLetters("EIGHT"));
	nums.push_back(countLetters("NINE"));
	int cases;
	cin >> cases;
	for (int cas = 1; cas <= cases; ++cas) {
		cout << "Case #" << cas << ": ";
		string s;
		cin >> s;
		vector<int> v = countLetters(s);
		bool done = false;
		backtrack(0, v, nums, vector<int>(), done);
	}
}

