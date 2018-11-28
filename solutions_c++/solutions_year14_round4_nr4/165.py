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

struct node {
	node *next[26];
} base[10333], *top;
typedef node *tree;

inline tree newNode() {
	memset(top, 0, sizeof(node));
	return top++;
}

void insertTrie(tree t, char *s) {
	for ( ; *s; ++s) {
		int d = *s - 'A';
		if (!t->next[d])
			t->next[d] = newNode();
		t = t->next[d];
	}
}

int M, N;
char S[1033][1033];
vector<int> Set[1033];
int ans, cnt;

void calc() {
	top = base;
//	puts("----");
	Rep(i, 1, N) {
//		printf("Set %d: ", i);
		if (!Set[i].empty()) {
			tree root = newNode();
			for (unsigned itr = 0; itr < Set[i].size(); ++itr) {
				insertTrie(root, S[ Set[i][itr] ]);
//				printf("%s ", S[Set[i][itr]]);
			}
		}
//		puts("");
	}
	int res = top - base;
	if (ans == res) ++cnt;
	else if (ans < res) {
		ans = res;
		cnt = 1;
	}
}

void Search(int i) {
	if (i == M + 1) {
		calc();
		return;
	}
	Rep(j, 1, N) {
		Set[j].push_back(i);
		Search(i + 1);
		Set[j].pop_back();
	}
}

void solve(int Case) {
	printf("Case #%d: ", Case);
	scanf("%d %d", &M, &N);
//	printf("M = %d, N = %d\n", M, N);
	Rep(i, 1, M) scanf("%s", S[i]);
	ans = -INF;
	cnt = 0;
	Search(1);
	printf("%d %d\n", ans, cnt);
}

int main() {
	int T;
	scanf("%d", &T);
	Rep(Case, 1, T) solve(Case);
	return 0;
}
