#include <cassert>
#include <cstdlib>
#include <cstdio>

#include <functional>
#include <iostream>
#include <algorithm>
#include <valarray>
#include <iterator>
#include <complex>
#include <numeric>
#include <utility>
#include <bitset>
#include <limits>
#include <memory>
#include <random>
#include <string>
#include <tuple>
#include <new>

#include <unordered_set>
#include <unordered_map>
#include <vector>
#include <deque>
#include <array>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>

#define DEBUG(...) fprintf(stderr, __VA_ARGS__)
#define ALL(c) begin(c), end(c)
#define SIZE(c) (int)(c).size()

using namespace std;

std::random_device rd;
std::mt19937 gen(rd());



constexpr int MAXL = 1000 * 200;

char str[MAXL];

long long get(string &s) {
	long long res = 0;
	for (int i = 0; i < (int)s.size(); i++) {
		res = res * 239 + s[i] - 'a' + 1;
	}
	return res;
}

void solve(int test) {
	DEBUG("test = %d\n", test);
	int n;
	scanf("%d\n", &n);
	vector<vector<string>> a(n);
	int cnt = 0;
	for (int i = 0; i < n; i++) {
		fgets(str, MAXL, stdin);
		std::stringstream ss(str);
		string tt;
		while (ss >> tt) {
			a[i].push_back(tt);
			cnt++;
		}
	}
	int res = cnt;
	std::unordered_set<string> eng;
	std::unordered_set<string> fre;
	for (auto x : a[0]) {
		eng.insert(x);
	}
	for (auto x : a[1]) {
		fre.insert(x);
	}
	int add = 0;
	for (auto x : eng) {
		add += fre.count(x);
	}
	DEBUG("n = %d, add = %d\n", n, add);
	unordered_set<string> fs;
	unordered_set<string> sc;
	for (int mask = 0; mask < 1 << n; mask++) {
		fs.clear();
		sc.clear();
		int temp = 0;
		if ((mask & 3) != 1) continue;
		for (int i = 2; i < n; i++) {
			if ((mask >> i) & 1) {
				for (auto x : a[i]) {
					if(!eng.count(x) && !fs.count(x)) {
						fs.insert(x);
						temp += fre.count(x);
						temp += sc.count(x);
					}
				}
			} else {
				for (auto x : a[i]) {
					if (!fre.count(x) && !sc.count(x)) {
						sc.insert(x);
						temp += eng.count(x);
						temp += fs.count(x);
					}
				}
			}
			if (temp >= res) break;
		}
		res = min(res, temp);
	}
	printf("Case #%d: %d\n", test, add + res);
}

int main () {
 	int T;
	scanf("%d", &T);
	for (int test = 1; test <= T; test++) solve(test);
}
