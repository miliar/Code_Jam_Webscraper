#include <stdio.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <assert.h>
#include <math.h>
#include <string.h>
using namespace std;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef long long ll;
#define FOREACH(it,vec) for(typeof((vec).begin()) it = (vec).begin(); it != (vec).end(); it++)
#define MODD(a,b) (((a)%(b)+(b))%(b))
#define REP(i,a,n) for (int i = (a); i < (n); i++)

int T;

int X, Y;
char line[1000];
char sp[] = ">v<^.";
int dx[] = {1,0,-1,0};
int dy[] = {0,1,0,-1};
int v[200][200];

bool iso(int x, int y, int d) {
	if (d == 4)
		return true;
	while(true) {
		x += dx[d];
		y += dy[d];
		if (x < 0 || y < 0 || x >= X || y >= Y)
			return false;
		if (v[x][y] < 4)
			return true;
	}
}

int main() {
	scanf("%d ", &T);
	for (int test = 0; test < T; test++) {
		fprintf(stderr, "Test %d/%d\n", test+1, T);
		printf("Case #%d: ", test+1);
		scanf("%d%d ", &Y, &X);
		REP(y,0,Y) {
			scanf("%s ", line);
			REP(x,0,X) {
				v[x][y] = -1;
				REP(t,0,5)
					if (line[x] == sp[t])
						v[x][y] = t;
				assert(v[x][y] != -1);
			}
		}
		bool ok = true;
		int res = 0;
		REP(x,0,X) REP(y,0,Y) {
			if (!iso(x,y,v[x][y]) && ok) {
				ok = false;
				REP(d,0,4)
					if (iso(x,y,d))
						ok = true;
				res++;
			}
		}
		if (!ok)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", res);
	}
	return 0;
}
