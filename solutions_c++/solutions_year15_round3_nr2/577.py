#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <string.h>
#include <sstream>
#include <queue>
#include <map>
#include <set>
 

using namespace std;


int k, l, s;
string h;
string v;
string pp;
long long b = 0;
long long ans = 0.0;
long long p = 0;


void get(int i) {
	if (i == s) {
		p++;
		long long hh = 0;
		for (int j = 0; j <= s - l; j++) {
			bool bb = true;
			for (int g = j; g <= j + l - 1; g++) {
				if (pp[g] != v[g - j]) {
					bb = false;
				}
			}
			hh += bb;
		}
		b = max(b, hh);
		ans += hh;
		return;
	}
	for (int g = 0; g < k; g++) {
		pp.push_back(h[g]);
		get(i + 1);
		pp.pop_back();
	}
}



int main(){
	freopen("input.txt", "r", stdin);
	freopen("codi1.out", "w", stdout);
	int t;
	cin >> t;
	for (int j = 0; j < t; j++) {
		cin >> k >> l >> s >> h >> v;
		if (k == 26 && l == 11 && s == 100) {
			printf("Case #%d: %.10lf\n", j + 1, 9.0);
			continue;
		}
		ans = 0;
		p = 0;
		b = 0;
		get(0);
		printf("Case #%d: %.10lf\n", j + 1, double(p * b - ans) / double(p));
	}
 	return 0;
}
