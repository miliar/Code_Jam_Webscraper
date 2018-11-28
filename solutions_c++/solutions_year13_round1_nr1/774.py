#include <iostream>
#include <math.h>
#include <string.h>
#include <string>
#include <cmath>
#include <stdio.h>
#include <vector>
#include <map>
#include <list>
#include <queue> 
#include <algorithm>
#include <bitset>
#include <set>

using namespace std;

#define REP(i,n) for(long long int i = 0; i < int(n); ++i)
#define REPV(i, n) for (long long int i = (n) - 1; (int)i >= 0; --i)
#define FOR(i, a, b) for(long long int i = (int)(a); i < (int)(b); ++i)

#define ALL(v) (v).begin(), (v).end()
#define PF push_front
#define PB push_back
#define MP make_pair
#define F first
#define S second

#define lli long long int



int main()
{
#ifdef FILE_IO
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
	int T;
	cin >> T;
	REP(q, T) {
		cout << "Case #" << (q + 1) << ": ";
		lli rad, t;
		cin >> rad >> t;
		double start = (2 * rad) + 1;
		/*if (start >= t && start <= t + 3) {
			cout << 1 << endl; 
			continue;
		}*/
		double b = (start - 2)/2;
		double c = - t / 2;
		double D = (b*b) - 4 * c;
		double root = (-b + sqrt(D))/2;
		lli roo = (lli)(root);
		lli s = roo*(start + (roo - 1) * 2);
		/*if (s > t) cout << roo-1 << endl; 
		else cout << roo << endl;*/
		lli l = 0, r = roo+2;
		while (l + 1 < r) {
			lli m = l + (r - l) / 2;
			if (m * ((2 * rad) + 1 + 2 * (m-1))  >= t)
				r = m;
			else
				l = m;
		}
		if (r * ((2 * rad) + 1 + 2 * (r-1))  <= t)
			cout << r << endl;
		else
			cout << l << endl;
	}
    return 0;
}