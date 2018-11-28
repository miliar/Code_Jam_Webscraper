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
#include <bitset>

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

int d[2048];

inline int solveSmall(int n, int k, int x) {
	memset(d, 0xff, sizeof(d));
	vector<int> masks;
	masks.pb((1 << k) - 1);        
	for(int i = 0; i < n - k; ++i) {
		masks.pb(masks.back() << 1);
	}
	for(int m : masks) {
		cerr << bitset<8>(m) << endl;
	}
	queue<int> q;
	d[x] = 0;
	q.push(x);
	//cout << bitset<8>(x) << endl;
	while(!q.empty()) {
		//cout << bitset<8>(x) << endl;
		x = q.front();
		q.pop();
		for(int m : masks) {
			int nx = x ^ m;
			if (d[nx] == -1) {
				d[nx] = d[x] + 1;
				q.push(nx);
			}
		}
	}
	return d[(1 << n) - 1];
}

inline char inv(char c) {
	if (c == '+')
		return '-';
	return '+';
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
	for(int test = 0; test < T; ++test) {
		string s;
		int k;
		cin >> s >> k;
		int ans = 0;
		int n = s.size();
		for(int i = 0; i < n - k + 1; ++i) {
			if (s[i] == '-') {
				++ans;
				for(int j = 0; j < k; ++j) {
					s[i+j] = inv(s[i+j]);
				}
			}
		}
		bool fail = 0;
		for(char c : s) {
			if (c == '-') {
				fail = 1;
				break;
			}
		}
		cout << "Case #" << (test + 1) << ": ";
		if (fail)
			cout << "IMPOSSIBLE";
		else
			cout << ans;
		cout << endl;
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