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

int factors[10];

int main()
{
#ifdef FILE_IO
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
	int T;
	cin >> T;
	cout << "Case #1:" << endl;
	int r, n, m, k;
	cin >> r >> n >> m >> k;
	REP(ii, r) {
		REP(iii, 10) factors[iii] = 0;
		REP(i, k) {
			int number;
			cin >> number;
			for (int j=2; j<=m; ++j) {
				if (number % j == 0) {
					int t = 0;
					while (number % j == 0) {
						number /= j;
						++t;
					}
					factors[j] = max(factors[j], t);
				}
			}	
		}
		//count dividers
			for(int j = 0; j < factors[3]; ++j) cout << 3;
			for(int j = 0; j < factors[5]; ++j) cout << 5;
			int t = n - factors[3] - factors[5];
			int t1 = factors[2];
			int rest = n - factors[3] - factors[5];
			int j = 0;
			while (t1 > t && j < rest) {
				t1 -= 2; 
				t -=1;
				cout << 4;
				++j;
			}
			for(; j < rest; ++j) cout << 2;
			cout << endl;
	}
    return 0;
}