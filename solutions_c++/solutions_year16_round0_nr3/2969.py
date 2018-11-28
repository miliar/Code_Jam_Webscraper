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

string final;

int n, k;

inline bool isprime(i64 x) {
	for(i64 i = 2; i*i <= x; ++i) {
		if (x % i == 0)
			return 0;
	}
	return 1;
}

inline i64 divisor(i64 x) {
	for(i64 i = 2; i*i <= x; ++i) {
		if (x % i == 0)
			return i;
	}
}


inline i64 parse(const string& s, int base) {
	i64 res = 0;
	for(int i = 0; i < n; ++i) {
		res *= base;
		res += s[i] - '0';
	}
	return res;
}

inline bool check(const string &s) {
	for(int base = 2; base <= 10; ++base) {
		if (isprime(parse(s, base)))
			return 0;
	}
	return 1;
}

inline bool next(string & s) {
	if (s == final)
		return 0;
	for(int i = s.size() - 2; i >= 1; --i) {
		if (s[i] == '1')
			s[i] = '0';
		else {
			s[i] = '1';
			break;
		}
	}
	return 1;
}

vector<string> ans;

inline void print() {
	i64 tmp;
	for(const string & s : ans) {
		cout << s;
		for(int base = 2; base <= 10; ++base) {
			tmp = parse(s, base);
			cout << ' ' << divisor(tmp);
		}
		cout << endl;	
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
	for(int test = 1; test <= T; ++test) {
		cin >> n >> k;
		final = string(n, '1');
		string cur = string(n, '0');
		cur[0] = '1';
		cur.back() = '1';
		while((int)ans.size() < k) {
			if (check(cur))
				ans.pb(cur);
			next(cur);
		}
		cout << "Case #" << test << ": " << endl;
		print();
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