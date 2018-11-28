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

int n;
int R, P, S;
int r, p, s;
int k;

char ans[2000100];

//0 R
//1 S

bool check(int must, int cur) {
	//cerr << must << ' ' << cur << endl;
	if (must == 0) {
		//rock
		if (cur >= k) {
			if (r > 0) {
				--r;
				ans[cur] = 'R';
				return 1;
			}
			return 0;
		}
		return check(0, 2*cur) && check(1, 2*cur + 1);
	}
	if (must == 1) {
		//sci
		if (cur >= k) {
			if (s > 0) {
				--s;
				ans[cur] = 'S';
				return 1;
			}
			return 0;
		}
		return check(2, 2*cur) && check(1, 2*cur + 1);
	}
	if (must == 2) {
		//paper
		if (cur >= k) {
			if (p > 0) {
				--p;
				ans[cur] = 'P';
				return 1;
			}
			return 0;
		}
		return check(2, 2*cur) && check(0, 2*cur + 1);
	}
}

inline void swp(int idx, int len) {
	if (strncmp(&ans[idx*len + k], &ans[(idx+1)*len + k], len) > 0) {
		for(int i = 0; i < len; ++i) {
			swap(ans[idx*len + k + i], ans[(idx + 1)*len + k + i]);
		} 
	}
}

void improve() {
	for(int i = 1; i < k; i <<= 1) {
		for(int j = 0; j < k/i; j += 2) {
			swp(j, i);
		}
	}
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
	memset(ans, '!', sizeof(ans));
	for(int test = 1; test <= T; ++test) {
		cin >> n;
		cin >> R >> P >> S;
		k = 1 << n;
		string a1(k, 'Z');
		string a2(k, 'Z');
		string a3(k, 'Z');
		cout << "Case #" << test << ": ";
		r = R; p = P; s = S;
		if (check(0, 1)) {
			a1 = "";
			improve();
			for(int i = 0; i < k; ++i) {
				a1 += ans[k+i];
			}
		}
		r = R; p = P; s = S;
		if (check(1, 1)) {
			a2 = "";
			improve();
			for(int i = 0; i < k; ++i) {
				a2 += ans[k+i];
			}
		}
		r = R; p = P; s = S;
		if (check(2, 1)) {
			a3 = "";
			improve();
			for(int i = 0; i < k; ++i) {
				a3 += ans[k+i];
			}
		}
		a1 = min({a1, a2, a3});
		if (a1[0] == 'Z')
			cout << "IMPOSSIBLE";
		else
			cout << a1;
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