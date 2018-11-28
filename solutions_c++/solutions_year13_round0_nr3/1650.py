#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <cstring>
#include <cassert>
#include <sstream>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) int(a.size() - 1)
#define all(a) a.begin(), a.end()
#define seta(a,x) memset (a, x, sizeof (a))
#define I (int)

typedef long long int64;
typedef pair <int, int> pii;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const int64 inf64 = ((int64)1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;
const string task = "";

template <class T> T sqr (T x) {return x * x;}

set<int64> res;

bool ls(pair<string, string> a, pair<string, string> b) {
	if (a.fs.size() != b.fs.size()) return a.fs.size() < b.fs.size();
	return a.fs < b.fs;
}

string get(int64 x) {
	char buf[100];
	memset(buf, 0, sizeof buf);
	sprintf(buf, "%I64d", x);
	string res = buf;
	return res;
}

int64 get(string s) {
	int64 now = 0;
	forn(i, s.size())
		now = now * 10 + s[i] - '0';
	return now;
}

void check(string s) {
	int64 now = get(s);
	int64 b = now * now;
	string e = get(b);
	forn(i, e.size())
		if (e[i] != e[e.size()-1-i])
			return;
	res.insert(get(e));
}

void go(int64 x) {
	if (x > 1e7) return;
	string s = get(x);
	string w = s; reverse(all(w));
	check(s + w);
	w = w.substr(1, w.size() - 1);
	check(s + w);
	if (x != 0) go(x * 10);
	go(x * 10 + 1);
	go(x * 10 + 2);
}

vector<int64> a;

void pre_calc(){
	go(0);
	for (int i = 1; i <= 10000; i ++) {
		string s = get(i);
		string w = s; reverse(all(w));
		check(s + w);
		w = w.substr(1, w.size() - 1);
		check(s + w);
	}
	vector<int64> b(all(res));
	a = b;
}

void solve() {
	int64 l, r;
	cin >> l >> r;
	int res = 0;
	forn(i, a.size())
		if (a[i] >= l && a[i] <= r)
			res ++;
	cout << res;
}

int main ()
{
	pre_calc();
	int n;
	cin >> n;

	forn(i, n){
		printf("Case #%d: ", i + 1);
		solve();
		puts("");
	}

	
	return 0;
}
