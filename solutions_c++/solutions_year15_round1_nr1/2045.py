#include <iostream>
#include <string>
#include <stack>
#include <queue>
#include <algorithm>
#include <vector>
#include <unordered_set>
#include <unordered_map>
#include <set>
#include <map>
#include <cstdio>
#include <cmath>
#include <climits>
using namespace std;

//const int mod = 1e+9 + 7;

typedef long long ll;


int main () { 
	int t;
	cin >> t;
	for (int cas = 1; cas <= t; cas++) {
		printf("Case #%d: ", cas);
		int n;
		cin >> n;
		
		vector<int> v;
		v.reserve(n);
		for (int i = 0; i < n; i++) {
			cin >> v[i];
		}

		int sum1 = 0;
		int max_gap = 0;
		for (int i = 0; i < n - 1; i++) {
			int temp = v[i] - v[i+1];
			if (temp > 0) {
				sum1 += temp;
				max_gap = max(max_gap, temp);
			}
		}

		int sum2 = 0;
		for (int i = 0; i < n - 1; i++) {
			if (v[i] >= max_gap) {
				sum2 += max_gap;
			} else {
				sum2 += v[i];
			}
		}

		printf("%d %d\n", sum1, sum2);
	}
	return 0;
}
