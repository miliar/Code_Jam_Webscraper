/*
 * 1.cpp
 *
 *  Created on: 2013-5-31
 *      Author: DebutantGY
 */

#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <climits>
#include <cassert>
#include <string>
#include <bitset>
#include <vector>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <numeric>
#include <functional>
#include <algorithm>
using namespace std;

#define INF 1000000000
#define LL_INF 4000000000000000000ll
#define EPS (1e-9)
#define MOD 1000002013

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
typedef pair<int, LL> pii;
typedef pair<int, LL> pil;
typedef vector<int> VI;
typedef vector<string> VS;

//inline int rand(int a, int b) { return rand() % (b - a + 1) + a; }

template <class T> inline bool Up(T &a, const T &b) { if(a < b) {a = b; return true;} return false; }
template <class T> inline bool Down(T &a, const T &b) { if(a > b) {a = b; return true;} return false; }

inline int getus() { int tmp, c; while(tmp = fgetc(stdin), tmp < '0' || tmp > '9'); tmp -= '0'; while(c = fgetc(stdin), '0' <= c && c <= '9') tmp = tmp * 10 + c - '0'; return tmp; }
inline int getint() { int tmp, c, flag; while(flag = fgetc(stdin), flag != '-' && (flag < '0' || flag > '9')); if(flag == '-') tmp = 0; else tmp = flag - '0'; while(c = fgetc(stdin), '0' <= c && c <= '9') tmp = tmp * 10 + c - '0'; return flag == '-' ? -tmp : tmp; }

#define MAXN 2048
#define Entry first
#define Total second

int N, M, V[MAXN], totV;
pil Stack[MAXN];

void Solve(int Case) {
	map<int, LL> In, Out;
	scanf("%d %d", &N, &M);
	
	totV = 0;
	LL ans = 0;
	Rep(i, 1, M) {
		int bg, ed, cnt;
		scanf("%d %d %d", &bg, &ed, &cnt);
		In[bg] += cnt;
		Out[ed] += cnt;
		V[++totV] = bg;
		V[++totV] = ed;
//		if (Case == 14) Debug2(bg, ed);

		int k = ed - bg;
		if (!k) continue;
		ans += (LL)k * (2 * N - k + 1) / 2 % MOD * cnt % MOD;
		ans %= MOD;
	}
	sort(V + 1, V + totV + 1);
	totV = unique(V + 1, V + totV + 1) - (V + 1);
	
	int top = 0;
	Rep(itr, 1, totV) {
		int time = V[itr];
		LL in = In[time], out = Out[time];
		if (in) Stack[++top] = pil(time, in);
		while (out) {
			assert(top);
			int lastTime = Stack[top].Entry;
			LL reduce = min(Stack[top].Total, out);
//			if (Case == 14) Debug(reduce);
			if ( (Stack[top].Total -= reduce) == 0)
				--top;
			out -= reduce;
			int k = time - lastTime;
			if (!k) continue;
			ans -= (LL)k * (2 * N - k + 1) / 2 % MOD * reduce % MOD;
			ans = (ans % MOD + MOD) % MOD;
		}
	}
	
	printf("Case #%d: %I64d\n", Case, ans);
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#endif
	
	int T;
	scanf("%d", &T);
	Rep(i, 1, T) Solve(i);
	
	
	return 0;
}
