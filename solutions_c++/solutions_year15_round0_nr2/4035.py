//============================================================================
// Name        : B.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <vector>
#include <iostream>
#include <cstring>
#include <cstdio>
#define MAXN 1010
using namespace std;
int n;
int ans;
bool over(vector<int> arr) {
	for (int i = 0; i < arr.size(); i++) {
		if (arr[i]) {
			return false;
		}
	}
	return true;
}
void dfs(vector<int> arr, int depth) {
	if (depth >= ans) {
		return;
	}
	if (over(arr)) {
		ans = depth;
		return;
	}
	vector<int> tmp;
	for (int i = 0; i < arr.size(); i++) {
		if (arr[i] > 0) {
			tmp.push_back(arr[i] - 1);
		}
	}
	dfs(tmp, depth + 1);

	tmp.clear();
	for (int i = 0; i < arr.size(); i++) {
		tmp.push_back(arr[i]);
	}
	sort(tmp.begin(), tmp.end());
	int size = tmp.size();
	int val = tmp[size - 1];
	tmp.push_back(0);
	for (int i = 1; i <= val / 2; i++) {
		tmp[size - 1] = i;
		tmp[size] = val - i;
		dfs(tmp, depth + 1);

	}
}
int main() {
	int T;
	int ca = 1;
	cin >> T;
	vector<int> arr;
	while (T--) {
		cin >> n;
		ans = 0;
		arr.clear();
		for (int i = 0; i < n; ++i) {
			int tmp;
			cin >> tmp;
			arr.push_back(tmp);
			ans = max(ans, tmp);
		}
		dfs(arr, 0);
		cout << "Case #" << ca++ << ": " << ans << endl;
	}
	return 0;
}
