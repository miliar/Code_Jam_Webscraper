#include "stdio.h"
#include "string.h"
#include <algorithm>
#include <queue>
#include <map>
#include <iostream>
#include <vector>
#include <string>
using namespace std;
int N,M;
int board[105][105];
void Check(){
	int maxH[2][105];
	memset(maxH,0,sizeof(maxH));
	for(int i=0;i<N;i++){
		for(int j=0;j<M;j++){
			if(board[i][j]>maxH[0][i])
				maxH[0][i]=board[i][j];
			if(board[i][j]>maxH[1][j])
				maxH[1][j]=board[i][j];
		}
	}
	for(int i=0;i<N;i++){
		for(int j=0;j<M;j++){
			if(board[i][j]==maxH[0][i]) continue;
			if(board[i][j]==maxH[1][j]) continue;
			bool ok=true;
			for(int ii=1;ii<M;ii++){
				if(board[i][ii]!=board[i][ii-1])
					ok=false;
			}
			if(ok) continue;
			ok=true;
			for(int ii=1;ii<N;ii++){
				if(board[ii][j]!=board[ii-1][j])
					ok=false;
			}
			if(!ok){
				printf("NO\n");
				return;
			}
		}
	}
	printf("YES\n");
}
int main(){
	freopen("D:\\Test\\in.txt","r",stdin);
	freopen("D:\\Test\\out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		scanf("%d %d",&N,&M);
		for(int i=0;i<N;i++)
			for(int j=0;j<M;j++){
				scanf("%d",&board[i][j]);
			}

		printf("Case #%d: ",t);
		Check();
	}
    return 0;
}