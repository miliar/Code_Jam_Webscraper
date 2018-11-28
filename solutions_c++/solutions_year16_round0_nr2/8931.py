#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <cassert>
#include <queue>
#include <ctime>
#include <string>
#include <cstring>
#include <bitset>
#include <unordered_map>
#define mp make_pair
#define pb push_back
#define NAME ""
#define y1 y1_423
#define list lista

using namespace std;

typedef long long ll;
typedef long double ld;

const int nmax = 1000 * 1000;
const int inf = 1000 * 1000 * 1000;
const ll infl = 1000ll * 1000ll * 1000ll * 1000ll * 1000ll * 1000ll;
const int mod = 1000 * 1000 * 1000 + 7;
const ld pi = acos(-1.0);

template<typename T>
ostream& operator << (ostream& cout, const vector<T> &a) {
	if ((int)a.size() == 0) {
		return (cout << "()");
	}
	cout << "(" << a[0];
	for (int i = 1; i < (int)a.size(); i++) {
		cout << "; " << a[i];
	}
	return (cout << ")");
}

template<typename T>
ostream& operator << (ostream& cout, const set<T> &a) {
	if ((int)a.size() == 0) {
		return (cout << "{}");
	}
	auto it = a.begin();
	cout << "{" << *it;
	++it;
	for (; it != a.end(); ++it) {
		cout << "; " << *it;
	}
	return (cout << "}");
}

template<typename T>
ostream& operator << (ostream& cout, const multiset<T> &a) {
	if ((int)a.size() == 0) {
		return (cout << "{}");
	}
	auto it = a.begin();
	cout << "{" << *it;
	++it;
	for (; it != a.end(); ++it) {
		cout << "; " << *it;
	}
	return (cout << "}");
}

template<typename T1, typename T2>
ostream& operator << (ostream& cout, const pair<T1, T2> &a) {
	return cout << "(" << a.first << "; " << a.second << ")";
}

int tests;
string s;

int main() {
	freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout);
	//freopen(NAME".in", "r", stdin);freopen(NAME".out", "w", stdout);
	cin >> tests;
	getline(cin, s);
	for (int test = 0; test < tests; test++) {
		getline(cin, s);
		int n = s.length();
		int cnt = 0;
		for (int i = 1; i < n; i++) {
			if (s[i] != s[i - 1]) {
				cnt++;
			}
		}
		if (s.back() == '-') {
			cnt++;
		}
		printf("Case #%d: %d\n", test + 1, cnt);
	}
}