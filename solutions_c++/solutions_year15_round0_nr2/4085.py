#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int dp(vector<int> v) {
	auto it = max_element(v.begin(), v.end());
	int index = it - v.begin();
	int temp = v[index];
	if (temp <= 3) {
		return temp;
	}
	int minTime = temp;
	for (int i = 2; i <= temp / 2; i++) {
		v[index] = temp - i;
		v.push_back(i);
		minTime = min(minTime, dp(v) + 1);
		v[index] = temp;
		v.pop_back();
	}
	return minTime;
}

int main () { 
	int t;
	cin >> t;
	for (int cas = 1; cas <= t; cas++) {
		printf("Case #%d: ", cas);
		int d;
		cin >> d;
		vector<int> v;
		for (int i = 0; i < d; i++) {
			int temp;
			cin >> temp;
			v.push_back(temp);
		}
		printf("%d\n", dp(v));
	}
	return 0;
}
