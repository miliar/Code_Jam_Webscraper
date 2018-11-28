#include <cstdio>

int grid[105][105];
int max[105];

int N,M;

int max_row(int r){
	int i;
	int m = 0;
	for(i=0;i<M;++i)
		if(grid[r][i]>m) m = grid[r][i];
	return m;
}

int max_col(int c){
	int i;
	int m = 0;
	for(i=0;i<N;++i)
		if(grid[i][c]>m) m = grid[i][c];
	return m;
}

bool check_row(int r){
	int m = max_row(r);
	int i;
	for(i=0;i<M;++i)
		if(grid[r][i]<m && grid[r][i]<max[i]) return false;
	return true;
}

const char* check(){
	int i,m;
	for(i=0;i<M;++i){
		max[i] = max_col(i);
	}
	for(i=0;i<N;++i){
		if(! check_row(i)) return "NO";
	}
	return "YES";
}

int main(){
	int T,t,i,j;
	scanf("%d", &T);
	for(t=0;t<T;++t){
		scanf("%d %d", &N, &M);
		for(i=0;i<N;++i)
			for(j=0;j<M;++j)
				scanf("%d", &grid[i][j]);
		printf("Case #%d: %s\n", t+1, check());
	}
	return 0;
}
