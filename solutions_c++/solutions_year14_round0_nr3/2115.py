#include<cstdio>
#include<memory.h>
#include<algorithm>
using namespace std;

int H, W;
int minecnt;

int arr[5][5];
bool visited[5][5];
int ci, cj;

void printMap(){
	for(int i = 0; i < H; i++){
		for(int j = 0; j < W; j++){
			if(i== ci && j == cj)
				printf("c");
			else
				printf("%c", arr[i][j] == -1 ? '*' : '.');
		}
		printf("\n");
	}

}

int hasMine(int i, int j){
	if(i < 0 || j < 0 || i >= H || j >= W)
		return 0;
	return arr[i][j] == -1 ? 1 : 0;
}
int runbfs(int, int);
inline int runbfs_unit(int ii, int jj){
	if(ii >= 0 && ii < H && jj >=0 && jj < W)
		if(arr[ii][jj] != -1 && !visited[ii][jj])
			return runbfs(ii, jj);
	return 0;
}
int runbfs(int i, int j){
	visited[i][j] = true;
	int cnt =1;
	if(arr[i][j] == 0){
		for(int ii = -1; ii <= 1; ii++)
			for(int jj = -1; jj <= 1; jj++)
				if(!(ii == 0 && jj == 0))
					cnt += runbfs_unit(i + ii, j + jj);
	}
	return cnt;
}
bool check(){
	int zerocnt= 0, nonzerocnt=  0;
	for(int i = 0; i < H; i++)
		for(int j = 0; j < W; j++){
			if(arr[i][j] != -1){
				arr[i][j] = 0;
				for(int ii = -1; ii <= 1; ii++)
					for(int jj = -1; jj <= 1; jj++)
						if(!(ii == 0 && 0 == jj))
							arr[i][j] += hasMine(i + ii, j + jj);
				if(arr[i][j] == 0)
					zerocnt++;
				else{
					ci = i, cj = j;
					nonzerocnt++;
				}
			}
		}
	if(zerocnt == 0 && nonzerocnt == 1)
		return true;
	else if(zerocnt == 0) return false;
	
	memset(visited, 0, sizeof(visited));
	bool hadrun = false;
	int totcnt = 0;
	for(int i = 0; i < H; i++){
		for(int j =0; j < W; j++){
			if(arr[i][j] == 0 && !visited[i][j]){
				if(hadrun)
					return false;
				totcnt = runbfs(i, j);
				ci = i, cj = j;
				hadrun = true;
			}
		}
	}
	return totcnt == H * W - minecnt;
}

bool rec(int ii, int jj, int cnt){
	if(ii == H && jj == 0){
		if(cnt != minecnt) return false;
		else if(check()){
			return true;
		}
	}
	if((H - ii - 1) * W+ (W - jj) < (minecnt - cnt))
		return false;
	int ni = jj == W - 1 ? ii + 1 : ii;
	int nj = jj == W - 1 ? 0 : jj + 1;
	if(cnt < minecnt){
		if((hasMine(ii - 1, jj + 1) && !hasMine(ii - 1, jj)) || (hasMine(ii - 1, jj - 1) && !hasMine(ii, jj - 1))){
		//	;
		}else{
			arr[ii][jj] = -1;
			if(rec(ni, nj, cnt + 1))
				return true;
			arr[ii][jj] = 0;
		}
	}
	return rec(ni, nj, cnt);
}

int main(){
	int maxtcnt;
	scanf("%d", &maxtcnt);
	for(int tt = 1 ; tt <=maxtcnt; tt++){
		scanf("%d %d %d", &H, &W, &minecnt);
		memset(arr, 0, sizeof(arr));

		bool answ = rec(0, 0, 0);
		printf("Case #%d:\n", tt);
		if(answ == false){
			printf("Impossible\n");
		}else{
			printMap();
		}
	}
	return 0;
}
