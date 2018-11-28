#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>
#include <memory.h>
#include <vector>
#include <sstream>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <complex>
 
using namespace std;
 
 
#define REP(a,b) for (int a=0; a<(int)(b); ++a)
#define FOR(a,b,c) for (int a=(b); a<(int)(c); ++a)
 
int main() {
	int t, n;
	long long p, q, r, s;
	vector <long long> num;
	long long best;

	cin >> t;

	REP(tc,t) {
		cin >> n;
		cin >> p >> q >> r >> s;
		num.resize(n+1);
		num[0] = 0;
		REP(i,n) num[i+1] = (i*p+q)%r+s;
		FOR(i,1,n+1) num[i] += num[i-1];

		best = 1ll<<60;
		FOR(left,1,n+1) {
			long long sum_left = num[left];
			int l = left+1, r = n, m;
			while (l<r) {
				m = (l+r+1)/2;
				if (num[m]-num[left] > num[n]-num[m]) r = m-1;
				else l = m;
			}
			if (l>r) { best = min(best, sum_left); continue; }
			long long mx = max(sum_left, max(num[l]-num[left], num[n]-num[l]));
			if (l < n) mx = min(mx, max(sum_left, max(num[l+1]-num[left], num[n]-num[l+1])));
			best = min(best, mx);
		}
		printf("Case #%d: %.10lf\n", tc+1, (num[n]-best)/(double)num[n]);
	}

	return 0;
} 