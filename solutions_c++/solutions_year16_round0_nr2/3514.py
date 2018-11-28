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


map<string, int> msi;

inline string rot(int c, string s) {
	reverse(s.begin(), s.begin() + c);
	for(int i = 0; i < c; ++i) {
		if (s[i] == '+')
			s[i] = '-';
	   	else
	   		s[i] = '+';
	}
	return s;
}

inline int bfs(int n, string s) {
	msi.clear();
	msi.emplace(s, 0);
	queue<string> q;
	q.push(s);
	string t;
	int d;
	while(!q.empty()) {
		s = q.front();
		q.pop();
		d = msi.find(s) -> y;
		for(int i = 1; i <= n; ++i) {
			t = rot(i, s);
			auto it = msi.find(t);
			if (it != msi.end())
				continue;
			msi.emplace(t, d + 1);
			q.push(t);
		}
	}
	return msi[string(n, '+')];
}

inline char inv(char c) {
	if (c == '-')
		return '+';
	return '-';
}

int greedy(int n, string s, char c) {
	if (n == 1) {
		if (s[0] == c)
			return 0;
		return 1;
	}	
	if (s[n-1] == c)
		return greedy(n - 1, s, c);
   	if (s[0] == s[n-1]) {
   		s = rot(n, s);
   		return greedy(n - 1, s, c) + 1;
   	}
   	return greedy(n - 1, s, inv(c)) + 1; 
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
		string s;
		cin >> s;
		cout << "Case #" << test << ": " << greedy(s.size(), s, '+') << endl;
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