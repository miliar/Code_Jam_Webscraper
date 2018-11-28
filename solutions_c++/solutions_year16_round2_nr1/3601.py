#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <string>
#include <cstring>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <set>
#include <iomanip>

#define INF 2000000000
#define MOD 1000000007

using namespace std;

multiset<char> st;
multiset<char>::iterator it;

string arr[10];
vector<int> vec;

bool solve(int index) {
	if (st.empty())
		return true;
	if (index == 10)
		return false;
	if (solve(index + 1))
		return true;
	int cnt = 0;
	while (true) {
		bool isGood = true;
		for (int j = 0; j < arr[index].length(); j++) {
			if (st.find(arr[index][j]) == st.end()) {
				isGood = false;
				for (int i = j - 1; i >= 0; i--)
					st.insert(arr[index][i]);
				break;
			}
			st.erase(st.find(arr[index][j]));
		}
		if (isGood) {
			cnt++;
			if (solve(index + 1)) {
				while (cnt--) 
					vec.push_back(index);
				return true;
			}
		}
		else {
			while (cnt--) {
				for (int i = 0; i < arr[index].length(); i++)
					st.insert(arr[index][i]);
			}
			return false;
		}
	}
	return false;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	arr[0] = "ZERO";
	arr[1] = "ONE";
	arr[2] = "TWO";
	arr[3] = "THREE";
	arr[4] = "FOUR";
	arr[5] = "FIVE";
	arr[6] = "SIX";
	arr[7] = "SEVEN";
	arr[8] = "EIGHT";
	arr[9] = "NINE";
	for (int testNum = 1; testNum <= t; testNum++) {
		vec.clear();
		st.clear();
		cout << "Case #" << testNum << ": ";
		string s;
		cin >> s;
		for (int i = 0; i < s.length(); i++)
			st.insert(s[i]);
		while (st.find('Z') != st.end()) {
			for (int i = 0; i < arr[0].length(); i++) {
				it = st.find(arr[0][i]);
				st.erase(it);
			}
			cout << 0;
		}
		solve(1);
		reverse(vec.begin(), vec.end());
		for (int i = 0; i < vec.size(); i++)
			cout << vec[i];
		cout << endl;
	}
	return 0;
}
