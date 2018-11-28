#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <iostream>
#define endl '\n'

using namespace std;

#define MP make_pair
#define lli long long int

const int N = 10010;

int n;

int solveStupid(vector<double> & f, vector<double> & s) {
	vector<bool> used(f.size(), false);
	int score = f.size();
	for(int i = 0; i < f.size(); ++i) {
		for(int j = 0; j < s.size(); ++j) {
			if (!used[j] && s[j] > f[i]) {
				--score;
				used[j] = true;
				break;
			}
		}
	}
	return score;
}

int solve2(vector<double> & f, vector<double> & s) {
	int p = 0, q = 0;
	int score = f.size();
	while(q < n) {
		if (s[q] > f[p]) {
			--score;
			++p; ++q;
		} else ++q;
	}
}

int solve(vector<double> & f, vector<double> & s) {
	int p = 0, q = 0;
	int score = 0;
	while(p < n) {
		if (f[p] > s[q]) {
			++score;
			++p; ++q;
		} else {
			++p;
		}
	}
	return score;
}

int main() {
ios_base::sync_with_stdio(0);
#ifdef FILE_IO
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif	
	int T;
	cin >> T;
	for(int qq = 0; qq < T; ++qq) {
		cout << "Case #" << qq + 1 << ": ";
		
		
		cin >> n;
		vector<double> f(n), s(n);
		for(int i = 0; i < n; ++i) cin >> f[i];
		for(int i = 0; i < n; ++i) cin >> s[i];
		sort(f.begin(), f.end());
		sort(s.begin(), s.end());

		cout << solve(f, s) << ' ' << solveStupid(f, s);

		cout << endl;
	}
	return 0;
} 