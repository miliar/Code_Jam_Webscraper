#pragma comment(linker, "/STACK:100000000")
#include <cassert>
#include <cstdio>
#include <sstream>
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

char s[100];

bool is_palindrome(int64 x) {
	sprintf(s, "%lld", x);
	for (int i = 0, j = strlen(s) - 1; i < j; ++i, --j)
		if (s[i] != s[j])
			return false;
	return true;
}

int main() {
//	assert(freopen(taskname".in", "r", stdin));
//	assert(freopen(taskname".out", "w", stdout));
	int t;
	int64 a, b;
	scanf("%d", &t);
	vector<int64> res;
	for (int64 x = 1; x * x <= (int64) 1e14; ++x)
		if (is_palindrome(x) && is_palindrome(x * x)) {
			res.pb(x * x);
			cerr << x * x << endl;
		}
	cerr << "hello" << endl;
	for (int it = 0; it < t; ++it) {
		scanf("%lld%lld", &a, &b);
		printf("Case #%d: %d\n", it + 1, upper_bound(res.begin(), res.end(), b) - upper_bound(res.begin(), res.end(), a - 1));
	}	
	return 0;
}