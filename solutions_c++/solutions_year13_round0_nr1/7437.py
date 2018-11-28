#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
#include <fstream>
#include <vector>
#include <deque>
#include <cmath>
#include <set>
using namespace std;

char board[5][5];

int judgedir(int si,int sj,int di,int dj){
	int nx=0;
	int no = 0;
	int nt = 0;
	for(int k=0;k<4;++k){
		//cout<<si+di*k<<' '<< sj+dj*k<<' '<<board[si+di*k][sj+dj*k]<<endl;
		switch(board[si+di*k][sj+dj*k]){
		case 'X':
			nx++;
			break;
		case 'O':
			no++;
			break;
		case 'T':
			++nt;
			break;
		default:
			//cout<<"empty"<<endl;
			return 0;
		}
	}
	//cout<<nx<<' '<<no<<' '<<nt<<endl;
	if(nx==4 || (nx==3 && nt==1)) return 1;
	if(no==4 || (no==3 && nt==1)) return -1;
	return 0;
}
int judge(){
	int empty = 0;
	for(int i=0;i<4;++i){
		for(int j=0;j<4;++j){
			if(board[i][j]=='.')
				++empty;
		}
	}
	int res;
	for(int i=0;i<4;++i){
		res = judgedir(i,0,0,1);
		if(res!=0) return res;
	}
	
	for(int j=0;j<4;++j){
		res = judgedir(0,j,1,0);
		if(res!=0) return res;
	}
	res = judgedir(0,0,1,1);
	if(res!=0) return res;
	res = judgedir(0,3,1,-1);
	if(res!=0) return res;
	
	if(empty>0){
		return 2;
	}else {
		return 0;
	}
}
int main(){
	int N;
	cin>>N;
	int nc = 0;
	while(N>0){
		--N;
		++nc;
		for(int i=0;i<4;++i){			
			cin>>board[i];
		}
		
		int res = judge();
		if(res==1){
			printf("Case #%d: X won\n",nc);
		} else if(res==-1){
			printf("Case #%d: O won\n",nc);
		} else if(res==0){
			printf("Case #%d: Draw\n",nc);
		} else {
			printf("Case #%d: Game has not completed\n",nc);
		}
	}
}