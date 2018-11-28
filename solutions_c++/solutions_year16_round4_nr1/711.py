// Smile please :)

#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cassert>
#include <cctype>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <string>
#include <iomanip>
#include <numeric>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <map>
#include <list>
#include <bitset>
#include <climits>
#include <unordered_map>
#include <unordered_set>
using namespace std;

//#undef KVARK_DEBUG

#ifdef KVARK_DEBUG
	#include "../h/debug.h"
#else
#define dbg(...) (void(1));
#define dbg2(...) (void(1));
#define dbg3(...) (void(1));
#define dbg4(...) (void(1));
#define dbg5(...) (void(1));
#define dbgp(...) (void(1));
#define dbg_arr(...) (void(1));
#define dbg_vec(...) (void(1));
#endif

typedef pair<int, int> pii;
typedef pair<long long, long long> pll;
typedef pair<double, int> pdi;
typedef vector<int> vi;
typedef vector<pii> vpii;
typedef vector<pll> vpll;
typedef vector<vector<int> > vvi;
typedef vector<vector<pii> > vvpii;
typedef vector<vector<long long> > vvl;
typedef vector<long long> vl;
typedef long long int llint;

#define ALL(v) (v.begin()), (v.end())
#define SZ(v) ((int)((v).size()))
#define endl "\n"

void task();

 #undef KVARK

int main(){
#ifdef KVARK
	freopen("input.txt", "r", stdin);
//	freopen("src/output.txt", "w", stdout);
#else
	freopen("src/gcj_input.txt", "r", stdin);
	freopen("src/gcj_output.txt", "w", stdout);
	srand(time(0));
#endif
//	ios_base::sync_with_stdio(0);

	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		cout << "Case #" << i + 1 << ": ";
		task();
		cout << endl;
	}

#ifdef KVARK_DEBUG
//	my_debug::printProcessInfo();
#endif
	return 0;
}
const int INF = 0x3f3f3f3f;
const int N = 3e5+10;
const int M = 3e5+10;

bool check(string s) {
	if (s.length() == 1)
		return true;
	for (int i = 0; i < s.length(); i += 2)
		if (s[i] == s[i + 1])
			return false;
	string t;
	for (int i = 0; i < s.length(); i += 2) {
		if (s[i] == 'R') {
			if (s[i + 1] == 'S')
				t += 'R';
			else
				t += 'P';
		}
		if (s[i] == 'P') {
			if (s[i + 1] == 'R')
				t += 'P';
			else
				t += 'S';
		}
		if (s[i] == 'S') {
			if (s[i + 1] == 'P')
				t += 'S';
			else
				t += 'R';
		}
	}
	return check(t);
}


string solve(string s, int a, int b, int c) {
	if (a == 0 && b == 0 && c == 0)
		return s;
	string t;
	for (int i = 0; i < s.length(); ++i) {
		if (s[i] == 'S') {
			if (b == 0)
				return "";
			--b;
			t += "SP";
		}
		if (s[i] == 'P') {
			if (a == 0)
				return "";
			--a;
			t += "PR";
		}
		if (s[i] == 'R') {
			if (c == 0)
				return "";
			--c;
			t += "RS";
		}
	}
	return solve(t, a, b, c);
}

void minimaze(string& s) {
	if (s.length() == 0)
		return;
	for (int len = 2; len <= s.length(); len *= 2) {
		for (int i = 0; i < s.length(); i += len) {
			string t1 = s.substr(i, len / 2);
			string t2 = s.substr(i + len / 2, len / 2);
			if (t2 < t1) {
				for (int j = i; j < i + len / 2; ++j)
					swap(s[j], s[j + len / 2]);
			}
		}
	}
}

void task(){
	int n;
	int a, b, c;
	cin >> n >> a >> b >> c;
	string ans;
	if (a) {
		string s = string(1, 'R');
		string res = solve(s, a-1, b, c);
		minimaze(res);
		if (res != "") {
			if (ans == "")
				ans = res;
			ans = min(ans, res);
		}
	}
	if (b) {
		string s = string(1, 'P');
		string res = solve(s, a, b-1, c);
		minimaze(res);
		if (res != "") {
			if (ans == "")
				ans = res;
			ans = min(ans, res);
		}
	}
	if (c) {
		string s = string(1, 'S');
		string res = solve(s, a, b, c-1);
		minimaze(res);
		if (res != "") {
			if (ans == "")
				ans = res;
			ans = min(ans, res);
		}
	}
	if (ans != "")
		cout << ans;
	else
		cout << "IMPOSSIBLE";
}
