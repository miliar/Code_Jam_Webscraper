#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>

using namespace std;

#define FOE(i, s, t) for (int i = s; i <= t; i++)

int r, c;
int a[1001][1001];

int dx[5] = {0, -1, 0, 1}, dy[5] = {-1, 0, 1, 0};


void solve(){
	scanf("%d%d", &r, &c);
	FOE(i, 1, r){
		string x;
		cin>>x;
		FOE(j, 1, c) if (x[j-1] == '.') a[i][j] = -1;
		else if (x[j-1] == '^') a[i][j] = 1;
		else if (x[j-1] == '<') a[i][j] = 0;
		else if (x[j-1] == '>') a[i][j] = 2;
		else a[i][j] = 3;
	}

	int cnt = 0;

	FOE(i, 1, r) FOE(j, 1, c) if (a[i][j] != -1){
		int cx = i + dx[a[i][j]], cy = j + dy[a[i][j]];
		while (cx >= 1 && cx <= r && cy >= 1 && cy <= c && a[cx][cy] == -1){
			cx = cx + dx[a[i][j]];
			cy = cy + dy[a[i][j]];
		}
		if (cx < 1 || cx > r || cy < 1 || cy > c){
			cnt++;
			int ok = 0;
			FOE(k, 0, 3){
				int cx = i + dx[k], cy = j + dy[k];
				while (cx >= 1 && cx <= r && cy >= 1 && cy <= c && a[cx][cy] == -1){
					cx += dx[k];
					cy += dy[k];
				}
				if (cx >= 1 && cx <= r && cy >= 1 && cy <= c) ok++;
			}
			if (!ok){
				puts("IMPOSSIBLE");
				return;
			}
		}
	}
	printf("%d\n", cnt);
}

int main(){
	int t;
	scanf("%d", &t);
	for (int i = 1 ;i <= t; i ++){
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}
