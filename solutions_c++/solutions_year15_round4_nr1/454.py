#include <stdio.h>
#define MAXN 100

char map[MAXN][MAXN+1];
int dir(char c){
	switch(c){
		case '.':
			return -1;
		case '>':
			return 0;
		case 'v':
			return 1;
		case '<':
			return 2;
		case '^':
			return 3;
	}
}
bool check(int x,int y,int n,int m,int d){
	int dx[4] = {0, 1, 0, -1};
	int dy[4] = {1, 0, -1, 0};
	x += dx[d], y += dy[d];
	while( x < n && y < m && x >= 0 && y >= 0){
		if( map[x][y] != '.' )
			return 1;
		x += dx[d], y += dy[d];
	}
	return 0;
}

int main(){
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;++t){
		int n, m;
		scanf("%d%d",&n,&m);
		for(int i=0;i<n;++i)
			scanf("%s", map[i]);
		
		int ans = 0;
		bool pos = 1;
		for(int i=0;i<n;++i){
			for(int j=0;j<m;++j){
				if( map[i][j] == '.' )
					continue;
				bool yes[4] = {0};
				for(int k=0;k<4;++k)
					yes[k] = check(i,j,n,m,k);
				//printf("dir(map[%d][%d]) = %d\n", i,j, dir(map[i][j]));
				if( yes[dir(map[i][j])] == 0 ){
					//printf("%d%d\n", i,j);
					if( yes[0]+yes[1]+yes[2]+yes[3] == 0 )
						pos = 0;
					else
						++ans;
				}
			}
		}
		if( pos ) printf("Case #%d: %d\n", t, ans);
		else printf("Case #%d: IMPOSSIBLE\n", t);
	}
	return 0;	
}
