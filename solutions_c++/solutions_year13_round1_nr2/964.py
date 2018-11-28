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

int findMax(int *a, int s, int n) {
	int m = s;
	for(int i = s + 1; i < n; ++i) {
		if (a[i] > a[m]) m = i;
	}
	return m;
}

int E, R, N;
int *v;

lli res(int pos, int e, lli acc) {
	if (pos >= N) {
		return acc;
	}
	lli m = 0;
	for(int i = 0; i <= e; ++i) {
		lli k = res(pos + 1, min(E, (e-i)+R), acc + (i * v[pos]));
		if (k > m) m = k;
	}
	return m;
}

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
		cin >> E >> R >> N;
		v = new int[N];
		REP(i, N) cin >> v[i];
		cout << res(0, E, 0) << endl;
		/*int s = 0;
		lli sum = 0;
		while (s < N) {
			int m = findMax(v, s, N);
			int e = E-R;
			sum += v[m] * f
			for(int k = m-1; k >= s; --k) {

			}
		}*/
	}
    return 0;
}