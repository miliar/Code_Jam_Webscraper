#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cstdlib>
#include <iomanip>
#include <ctime>
#include <utility>

#define x first
#define y second
#define mp make_pair
#define pb push_back
#define sqr(x) (x)*(x)
#define _with_file
#define TASK ""
#define forn(i, n) for(int i = 0; i < (int)n; ++i)

void quit(); 

using namespace std;

typedef long long i64;
typedef unsigned long long u64;
#ifdef local
typedef double ld;
#else
typedef long double ld;
#endif
typedef pair <int, int> PII;
typedef pair <i64, i64> PII64;
typedef pair <ld, ld> PLL;

const ld PI = acos(-1);
const ld EPS = 1e-10;
double __t;

int n, k;
double p[1024];

int idx[1024];

inline int bitCount(int x) {
	int res = 0;
	while(x) {
		res += x & 1;
		x >>= 1;	
	}
	return res;
}

void maskToIdx(int x) {
	int cur = 0;
	for(int i = 0; i < n; ++i)
		if (x & (1 << i))
			idx[cur++] = i;	
}

double proba() {
	double res = 0;
	for(int i = 0; i < (1 << k); ++i) {
		if (bitCount(i) == k/2) {
			double cur = 1.0;
			for(int j = 0; j < k; ++j) {
				if (i & (1 << j)) {
					cur *= p[idx[j]];
				} else {
					cur *= 1.0 - p[idx[j]];
				}
			}	
			res += cur;
		}
	}
	return res;
}

int main()
{
	#ifdef local
		__t = clock();
		#ifndef _with_files
			freopen("z.in", "rt", stdin);
			freopen("z.out", "wt", stdout);
		#endif
	#endif
	#ifdef _with_files
		freopen(TASK".in", "rt", stdin);
		freopen(TASK".out", "wt", stdout);
	#endif
	ios::sync_with_stdio(0);
	cin.tie(0);
	int T;
	cin >> T;
	for(int test = 1; test <= T; ++test) {
		cin >> n >> k;
		for(int i = 0; i < n; ++i)
			cin >> p[i];
		double ans = 0.0;
		for(int i = 0; i < (1 << n); ++i) {
			if (bitCount(i) == k) {
				maskToIdx(i);
				ans = max(ans, proba());	
			}
		}	
		cout << "Case #" << test << ": ";
		cout << ans << endl;
	} 
	quit();
}

void quit()
{
	#ifdef local
		cerr << "\nTOTAL TIME: "<< (clock() - __t)/1000.0 << " s\n";
	#endif
	exit(0);		
}