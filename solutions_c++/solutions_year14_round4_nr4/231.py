#pragma comment(linker, "/STACK:128777216")

#include <cstdio>
#include <cmath>
#include <cstring>
#include <ctime>
#include <algorithm>
#include <vector>
#include <deque>
#include <string>
#include <map>
#include <set>
#include <iostream>
#include <functional>
#include <numeric>
#include <sstream>
#include <exception>
#include <cassert>
#include <windows.h>

typedef long long i64;
typedef unsigned int u32;
const int null = 0;

using namespace std;

typedef vector<int> VI;

template<class T> int size(const T &a) {
	return int(a.size());
}
template<class T> T abs(const T &a) {
	return (a < 0 ? -a : a);
}
template<class T> T sqr(const T &a) {
	return a * a;
}

#define all(a) a.begin(),a.end()

string a[8];
vector<set<string> > words;

int mx, cnt;

void gen(int i, int m) {
	if (i == -1) {
		int res = 0;
		for (int i = 0; i < m; i++) {
			set<string> cur = ::words[i];
			if (cur.size() == 0) continue;
			res++;
			string prev = "";
			for (set<string>::iterator it = cur.begin(); it != cur.end(); it++) {
				string c = *it;
				for (int j = 0; ; j++) {
					if (j == c.size() || j == prev.size() || c[j] != prev[j]) {
						res += c.size() - j;
						break;
					}
				}
				prev = c;
			}
		}
		if (res > mx) {
			mx = res;
			cnt = 1;
		}
		else if (res == mx) {
			cnt++;
		}
		return;
	}
	for (int j = 0; j < m; j++) {
		words[j].insert(a[i]);
		gen(i - 1, m);
		words[j].erase(a[i]);
	}
}

int main() {
#ifdef pperm
	freopen("input.txt", "r", stdin);
	//freopen("input.txt", "w", stdout);
	freopen("output.txt", "w", stdout);
#endif
	int T;
	scanf("%d", &T);
	for (int iTest = 1; iTest <= T; iTest++) {
		int n, m;
		scanf("%d %d", &n, &m);
		for (int i = 0; i < n; i++) {
			cin >> a[i];
		}
		words.clear();
		words.resize(m);
		mx = -1;
		cnt = 0;
		gen(n - 1, m);
		printf("Case #%d: %d %d\n", iTest, mx, cnt);
	}
#ifdef pperm
	fprintf(stderr, "\n%.3lf\n", clock() / double(CLOCKS_PER_SEC));
#endif
	return 0;
}