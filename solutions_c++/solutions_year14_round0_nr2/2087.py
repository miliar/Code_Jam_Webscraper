/*
 * 1.cpp
 *
 *  Created on: 
 *      Author: 
 */

#include <ctime>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <climits>
#include <cassert>

#include <iostream>
#include <sstream>

#include <string>
#include <vector>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <bitset>

#include <utility>
#include <numeric>
#include <functional>
#include <algorithm>

using namespace std;

#define INF 1000000000
#define LL_INF 4000000000000000000ll
#define EPS (1e-9)

#define Lowbit(x) ((x) & (-(x)))
#define Lc(x) ((x) << 1)
#define Rc(x) (Lc(x) + 1)
#define Pow2(x) (1 << (x))
#define Contain(a, x) (((a) >> (x)) & 1)

#define Rep(i, a, b) for(int i = (a); i <= (b); ++i)
#define Til(i, a, b) for(int i = (a); i >= (b); --i)
#define Foru(i, a, b) for(int i = (a); i < (b); ++i)
#define Ford(i, a, b) for(int i = (a); i > (b); --i)

#define It iterator
#define For(i, x) for(__typeof(x.begin()) i = x.begin(); i != x.end(); ++i)

#define Debug(x) (cerr << #x << " = " << (x) << endl)
#define Debug2(x, y) (cerr << #x << " = " << (x) << ", " << #y << " = " << (y) << endl)

typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
typedef pair<int, int> pii;
typedef vector<int> VI;
typedef vector<string> VS;

//inline int rand(int a, int b) { return rand() % (b - a + 1) + a; }

template <class T> inline bool Up(T &a, const T &b) { if(a < b) {a = b; return true;} return false; }
template <class T> inline bool Down(T &a, const T &b) { if(a > b) {a = b; return true;} return false; }

inline int getus() { int tmp, c; while(tmp = fgetc(stdin), tmp < '0' || tmp > '9'); tmp -= '0'; while(c = fgetc(stdin), '0' <= c && c <= '9') tmp = tmp * 10 + c - '0'; return tmp; }
inline int getint() { int tmp, c, flag; while(flag = fgetc(stdin), flag != '-' && (flag < '0' || flag > '9')); if(flag == '-') tmp = 0; else tmp = flag - '0'; while(c = fgetc(stdin), '0' <= c && c <= '9') tmp = tmp * 10 + c - '0'; return flag == '-' ? -tmp : tmp; }

double C, F, X;

double calc(int buy) {
	double speed = 2.0;
	double totTime = 0.0;
	
	Rep(i, 1, buy) {
		totTime += C / speed;
		speed += F;
	}
	totTime += X / speed;
	return totTime;
}

void solve(int Case) {
	scanf("%lf %lf %lf", &C, &F, &X);
	int left = 0, right = 100000;
	double ans = calc(0);
	while (right - left >= 3) {
//		printf("left = %d, right = %d\n", left, right);
		int lp = (left + left + right) / 3;
		int rp = (left + right + right) / 3;
//		printf("lp = %d, rp = %d\n", lp, rp);
		double lv = calc(lp), rv = calc(rp);
		Down(ans, lv);
		Down(ans, rv);
		if (lv < rv) {
			right = rp;
		}
		else {
			left = lp;
		}
	}
	Rep(i, left, right)
		Down(ans, calc(i));
	printf("Case #%d: %.7f\n", Case, ans);
}

int main() {
	int T;
	scanf("%d", &T);
	Rep(Case, 1, T) solve(Case);
	return 0;
}

