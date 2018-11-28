#pragma comment(linker, "/STACK:100000000")
#include <sstream>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <ctime>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <algorithm>
#include <iostream>
using namespace std;
#define int64 long long
#define ldb long double
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sz(a) ((int) (a).size())
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define taskname "task_c"
const ldb pi = acos(-1.0);
const int L = (int) 1e5;
char s[L];
int t, n, where[L];

int main() {
//	assert(freopen(taskname".in", "r", stdin));
//	assert(freopen(taskname".out", "w", stdout));
	scanf("%d", &t);
	for (int it = 0; it < t; ++it) {
		scanf("%d", &n), fgets(s, L, stdin);
		map<string, int> data;
		for (int i = 0; i < n; ++i) {
			fgets(s, L, stdin);
			stringstream ss;
			ss << s;
			while (ss >> s) {
				if (data.find(s) == data.end()) {
					int num = sz(data);
					where[num] = 0;
					data[s] = num;
				}
				where[data[s]] |= (1 << i);
			}
		}
		int res = (int) 1e9;
		for (int mask = 0; mask < (1 << n); ++mask) {
			if (mask % 4 != 2) continue;
			int tmp = 0;
			for (int i = 0; i < sz(data); ++i)
				if ((where[i] & mask) && (where[i] & (~mask))) ++tmp;
			res = min(res, tmp);
		}
		printf("Case #%d: %d\n", it + 1, res);
	}	
	return 0;
}
