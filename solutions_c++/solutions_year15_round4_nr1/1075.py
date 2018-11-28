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

int dx[] = {0, 1, 0, -1};
int dy[] = {1, 0, -1, 0};

char s[1000][1000];

int main()
{
	int tts = 0, Tests;
	int n, m;
	for (scanf("%d", &Tests); Tests--; ) { 
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; ++i) scanf("%s", s[i]);

		int ans = 0;
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) 
			if (s[i][j] != '.') {
				int tot = 0;
				for (int k = 0; k < 4; ++k) {
					int nx = i + dx[k], ny = j + dy[k];
					for (; nx >= 0 && ny >= 0 && nx < n && ny < m && s[nx][ny] == '.'; ) {
						nx += dx[k];
						ny += dy[k];
					}
					if (!(nx >= 0 && ny >= 0 && nx < n && ny < m)) ++tot;
				}
				if (tot == 4) {
					ans = -1;
					break;
				}
				int o = 0;
				if (s[i][j] == 'v') o = 1;
				if (s[i][j] == '^') o = 3;
				if (s[i][j] == '<') o = 2;
				int nx = i + dx[o], ny = j + dy[o];
				for (; nx >= 0 && ny >= 0 && nx < n && ny < m && s[nx][ny] == '.'; ) {
					nx += dx[o];
					ny += dy[o];
				}
				if (!(nx >= 0 && ny >= 0 && nx < n && ny < m)) ++ans;
			}
			if (ans == -1) break;
		}

		printf("Case #%d: ", ++tts);
		if (ans == -1) puts("IMPOSSIBLE"); else printf("%d\n", ans);
	}
	return 0;
}