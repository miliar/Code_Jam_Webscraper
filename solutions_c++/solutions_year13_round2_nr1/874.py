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

		int a, n, t;
		cin >> a >> n;
		vector<int> motes;
		REP(i, n) {
			cin >> t;
			motes.push_back(t);
		}
		std::sort(ALL(motes));
		if (a == 1) {
			cout << n << endl;
			continue;
		}
		int best = n;
		for (int j = 0; j <= n; ++j) {
			lli sum = a;
			int op = j;
			for(int i = 0; i < n - j; ++i) {
				while(sum <= motes[i]) {
					sum += (sum - 1);
					++op;
				}
				sum += motes[i];
			}
			best = min(best, op);
		}
		cout << best;

		cout << endl;
	}
    return 0;
}