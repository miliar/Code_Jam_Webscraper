#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <cstring>

using namespace std;

const int N = 4;

int map[N][N];
int n;
int ans = 0;
int now = 0;

bool vised[N];
bool oped[N];

bool test(int x){
	if (x == n)
		return true;
	bool res = false;
	for (int i = 0; i < n; i++)
		if (!vised[i]){
			vised[i] = true;
			for (int j = 0; j < n; j++)
				if (map[i][j] && !oped[j]) {
					oped[j] = true;
					if (!test(x + 1)) 
						return false;
					res = true;
					oped[j] = false;
				}
			vised[i] = false;
		}
	return res;
}

void dfs(int x){
	if (now > ans) return;
	if (x == n) {
		memset(vised,0,sizeof(vised));
		memset(oped,0,sizeof(oped));
		if (test(0)) 
			ans = now;
		return ;
	}
	for (int i = 0; i < 1 << n; i++){
		for (int j = 0; j < n; j++){
			if ((i >> j & 1) && !map[x][j]){
				map[x][j] = 2; now++;
			}
		}
		dfs(x + 1);
		for (int j = 0; j < n; j++) if (map[x][j] == 2) {
			map[x][j] = 0; now --;
		}
	}
}
char buf[255];
int main() {
	freopen("D.in", "r", stdin);
	freopen("D.out", "w", stdout);

	int t;
	scanf("%d", &t);
	for (int cas = 1; cas <= t; cas++){
		printf("Case #%d: ", cas);
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			scanf("%s", buf);
			for (int j = 0; j < n; j++){
				map[i][j] = buf[j] == '1';
			}
		}
		ans = 0x7fffffff; now = 0;
		dfs(0);
		printf("%d\n", ans);
		// a,b,c,d --> j
		// |a| <= 4 or |b| <= 4 or |c| <= 4 or |d| <= 4
	}
}