// GJ 2014 C
// minesweeper

#include <iostream>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <algorithm>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
using namespace std;


int N;
int cases;
int R,C,M;
int finalR,finalC;// how small the board is left behind
char pattern[60][60];

void prepPattern(){

	for(int i=1; i <= R; i++){
		for(int j=1; j <=C; j++){
			pattern[i][j]='.';
		}
	}
	
	pattern[1][1]='c';
}
void printPattern(){
	
	for(int i=1; i <=R; i++){
		for(int j=1; j <=C; j++){
			printf("%c",pattern[i][j]);
		}
		printf("\n");
	}
}

void fillRM(int r, int n, int m){
	for(int i=n-m+1; i <=n; i++){
		pattern[r][i]='*';
	}
}
void fillCM(int c, int n, int m){
	for(int i=n-m+1; i <=n; i++){
		pattern[i][c]='*';
	}
}


void cut(int r1, int c1, int r2, int c2){
	for(int i=r1; i <= r2; i++){
		for(int j=c1; j <=c2; j++){
			pattern[i][j]='*';
		}
	}
}


bool solve(int r, int c, int m){
	//printf("solve(%d,%d,%d)\n",r,c,m);
	
	if(r==1){	// a straight line
		return false;
	}
	if(c==1){
		return false;
	}
	if(m==0)return true;
	if(r==2 && c==2){
		if(m==0){
			return true;
		}else{
			return false;
		}
	}
	if(r==2 && c==3){
		if(m==2){
			fillCM(3,2,2);
			return true;
		}else{
			return false;
		}
	}
	if(r==3 && c==2){
		if(m==2){
			fillRM(3,2,2);
			return true;
		}else{
			return false;
		}
	}
	if(r>c){		// vertical rectangle
		if(m>=c){
			cut(r,0,r,c);
			return solve(r-1,c,m-c);			// cut the lowest strip
		}else{		// really need to plan
			if(c-m>=2){	// if one row can satisfy
				fillRM(r,c,m);
				return true;
			}else{
				fillRM(r,c,c-2);
				return solve(r-1,c,m-c+2);
			}
		}
	}else{		// horizontal rectangle
		if(m>=r){
			cut(0,c,r,c);
			return solve(r,c-1,m-r);			// cut the right most strip
		}else{		// really need to plan
			if(r-m>=2){	// if one row can satisfy
				fillCM(c,r,m);
				return true;
			}else{
				fillCM(c,r,r-2);
				return solve(r,c-1,m-r+2);
			}
		}
	}
}

bool soolve(int r, int c, int m){
	if(R*C-M==7)return false;
	if(r*c-m==1){
		for(int i=1; i <= R; i++){
			for(int j=1; j <=C; j++){
				pattern[i][j]='*';
			}
		}
		pattern[1][1]='c';
		return true;
	}
	if(r==1){	// a straight line
		fillRM(R,C,M);
		return true;
	}
	if(c==1){
		fillCM(C,R,M);
		return true;
	}
	if(r==2 && c==2){
		if(m==0){
			return true;
		}else{
			return false;
		}
	}
	if(r==2 && c==3){
		if(m==2){
			fillCM(3,2,2);
			return true;
		}else{
			return false;
		}
	}
	if(r==3 && c==2){
		if(m==2){
			fillRM(3,2,2);
			return true;
		}else{
			return false;
		}
	}
	return solve(r,c,m);
}

int main(){

	freopen("C-small-attempt02.in","r",stdin);
	freopen("C-small-attempt02.out","w",stdout);

	cin >> N;
	cases=0;
	cin.ignore();
	while(N--){
		cases++;
		
		scanf("%d %d %d",&R, &C, &M);
		prepPattern();
		printf("Case #%d:\n",cases);

		if(M==0 || soolve(R,C,M)){
			// print result
			printPattern();
		}else{
			printf("Impossible\n");
		}

	}


	return 0;
}