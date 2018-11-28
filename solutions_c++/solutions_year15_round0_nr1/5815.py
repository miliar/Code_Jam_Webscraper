#define _CRT_SECURE_NO_WARNINGS
#include <functional>
#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <sstream>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <ctime>
#include <set>
#include <map>

#define ll long long
#define ld long double
#define vi vector<int>
#define vvi vector<vi >
#define pii pair<int,int>
#define forr(i, x, n) for(int i = (x); i < (n); i++)
#define forn(i, n) forr(i, 0, (n))
#define min(x, y) ((x) < (y)? (x) : (y))
#define max(x, y) ((x) > (y)? (x) : (y))
#define sqrt(x) (pow((ld)x, (ld)0.5))
#define sqr(x) ((x) * (x))
#define mp make_pair
#define endl "\n"
#define TASKNAME "deques"

#define eprintf(...) fprintf(stderr, __VA_ARGS__)

const int inf = (int)1e9;
const int mod = (int)1e9 + 7;
const ll infll = (ll)1e18;
const ld eps = 1e-9;

using namespace std;

void solve(int testN){
	int n;
	char buff[10000];
	scanf("%d %s", &n, &buff);
	string s(buff);
	int ans = 0, cur = s[0] - '0';
	forr(i, 1, n + 1){
		int x = s[i] - '0';
		if(cur < i)
			ans += (i - cur), cur = i;
		cur += x;
	}
	printf("Case #%d: %d\n", testN, ans);
}

int main() {
#ifdef __DEBUG__
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	clock_t start = clock();
#endif
	int tests;
	scanf("%d", &tests);
	forn(i, tests){
		eprintf("Case #%d working\n", i + 1);
		solve(i + 1);	
		eprintf("Case #%d complete\n", i + 1);
	}
#ifdef __DEBUG__
	fprintf(stderr, "\nTime: %Lf\n", ((clock() - start) / (ld)CLOCKS_PER_SEC));
#endif
	return 0;
}