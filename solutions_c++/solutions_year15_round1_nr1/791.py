#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cfloat>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <set>

using namespace std;

#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define pb push_back
#define mp make_pair

int main() {
	int tc;
	cin >> tc;
	for (int t = 0; t < tc; t++) {
		int n;
		cin >> n;
		vector<int> v(n);
		FOR(i, 0, n) cin >> v[i];
		
		int madiff = 0;
		int first = 0;
		FOR(i, 1, n) {
			madiff = max(madiff, max(0, v[i-1] - v[i]));
			first += max(0, v[i-1] - v[i]);
		}
		
		
		int second = 0;
		int cur = v[0];
		FOR(i, 1, n) {
			second += min(madiff, cur);
			cur = max(0, cur - madiff);
			cur = v[i];
		}
		cout << "Case #" << t+1 << ": " << first << " " << second << endl;
		
	}
	return 0;
}
