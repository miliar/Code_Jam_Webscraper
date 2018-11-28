#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <vector>
#include <cstdlib>
#include <utility>
#include <memory.h>
#include <cassert>
#include <iterator>
#include <bitset>
#include <iomanip>
#include <complex>
#include <queue>
#include <ctime>
#include <deque>
#include <stack>
#include <set>
#include <map>
 
using namespace std;
 
#define pb push_back
#define mp make_pair
#define F first
#define S second

int n;

bool isOk(vector<int> p, vector<int> &v) {
	if (p.size() == 1) return true;
	vector<int> pp;
	for (int i = 0; i < p.size(); i += 2) {
		int a = v[p[i]];
		int b = v[p[i + 1]];
		int sz = (int)pp.size();
		if (a == b) return false;
		if (a == 0 && b == 2) pp.pb(p[i]);
		if (a == 1 && b == 0) pp.pb(p[i]);
		if (a == 2 && b == 1) pp.pb(p[i]);
		if (sz == (int)pp.size()) pp.pb(p[i + 1]);
	}
	return isOk(pp, v);
}

int r, pu, s;
	


void solve1() {    
	vector<int> v;
	for (int i = 0; i < r; i++) v.pb(0);
	for (int i = 0; i < pu; i++) v.pb(1);
	for (int i = 0; i < s; i++) v.pb(2);
	vector<int> p;
	int m = (1 << n);
	string out = "";
	for (int i = 0; i < m; i++) p.pb(i);
	do {
		if (isOk(p, v)) {
			string pt = "";
			for (int i = 0; i < p.size(); i++) {
				int x = v[p[i]];
				if (x == 0) pt += "R"; else if (x == 1) pt += "P"; else pt += "S";
			}            
			if (out == "") out = pt;
			out = min(out, pt);
		}
	} while (next_permutation(p.begin(), p.end()));
	int iter = 1000;
	while (iter--) {
		random_shuffle(p.begin(), p.end());
		if (isOk(p, v)) {
			string pt = "";
			for (int i = 0; i < p.size(); i++) {
				int x = v[p[i]];
				if (x == 0) pt += "R"; else if (x == 1) pt += "P"; else pt += "S";
			}            
			if (out == "") out = pt;
			out = min(out, pt);
		} 
	}
	if (out == "")
	puts("IMPOSSIBLE"); else cout << out << endl;
}

bool isOk(int r, int pu, int ss, string s) {
	map<int, int> cnt;
	cnt['R'] = r;
	cnt['P'] = pu;
	cnt['S'] = ss;
	for (int i = 0; i < (int)s.size(); i++) {
		cnt[s[i]]--;
	}
	bool fail = false;
	map<int, int> :: iterator it;
	for (it = cnt.begin(); it != cnt.end(); it++) {
		if (it -> S != 0) {
			fail = true;
			break;
		}
	}
	return !fail;
}

string get(string add, int len) {
	if (len == n) {
		return add;
	}             
	if (len > n) {
		return add;
	}
	if (len < 0) {
		exit(228);
	}                 
	string right = "";
	for (int i = 0; i < add.size(); i++) {
		right += add[i];
	}
	string le = get(add, len + 1);
	if (add == "S") {
		right = get("P", len + 1);
	} else if (add == "P") right = get("R", len + 1);
	else right = get("S", len + 1);
	string fs = le + right;
	string ss = right + le;
	return min(fs, ss);
}

string go(string t, int o) {
	string got = get(t, o);
	if (isOk(r, pu, s, got)) return got;
	return "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ";
}

void solve2() {
	string out = "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ";
	out = min(out, go("S", 0));
	out = min(out, go("P", 0));
	out = min(out, go("R", 0));
	if (out.find("Z") != string :: npos) out = "IMPOSSIBLE";
	cout << out << endl;
}


void solve(int test) {
	printf("Case #%d: ", test);
	scanf("%d", &n);
	scanf("%d%d%d", &r, &pu, &s);
	vector<int> v;
	for (int i = 0; i < r; i++) v.pb(0);
	for (int i = 0; i < pu; i++) v.pb(1);
	for (int i = 0; i < s; i++) v.pb(2);
	vector<int> p;
	int m = (1 << n);
	if (m <= 10) solve1(); else solve2();

}
              
int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	srand(time(NULL));
	int tc;
	scanf("%d", &tc);
	for (int i = 1; i <= tc; i++) {
		solve(i);
	}
	return 0;
}
