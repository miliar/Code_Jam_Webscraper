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

int N;
double A[1033], B[1033];

void solve(int Case) {
	int ans1 = 0, ans2 = 0;
	scanf("%d", &N);
	Foru(i, 0, N) scanf("%lf", A + i);
	Foru(i, 0, N) scanf("%lf", B + i);
	sort(A, A + N);
	sort(B, B + N);
	set<double> S(B, B + N);

	{
		int x = 0, y = N - 1;
		Til(i, N - 1, 0)
			if (A[y] > B[i])
				--y, ++ans1;
			else 
				++x;
	}
	{
		Foru(i, 0, N) {
			set<double>::iterator itr = S.upper_bound(A[i]);
			if (itr != S.end())
				S.erase(itr);
			else {
				S.erase(S.begin());
				++ans2;
			}
		}
	}
	printf("Case #%d: %d %d\n", Case, ans1, ans2);
}

int main() {
	int T;
	scanf("%d", &T);
	Rep(Case, 1, T) solve(Case);
	return 0;
}
 
