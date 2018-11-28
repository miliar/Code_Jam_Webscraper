#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <stdio.h>
#include <iomanip>
#include <string>
using namespace std;

bool is_possible(vector<int> &coins, int v) {
	bool possible[v+1];
	for (int i = 0; i <= v; i++) possible[i] = false;
	possible[0] = true;
	// cout << "printing1 ";
	// for (int i = 0; i <= v; i++) {
	// 	cout << possible[i] << " ";
	// 	//if (!possible[i]) return false;
	// }
	// cout << endl;
	for (int i = 0; i < coins.size(); i++) {
		bool new_possible[v+1];
		for (int j = 0; j <= v; j++) new_possible[j] = false;
		for(int j = 0; j <= v; j++) {
			if (possible[j] && (j + coins[i] <= v)) {
				new_possible[coins[i] + j] = true;
			}
		}
		for (int j = 0; j <= v; j++) possible[j] = possible[j] || new_possible[j];
	}
	//cout << endl;
	//cout << "printing2 ";
	for (int i = 0; i <= v; i++) {
		//cout << possible[i] << " ";
		if (!possible[i]) return false;
	}
	//cout << endl;
	//for (int i = 0; i < coins.size(); i++) cout << coins[i] << " " << v << " ";
	//cout << endl;
	return true;
}

bool iterate(vector<int> & coins, set<int> &have, int cur, int n, int v) {
	if (cur == n) {
		return is_possible(coins, v);
	}
	bool ans = false;
	for (int i = 1; i <= v; i++) {
		if (have.find(i) == have.end()) {
			have.insert(i);
			coins.push_back(i);
			ans = ans || iterate(coins, have, cur+1, n, v);
			have.erase(i);
			coins.pop_back();
		}
	}
	return ans;
}


int answer(int c, int d, int v, int cns[]) {
	vector<int> coins;
	for (int i = 0; i < d; i++) coins.push_back(cns[i]);
	bool possible[v+1];
	for (int i = 0; i <= v; i++) possible[i] = false;
	possible[0] = true;
	for (int i = 0; i < d; i++) {
		for(int j = 0; j <= v; j++) {
			if (possible[j] && j + coins[i] <= v) possible[coins[i] + j] = true;
		}
	}
	set<int> have;
	for (int i = 0; i < d; i++) have.insert(coins[i]);
	for (int i = 0; i < v; i++) {
		if (iterate(coins, have, 0, i, v)) return i;
	}
}

int main()
{
    int t;
	cin >> t;
	for (int _t = 1; _t <= t; _t++) {
		int c, d, v;
		cin >> c >> d >> v;
		int coins[d];
		for (int i = 0; i < d; i++) cin >> coins[i];
		cout << "Case #" << _t << ": " << answer(c, d, v, coins) << endl;
	}
    return 0;
}
