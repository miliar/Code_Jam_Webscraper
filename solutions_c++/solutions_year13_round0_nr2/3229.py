#include <stdio.h>

int n, m;
int grid[128][128];

bool checkrow(int i, int me){
	int j;
	for(j=0;j<m;j++)
		if(grid[i][j] > me)
			return false;
	return true;
}
bool checkcol(int j, int me){
	int i;
	for(i=0;i<n;i++)
		if(grid[i][j] > me)
			return false;
	return true;
}
void solve(){
	int i, j;
	scanf("%d %d", &n, &m);
	for(i=0;i<n;i++){
		for(j=0;j<m;j++)
			scanf("%d", &grid[i][j]);
	}

	for(i=0;i<n;i++){
		for(j=0;j<m;j++){
			if(!checkrow(i, grid[i][j]) && !checkcol(j, grid[i][j])){
				printf("NO");
				return;
			}
		}
	}
	printf("YES");
	return;
}

int main(int argc, char *argv[]){
	int t, T;
	scanf("%d", &T);
	for(t=1;t<=T;t++){
		printf("Case #%d: ", t);
		solve();
		printf("\n");
	}
	return 0;
}
