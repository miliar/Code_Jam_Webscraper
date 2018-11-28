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
int X, Y, N;
bool vis[1010][3000];
int dx[] = {0,-1,0,1};
int dy[] = {1,0,-1,0};

bool visit(int x, int y, int d) {
	if (vis[x][y])
		return false;
	vis[x][y] = true;
	if (y == Y-1)
		return true;
	REP(w,0,4) {
		int dt = (d+1-w+4)%4;
		int xt = x+dx[dt], yt = y+dy[dt];
		if (xt < 0 || xt >= X || yt < 0 || yt >= Y)
			continue;
		if (visit(xt, yt, dt))
			return true;
	}
	return false;
}

int main() {
	scanf("%d ", &T);
	for (int test = 0; test < T; test++) {
		fprintf(stderr, "Test %d/%d\n", test+1, T);
		printf("Case #%d: ", test+1);
		scanf("%d%d%d", &X, &Y, &N);
		REP(x,0,X) REP(y,0,Y)
			vis[x][y] = false;
		REP(i,0,N) {
			int x0, y0, x1, y1;
			scanf("%d%d%d%d", &x0, &y0, &x1, &y1);
			REP(x,x0,x1+1) REP(y,y0,y1+1)
				vis[x][y] = true;
		}
		int res = 0;
		REP(xs,0,X) {
			if (visit(xs, 0, 0))
				res++;
		}
		/*for (int y = Y-1; y >= 0; y--) {
			REP(x,0,X)
				printf("%d", vis[x][y]);
			printf("\n");
		}*/
		printf("%d\n", res);
	}
	return 0;
}
