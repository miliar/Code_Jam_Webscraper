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

int a[10][10], b[10][10];

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int tts, Tests;
	tts = 0;
	for (scanf("%d", &Tests); Tests--; ) {
		int u, v;
		scanf("%d", &u);
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j) scanf("%d", &a[i][j]);

		scanf("%d", &v);
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j) scanf("%d", &b[i][j]);
		
		--u, --v;
		int tot = 0, wh;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				if (a[u][i] == b[v][j]) {
					++tot;
					wh = a[u][i];
				}
		printf("Case #%d: ", ++tts);
		if (tot == 1) printf("%d\n", wh);
		else
		if (tot > 1) puts("Bad magician!");
		else 
			puts("Volunteer cheated!");
	}
	return 0;
}