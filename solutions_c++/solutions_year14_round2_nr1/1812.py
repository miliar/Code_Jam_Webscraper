#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <string>
#include <climits>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <list>
#include <ctime>

#define PI 3.14159265358979
#define EPS 1e-9

using namespace std;

#define REP(i, n) for (int i=0; i<n; i++)
#define FOR(i, m, n) for (int i=m; i<=n; i++)
#define ABS(a) (((a)>0)?(a):(-(a)))
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> ii;

int n;
vector<int> p[111];
vector<char> zn[111];

void solve() {
	REP (i, 111) {
		p[i].clear();
		zn[i].clear();
	}
	scanf("%d", &n);
	char s[111];
	int L;
	REP(i, n) {
		scanf(" %s", s);
		int l = strlen(s);
		REP(j, strlen(s)) {
			//printf("%d\n", j);
			zn[i].push_back(s[j]);
			//printf("Added %c\n", s[j]);
			int x = 1;
			while (j+1<l && s[j+1]==s[j]) {
				j++; x++;
			}
			p[i].push_back(x);
		}
		L = p[0].size();
		if (p[i].size()!=L) {
			printf("Fegla Won\n");
			return ;
		}
		REP (j, L) {
			if (zn[i][j] != zn[0][j]) {
				printf("Fegla Won\n");
				return ;
			}
		}
	}
	//printf("b\n");
	int res = 0;
	REP (j, L) {
		//printf("c\n");
		int best = 1111111;
		FOR (k, 1, 100) {
			//printf("d\n");
			int cnt = 0;
			REP (i, n) cnt += ABS((p[i][j] - k));
			best = min(best, cnt);
		}
		res += best;
	}
	printf("%d\n", res);
}

int main()
{
	int t;
	scanf("%d", &t);
	REP (i, t) {
		printf("Case #%d: ", i+1);
		solve();
	}
	return 0;
}
