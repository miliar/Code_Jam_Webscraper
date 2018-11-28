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

#define MAXM 2000333
#define MAXN 1033

struct enode {
	int to, c;
	enode *next; 
} ebase[MAXM], *etop, *fir[MAXN];
typedef enode *edge;

inline void addEdge(int a, int b, int c) {
//	printf("%d\n", etop - ebase);
	etop->to = b;
	etop->c = c;
	etop->next = fir[a];
	fir[a] = etop++;
}

bool checkIntersect(int l1, int r1, int l2, int r2) {
	return !((r1 < l2) || (r2 < l1));
}

int W, H, B;
int X0[MAXN], Y0[MAXN], X1[MAXN], Y1[MAXN];
LL dist[MAXN];
bool done[MAXN];

void solve(int Case) {
	printf("Case #%d: ", Case);
	scanf("%d %d %d", &W, &H, &B);
	Rep(i, 1, B) {
		scanf("%d %d %d %d", X0 + i, Y0 + i, X1 + i, Y1 + i);
		++X1[i];
		++Y1[i];
	}
	X0[0] = X1[0] = 0;
	Y0[0] = 0;
	Y1[0] = H;

	X0[B + 1] = X1[B + 1] = W;
	Y0[B + 1] = 0;
	Y1[B + 1] = H;

	Rep(i, 0, B + 1) fir[i] = NULL;
	etop = ebase;

//	Rep(i, 0, B + 1) printf("(%d, %d) (%d, %d)\n", X0[i], Y0[i], X1[i], Y1[i]);

	Rep(i, 0, B + 1) {
		Rep(j, i + 1, B + 1) {
			int L = -1, R = max(W, H) + 10;
			while (L + 1 != R) {
				int M = (L + R) >> 1;
				if (checkIntersect(X0[i] - M, X1[i] + M, X0[j], X1[j])
				 && checkIntersect(Y0[i] - M, Y1[i] + M, Y0[j], Y1[j]))
					R = M;
				else
					L = M;
			}
			addEdge(i, j, R);
			addEdge(j, i, R);
//			printf("(%d, %d) = %d\n", i, j, R);
		}
	}
	
	Rep(i, 0, B + 1) dist[i] = LL_INF;
	Rep(i, 0, B + 1) done[i] = false;
	dist[0] = 0;
	Rep(Round, 0, B + 1) {
		int x = -1;
		Rep(i, 0, B + 1) if (!done[i])
			if (x == -1 || dist[i] < dist[x])
				x = i;
		if (x == -1) break;
		done[x] = true;
		for (edge e(fir[x]); e; e = e->next)
			Down(dist[e->to], dist[x] + e->c);
	}
	printf("%I64d\n", dist[B + 1]);
}

int main() {
	freopen("C-large.in", "r", stdin);
	int T;
	scanf("%d", &T);
	Rep(Case, 1, T) solve(Case);
	return 0;
}
