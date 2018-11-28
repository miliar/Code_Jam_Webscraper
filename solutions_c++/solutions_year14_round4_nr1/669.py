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
	int n, x;
	cin >> n >> x;
	vector <int> s(n);
	for (int i = 0; i < n; i++)
		cin >> s[i];
	sort(s.begin(), s.end());
	int l = 0, r = n - 1;
	int cnt = 0;
	while (l < r) {
		if (s[l] + s[r] <= x)
			l++;
		r--;
		cnt++;
	}
	if (l == r)
		cnt++;
	printf("%d\n", cnt);
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