#include<cstdio>
#include<iostream>
#include<cstring>
#include<vector>

using namespace std;

int T,n,m;
char mat[105][105];
int cnt[105][105];
bool vis[105][105];
bool cyc[105][105];
bool in[105][105];
int dr[]={0,-1,0,1};
int dc[]={-1,0,1,0};
char dir[300];

int dfs(int r, int c) {
	vis[r][c] = 1;
	in[r][c] = 1;

	int ret = 1;
	int meet = 0;
	for(int k=1;k<=100;++k) {
		int nr = r + dr[ dir[mat[r][c]] ] * k;
		int nc = c + dc[ dir[mat[r][c]] ] * k;
		if(nr < 0 || nr >= n) continue;
		if(nc < 0 || nc >= m) continue;
		if(mat[nr][nc] != '.' && in[nr][nc]) {
			cyc[r][c] = true;
			break;
		}
		if(mat[nr][nc] != '.') {
			if(!vis[nr][nc]) {
				ret = dfs(nr,nc);
				cyc[r][c] = cyc[nr][nc];
				break;
			}
			else {
				meet = 1;
				cyc[r][c] = cyc[nr][nc];
				break;
			}
		}
	} in[r][c] = 0;
	if(cyc[r][c] || meet) return 0;
	return ret;
}

int main() {
	dir['^'] = 1;
	dir['>'] = 2;
	dir['v'] = 3;
	dir['<'] = 0;
	scanf("%d",&T);
	for(int cs=1;cs<=T;++cs) {
		printf("Case #%d: ",cs);
		memset(cnt,0,sizeof(cnt));
		memset(vis,0,sizeof(vis));
		memset(cyc,0,sizeof(cyc));
		memset(in,0,sizeof(in));
		scanf("%d%d",&n,&m);
		for(int i=0;i<n;++i) scanf("%s",mat[i]);
		for(int i=0;i<n;++i) for(int j=0;j<m;++j) if(mat[i][j] != '.') {
			int dt = dir[mat[i][j]];
			for(int k=1;k<=100;++k) {
				int ni = i + dr[dt] * k;
				int nj = j + dc[dt] * k;
				if(ni < 0 || ni >= n) continue;
				if(nj < 0 || nj >= m) continue;
				cnt[ni][nj]++;
				if(mat[ni][nj] != '.') break;
			}
		}
		bool no = false;
		int ans = 0;
		for(int i=0;i<n;++i) for(int j=0;j<m;++j) if(mat[i][j] != '.' && cnt[i][j] == 0 && !vis[i][j]) {
			
			bool have = false;
			for(int k=0;k<4;++k) {
				for(int t=1;t<=100;++t) {
					int ni = i + dr[k] * t;
					int nj = j + dc[k] * t;
					if(ni < 0 || ni >= n) continue;
					if(nj < 0 || nj >= m) continue;
					if(mat[ni][nj] != '.') have = true;
				}
			}
			if(!have) no = true;
			ans += dfs(i,j);
		}
		if(no) printf("IMPOSSIBLE\n");
		else printf("%d\n",ans);
	}
}
