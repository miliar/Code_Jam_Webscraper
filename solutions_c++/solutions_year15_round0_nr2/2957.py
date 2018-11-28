/*
ID:
PROG: kimbits
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <complex>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <complex>
#include <stdio.h>
#include <cstdlib>
#include <unordered_set>
#include <memory.h>
#include <ctime>
#include <stack>
#include <unordered_map>
#include <functional>
#ifdef SAMMAX
#include <ctime>
clock_t beg;
#endif


const double pi = 3.1415926535897932384626433832795;
double EPS = 10e-9;
const int INF = 2000000000;

#pragma comment(linker, "/stack:1500000000")
#define sz size()
#define mp make_pair
#define pb push_back
#define ALL(a) (a).begin(), (a).end()
#define RALL(a) (a).rbegin(), (a).rend()
#define MEMS(a,b) memset(a,b,sizeof(a))
#define sqr(a) ((a)*(a))
#define HAS(a,b) ((a).find(b)!=(a).end())
#define MAX(a,b) ((a>=b)?a:b)
#define MIN(a,b) ((a<=b)?a:b)
#define ABS(a) ((a<0)?-(a):a)
#define FOR(i,a,b) for (int i=(a);i<(b);++i)
#define FORD(i,a,b) for (int i=(a);i>(b);--i)
#define VVI vector < vector <int> >
#define VI vector <int>
#define LL long long    
#define U unsigned
#define pnt pair <int,int>
LL gcd(LL a, LL b){ if (a == 0) return b; return gcd(b%a, a); }
LL lcm(LL a, LL b){ return a / gcd(a, b) * b; }

using namespace std;

void ifd() {
#ifdef SAMMAX
	//freopen("in.txt", "r", stdin);
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	beg = clock();
#else
	//freopen("kimbits.in", "r", stdin);
	//freopen("kimbits.out", "w", stdout);
#endif  
}
void tme() {
#ifdef SAMMAX
	fprintf(stderr, "*** Total time: %.3lf ***\n", 1.0*(clock() - beg) / CLOCKS_PER_SEC);
#endif
}


int tests, ans;
int d, val, mx, max_not_divided;
VI all;

int need_time(int val, int max_val, int &max_not_divided) {
	if (val <= max_val) {
		max_not_divided = MAX(max_not_divided, val);
		return 0;
	} else {
		max_not_divided = max_val;
		return (val + max_val - 1) / max_val - 1;
	}
}

int main() {
	ifd();

	cin >> tests;
	FOR(cur_test, 1, tests + 1) {
		cin >> d;
		all.clear();
		mx = 0;

		FOR(i, 0, d) {
			cin >> val;
			mx = MAX(mx, val);
			all.push_back(val);
		}
		ans = mx;
		max_not_divided = 0;

		FOR(max_val, 1, mx + 1) {
			int cur_time = 0;
			FOR(i, 0, d) {
				cur_time += need_time(all[i], max_val, max_not_divided);
			}
			ans = MIN(ans, cur_time + max_not_divided);
		}
		
		printf("Case #%d: %d\n", cur_test, ans);
	}

	tme();
	return 0;
}