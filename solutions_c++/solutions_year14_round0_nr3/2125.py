#include <algorithm>
#include <bitset>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <iomanip>
#include <iterator>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <string.h>
#include <utility>
#include <vector>
using namespace std;
#define exp 1e-9
#define si 2505
#define inf 0x3f
#define INF 0x3f3f3f3f
#define loop(n) for(int i=0;i<n;i++)
#define period(s,e) for(int i=s;i<=e;i++)
#define min(a,b) a<b?a:b

int R,C, M, dp[si];
char whole[si], mine[si];
bool board[si][si];

int bfs(){

	return true;
} 
bool solve(){
	int side=min(R,C), all=R*C-M, index, finished, row=-1, col=-1, min_sq, cc=C, rr=R, start=0;
	bool br;
	memset(board,false,sizeof(board));
	queue <pair <int, int> > q;
	if(all==0)
		return false;

	if(all==1){
	}else if((all==3 || all==2) && C==2 && R==2){
		return false;
	}
	else{
		index=lower_bound(dp,dp+50,all)-dp;
		if(all!=dp[index] || (index+1)<=C || (index+1)<=R){
			if(all<4 && all>1)
				return false;
			if(all-4==1)
				return false;
			if(all%R==(1) && all%C==(1) && (C==2 || R==2))
				return false;
			if((all%R==(R-1) && C==2 && all>R) || (all%C==(C-1) && R==2 && all>C))
				return false;
		}
		while(all>2){
			for(int i=cc, j=rr;i>0 && j>0;){
				if(i*j<=all && all-i*j!=1){
					if(start==1)
						return false;
					if(i==1)
						return false;
					col=i;
					row=j;
					q.push(make_pair(i,j));
					break;
				}
				if((i-1)*j>(i*(j-1))){
					if(i*(j-1)<=all && all-i*(j-1)!=1 && !(i-(all-i*(j-1))>=2 && start==0 && j==2) && j-1!=0){
						if(start==1)
							return false;
						if(i==1)
							return false;
						col=i;
						row=j-1;
						q.push(make_pair(i,j-1));
						break;
					}
					else
						i--;
				}
				else{
					j--;
				}

			}

			if(col!=-1 && row!=-1){
				for(int i=start;i<start+row;i++)
					fill(board[i],board[i]+col,true);
				all-=col*row;
				start+=row;
			}

			cc=col-1;
			rr=R-row;

		}
		if(all==1 || col==-1 || row==-1)
			return false;
		if(all==2)
			board[start][0]=board[start][1]=true;
	}


	for(int i=0;i<R;i++){
		for(int j=0;j<C;j++){
			if(i==0 && j==0){
				printf("c");
				continue;
			}
			if(board[i][j])
				printf(".");
			else
				printf("*");
		}
		printf("\n");
	}
	return true;
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("cfg.in", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	loop(50){
		dp[i]=(i+1)*(i+1);
	}
	int T, remain;
	char tmp[si];
	fill(whole,whole+si,'.');
	fill(mine,mine+si,'*');
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		scanf("%d%d%d",&R,&C, &M);
		printf("Case #%d:\n",t);
		if(((R==1 || C==1) && R*C-1<M))
			printf("Impossible\n");
		else if(R!=1 && C!=1){
			if(!solve()){
				printf("Impossible\n");
			};
		}else if(R==1){
			printf("c");
			remain=C-M-1;
			strncpy(tmp,whole,remain);
			tmp[remain]='\0';
			printf("%s",tmp);
			strncpy(tmp,mine,M);
			tmp[M]='\0';
			printf("%s\n",tmp);
		}else{
			printf("c\n");
			remain=R-M-1;
			loop(remain)
				printf(".\n");
			loop(M)
				printf("*\n");
		}
	}



	return 0;
}