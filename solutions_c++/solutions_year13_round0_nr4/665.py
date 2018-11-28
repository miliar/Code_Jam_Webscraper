#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <cstdlib>
#include <map>
#include <queue>

#define LL long long int
#define FOR(i, s, e) for (int i=(s);i<(e);i++)
#define FOE(i, s, e) for (int i=(s);i<=(e);i++)
#define FOD(i, s, e) for (int i=(e)-1;i>=(s);i--)
#define CLR(x, a) memset(x, a, sizeof(x))

#define M 205
#define N 50
using namespace std;

int testcase;
int n, NK, keys[M], type[N], door[N][N];
int f[1<<22], next[1<<22], x, y, dq[N];

int F(int state){
	if (state == (1<<n) - 1) return 1;
	if (f[state] != -1) return f[state];
	
	int cur[M];
	CLR(cur, 0);
	
	FOR(i, 0, M) cur[i] = keys[i];
	FOR(i, 0, n)
		if ((1<<i) & state){
			cur[type[i]]--;
			FOR(j, 0, dq[i]) cur[door[i][j]]++;
		}
	
	FOR(i, 0, n){
		if ((1<<i) & state) continue;
		if (cur[type[i]] == 0) continue;
		int new_state = state | (1<<i);
		if (F(new_state)){
			next[state] = i;
			f[state] = 1;
			return 1;
		}
	}
	
	f[state] = 0;
	return 0;
}

int main(){
	scanf("%d", &testcase);
	FOR(TC, 0, testcase){
		CLR(keys, 0);
		CLR(door, 0);
		
		scanf("%d%d", &NK, &n);
		FOR(i, 0, NK){
			scanf("%d", &y);
			keys[y]++;
		}
		
		FOR(i, 0, n){
			scanf("%d%d", &type[i], &dq[i]);
			FOR(j, 0, dq[i]) scanf("%d", &door[i][j]);
		}
		
		CLR(f, -1);
		if (F(0)){
			printf("Case #%d:", TC + 1);
			x = 0;
			FOR(i, 0, n){
				printf(" %d", next[x] + 1);
				x += (1<<next[x]);
			}
			printf("\n");
		}
		else printf("Case #%d: IMPOSSIBLE\n", TC + 1);
	}
	return 0;
}
