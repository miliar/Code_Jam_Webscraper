
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <unordered_map>
#include <algorithm>
#include <utility>
#include <set>
#include <unordered_set>
#include <cmath>
#include <math.h>
#include <queue>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sstream>
#include <tuple>
#include <utility>
#include <iomanip>

using namespace std;
typedef long long LL;

#define printv(printVec) for (auto printVecIter : (printVec)) cout << printVecIter << " "; cout << endl;



void tsek(vector<string> plan, vector<int> mems) {
	int tot = 0;
	for (string s : plan) {
		for (int i = 0; i < s.size(); i++) {
			mems[s[i] - 'A']--;
		}
		for (auto a : mems) tot+=a;
		for (auto a : mems) {
			if (a > tot/2) {
				cout << "BOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO" << endl;
for (auto a : mems) cout << a << " "; cout << endl;
			}	
		}		
	}
}

int main() {
	std::ios::sync_with_stdio(false);cin.tie(0);
	int t;
	cin >> t;
	int T = t;
	for (int casenum = 0; casenum < t; casenum++) {
		int n; cin >> n;
		vector<int> mems(n);
		int tot = 0;
		for (int i = 0; i < n; i++) {
			cin >> mems[i];
			tot += mems[i];
		}
		vector<string> plan;
		vector<pair<int, char>> v;
		for (int i = 0; i < n; i++) {
			v.emplace_back(mems[i], 'A' + (char)i);
		}
		sort(v.rbegin(), v.rend());
		while (v[0].first > v[1].first) {
			plan.push_back(string(1, v[0].second));
			v[0].first--;
		}
		for (int i = 2; i < n; i++) {
			while (v[i].first) {
				plan.push_back(string(1, v[i].second));
				v[i].first--;
			}
		}
		while (v[0].first) {
			string s;
			s.push_back(v[0].second);
			s.push_back(v[1].second);
			plan.push_back(s);
			v[0].first--;
		}
tsek(plan, mems);
		cout << "Case #" << casenum+1 << ": ";
		for (auto a : plan) cout << a << " ";
		cout << endl;
		
	}

	
}

















