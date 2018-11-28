#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <complex>
#include <ctime>
#include <cassert>
#include <functional>

using namespace std;

typedef long long ll;
typedef vector<int> VI;
typedef pair<int, int> PII;

#define REP(i,s,t) for(int i=(s);i<(t);i++)
#define FILL(x,v) memset(x,v,sizeof(x))

const int INF = (int)1E9;
#define MAXN 105

int N, M;
char g[MAXN][MAXN];
int indeg[MAXN][MAXN], outdeg[MAXN][MAXN];
PII pt[MAXN][MAXN], ot = PII(-1,-1);
int dir[4][2] = { -1, 0, 0, 1, 1, 0, 0, -1 };
PII seek(int x, int y, int d) {
	if (x < 0 || y < 0 || x >= N || y >= M) return ot;
	if (g[x][y] != '.') return PII(x, y);
	return seek(x + dir[d][0], y + dir[d][1], d);
}
int main(){
	int cs;
	cin >> cs;
	REP(csn, 1, cs + 1){
		printf("Case #%d: ", csn);
		cin >> N >> M;
		REP(i, 0, N) scanf("%s", g[i]);
		REP(i, 0, N) REP(j, 0, M) pt[i][j] = ot;
		FILL(indeg, 0); FILL(outdeg, 0);
		REP(i, 0, N){
			REP(j, 0, M){
				char c = g[i][j];
				if (c == '.') continue;
				int d;
				if (c == '^') d = 0;
				else if (c == '>') d = 1;
				else if (c == 'v') d = 2;
				else if (c == '<') d = 3;
				PII nxt = seek(i + dir[d][0], j + dir[d][1], d);
				if (nxt == ot) continue;
				//cerr << i << " " << j << " -> " << nxt.first << " " << nxt.second << endl;
				pt[i][j] = nxt;
				indeg[nxt.first][nxt.second]++;
				outdeg[i][j]++;
			}
		}
		int ans = 0, ok = 1;
		REP(i, 0, N) {
			REP(j, 0, M){
				if (g[i][j] == '.') continue;
				if (outdeg[i][j] == 0) {
					if (indeg[i][j] == 0) {
						bool hit = 0;
						REP(d, 0, 4){
							PII nxt = seek(i + dir[d][0], j + dir[d][1], d);
							if (nxt != ot) {
								hit = 1;
								break;
							}
						}
						if (!hit) {
							ok = 0;
							break;
						}
					}
					ans++;
				}
			}
			if (!ok) break;
		}
		if (!ok) puts("IMPOSSIBLE");
		else printf("%d\n", ans);
	}
	return 0;
}