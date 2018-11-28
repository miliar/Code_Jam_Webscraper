#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <string.h>

using namespace std;

const double pi = acos(-1.0);
const double eps = 1E-7;

typedef long long int64;
typedef unsigned long long uint64;
#define two(X) (1<<(X))
#define twoL(X) (((int64)(1))<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)
#define sqr(x) ((x)*(x))
#define Abs(x) ((x) < 0 ? (-(x)) : (x))
typedef pair<int,int> ipair;
#define SIZE(A) ((int)A.size())
#define MP(A,B) make_pair(A,B)
#define PB(X) push_back(X)
#define ME(a) memset((a), 0, sizeof((a)))
#define MM(a, b) memcpy((a), (b), sizeof((a)))
#define FOR(i,n) for (int (i) = 0; (i) < (n); ++(i))
#define REP(i,a,b) for (int (i) = (a); (i) < (b); ++(i))

const int MOD = 1000000007;

int n, m;
char a[100][100];
int b[100];
int size[10];
int Trie[5][100][30];
int ans, tot;

	inline void Ins(int i, int o)
	{
		int t = 0, l = strlen(a[i] + 1);
		for (int j = 1; j <= l; ++j) {
			int wh = a[i][j] - 'A';
			if (!Trie[o][t][wh])
				Trie[o][t][wh] = ++size[o];
			t = Trie[o][t][wh];
		}
	}

	void dfs(int o) 
	{
		if (o > n) {
			ME(Trie);
			for (int i = 1; i <= m; ++i) size[i] = 0;
			for (int i = 1; i <= n; ++i)
				Ins(i, b[i]);
			int tmp = m;
			for (int i = 1; i <= m; ++i) {
				tmp += size[i];
				if (size[i] == 0) tmp = 0;
			}
			if (tmp > ans) {
				ans = tmp;
				tot = 1;
			} else if (tmp == ans) {
				++tot;
				if (tot >= MOD) tot -= MOD;
			}
			return;
		}
		for (int k = 1; k <= m; ++k) {
			b[o] = k;
			dfs(o + 1);
		}
	}

int main()
{

	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out", "w", stdout);

	int Tests, tts = 0;
	for (scanf("%d", &Tests); Tests--; ) {
		scanf("%d%d", &n, &m);
		for (int i = 1; i <= n; ++i) scanf("%s", a[i] + 1);

		ans = 0;
		tot = 0;
		dfs(1);

		printf("Case #%d: %d %d\n", ++tts, ans, tot);
	}
	return 0;
}