#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <ctype.h>
#include <limits.h>
#include <queue>
using namespace std;
	


int r,c,m;
int flag;
int map[55][55];
int visit[55][55];

int dir[][2]={{-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}};
int record[300];
int bx,by;
int mcount;
int cc;

void print(){
	printf("Case #%d:\n",cc);
	int i,j;
	for(i=1;i<=r;i++){
		for(j=1;j<=c;j++){
			if(i==bx && j==by && r*c-m!=1)
				printf("c");
			else if(map[i][j]==9)
				printf("*");
			else {
				if(r*c-m==1)
					printf("c");
				else 
					printf(".");
			}
		}
		printf("\n");
	}
}

void update(){
	int i,j;
	for(i=0;i<r*c;i++){
		if(record[i]==9){
			int row=i/c+1;
			int col=i%c+1;
			map[row][col]=9;
			for(j=0;j<8;j++){
				if(map[row+dir[j][0]][col+dir[j][1]]!=9)
					map[row+dir[j][0]][col+dir[j][1]]++;
			}
		}
	}
}

int travel(int row,int col){
	queue<pair<int ,int> > mqueue;
	mqueue.push(pair<int,int>(row,col));
	while(!mqueue.empty() && mcount!=r*c-m){
		row=mqueue.front().first;
		col=mqueue.front().second;
		mqueue.pop();
		for(int i=0;i<8;i++){
			int rr=row+dir[i][0];
			int cc=col+dir[i][1];
			if(rr>=1 && rr<=r && cc>=1 && cc<=c){
				if(!visit[rr][cc]){
					visit[rr][cc]=1;
					mcount++;
					if(map[rr][cc]==0 )
					mqueue.push(pair<int,int>(rr,cc));
				}
			
			}
		}
	}
	if(mcount==r*c-m){
		print();
		return 1;
	}else
		return 0;
}

int isok(){
	int i,j;
	int ff=1;
	for(i=1;i<=r;i++){
		for(j=1;j<=c;j++)
			if(map[i][j]==0){
				ff=0;
				break;
		}
		if(!ff)
			break;
	}
	if(!ff){
		bx=i;
		by=j;
		visit[i][j]=1;
		mcount=1;
		if(travel(i,j))
			return 1;
		else
			return 0;
	}
	if(r*c-m==1){
		print();
		return 1;
	}
	return 0;
}

int cmp(int a,int b){
	return a>b;
}

int main(){
	freopen("C:\\Users\\jason\\Downloads\\C-small-attempt1.in","r",stdin);
	freopen("C:\\Users\\jason\\Downloads\\out.txt","w",stdout);
	int t;
	int i;
	scanf("%d",&t);
	for(cc=1;cc<=t;cc++){
		scanf("%d %d %d",&r,&c,&m);
		flag=0;		
		
		memset(record,0,sizeof(record));
		for(i=0;i<m;i++)
			record[i]=9;
		do{
			memset(map,0,sizeof(map));
			memset(visit,0,sizeof(visit));
			update();
			if(isok()){
				flag=1;
				break;
			}
		}while(next_permutation(record,record+r*c,cmp));
		if(!flag)
			printf("Case #%d:\nImpossible\n",cc);
	}
	return 0;
}

/*
	if(mcount==r*c-m){
		print();
		return 1;
	}
	if(map[row][col]!=0)
		return 0;
	else{
		for(int i=0;i<8;i++){
			int rr=row+dir[i][0];
			int cc=col+dir[i][1];
			if(!visit[rr][cc]){
				visit[rr][cc]=1;
				mcount++;
				if(map[rr][cc]==0)
					dfs(rr,cc);
			}
		}
	}
	return 0;

*/