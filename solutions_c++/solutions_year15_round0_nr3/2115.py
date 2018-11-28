#include "assert.h"
#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <time.h>
#include <vector>

#if LOCAL
	#define DO_NOT_SEND
#endif

typedef long long LL;

int IntMaxVal = (int) 1e20;
int IntMinVal = (int) -1e20;
LL LongMaxVal = (LL) 1e20;
LL LongMinVal = (LL) -1e20;

#define FOR(i, a, b) for(int i = a; i < b ; ++i)
#define FORD(i, a, b) for(int i = a; i >= b; --i)

template<typename T> inline void minimize(T &a, T b) { a = std::min(a, b); }
template<typename T> inline void maximize(T &a, T b) { a = std::max(a, b); }

#define all(v) v.begin(),v.end()

using namespace std;

#define endl '\n'
template<typename T> struct argument_type;
template<typename T, typename U> struct argument_type<T(U)> { typedef U type; };
// #define next(t, i) argument_type<void(t)>::type i; read(i);
#define next(t, i) argument_type<void(t)>::type i; cin >> i;

void read(int &x) { scanf("%d", &x); }
void read(LL &x) { scanf("%I64d", &x); }
void read(double &x) { scanf("%lf", &x); }
void read(string &s) { static char buf[5000000]; scanf("%s", &buf); s = string(buf); }

template <typename T1, typename T2> istream& operator >>(istream& is, pair<T1, T2>& s) { is >> s.first >> s.second; return is; }
template <typename T> ostream& operator << (ostream& os, const vector<T> &v) { for (int i = 0 ; i < v.size() ; i++) os << v[i] << ' '; os << endl; return os; }
template <typename T1, typename T2> ostream& operator <<(ostream& s, pair<T1, T2>& t) { s << t.first << ' ' << t.second; return s; }
template <typename T> vector<T> readVector(int n) { vector<T> res(n); for (int i = 0 ; i < n ; i++) cin >> res[i]; return res; }

struct myCout {
} mycout;

myCout& operator << (myCout &s, const string &str) { printf("%s", str.c_str()); }
myCout& operator << (myCout &s, int x) { printf("%d", x); }
myCout& operator << (myCout &s, long long int x) { printf("%I64d", x); }
myCout& operator << (myCout &s, double x) { printf("%.10lf", x); }
myCout& operator << (myCout &s, char c) { printf("%c", c); }
template <typename T> myCout& operator << (myCout& s, const vector<T> &v) { for (int i = 0 ; i < v.size() ; i++) s << v[i] << ' '; s << endl; return s; }
// #define cout mycout

vector<vector<int>> move_matrix = {
	{ 1 , 2 , 3 , 4 } ,
	{ 2 ,-1 , 4 ,-3 } ,
	{ 3 ,-4 ,-1 , 2 } ,
	{ 4 , 3 ,-2 , -1} ,
};

int update(int left, int right) {
	bool neg = false;
	if (left >= 4) {
		neg = !neg;
		left -= 4;
	}
	if (right >= 4) {
		neg = !neg;
		right -= 4;
	}
	int res = move_matrix[left][right];
	if (res < 0) {
		neg = !neg;
		res = -res;
	}
	res--;
	if (neg) res += 4;
	return res;
}

int to_int(char c) {
	return 1 + c - 'i';
}

int solve() {
	next(int, n);
	next(LL, m);
	LL totalLen = n * m;
	next(string, s);
	int cur = 0;
	int ptr1 = -1;
	vector<bool> started(8);
	while (cur != 1 && ptr1 < totalLen - 1 && (ptr1 % n != 0 || !started[cur])) {
		if (ptr1 % n == 0) started[cur] = true;
		ptr1++;
		cur = update(cur, to_int(s[ptr1 % n]));
	}
	if (cur != 1) return false;
	
	cur = 0;
	int ptr2 = totalLen;
	started.assign(started.size(), false);
	while (cur != 3 && ptr2 > 0 && (ptr2 % n != 0 || !started[cur])) {
		if (ptr2 % n == 0) started[cur] = true;
		ptr2--;
		cur = update(to_int(s[ptr2 % n]), cur);
	}
	if (cur != 3 || ptr2 <= ptr1) return false;
	
	cur = 0;
	
	int l = ptr1 + 1;
	int r = ptr2;
	
	while (l < r) {
		cur = update(cur, to_int(s[l % n]));
		l++;
	} 
	
	return cur == 2;
}

int main() {
	srand (time(NULL));
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	
	next(int, t);
	FOR (i, 0, t) cout << "Case #" << i + 1 << ": " << ( solve() ? "YES" : "NO") << endl;
}