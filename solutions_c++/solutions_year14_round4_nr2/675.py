#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
using namespace std;

void solve(){
	int n;
	cin >> n;
	vector <int> s(n);
	set <int> g;
	for (int& i : s) {
		cin >> i;
		g.insert(i);
	}
	int cnt = 0;
	for (int i : g) {
		int gg = 0;
		for (size_t j = 0; j < s.size(); j++) {
			if (s[j] == i) {
				cnt += min(gg, n - gg - 1);
				n--;
				s[j] = 0;
				break;
			}
			if (s[j] != 0)
				gg++;
		}
	}
	cout << cnt << endl;
}

int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++){
		printf("Case #%d: ", test);
		solve();
	}
}