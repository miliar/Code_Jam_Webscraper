//============================================================================
// Name        : Code_jam_Problem.cpp
// Author      : mahfuz
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include<cstdio>
using namespace std;
char board[10][10] ;
bool in_line(int n,int m){
	if(n<0 || n>=4 ||m<0 ||m>=4) return false ;
	return true ;
}

bool check_row(int p,int q){
	for(int i=1;i<4;i++){
		if(in_line(p,q+i) && board[p][q+i]=='T') continue ;
		if(!in_line(p,q+i) ||board[p][q+i]!=board[p][q]) return false;

	}
	return true ;
}
bool check_hor(int p,int q){
	for(int i=1;i<4;i++){
		if(in_line(p+i,q) && board[p+i][q]=='T') continue ;
		if(!in_line(p+i,q) || board[p+i][q]!=board[p][q]) return false;
	}
	return true ;
}
bool check_dia(int p,int q){
	for(int i=1;i<4;i++){
		if(in_line(p+i,q+i) && board[p+i][q+i]=='T') continue ;
		if(!in_line(p+i,q+i) || board[p+i][q+i]!=board[p][q]) return false;
	}
	return true ;
}
bool check_row_r(int p,int q){
	for(int i=1;i<4;i++){
		if(in_line(p,q-i) && board[p][q-i]=='T') continue ;
		if(!in_line(p,q-i) ||board[p][q-i]!=board[p][q]) return false;

	}
	return true ;
}
bool check_hor_r(int p,int q){
	for(int i=1;i<4;i++){
		if(in_line(p-i,q) && board[p-i][q]=='T') continue ;
		if(!in_line(p-i,q) || board[p-i][q]!=board[p][q]) return false;
	}
	return true ;
}
bool check_dia_r(int p,int q){
	for(int i=1;i<4;i++){
		if(in_line(p+i,q-i) && board[p+i][q-i]=='T') continue ;
		if(!in_line(p+i,q-i) || board[p+i][q-i]!=board[p][q]) return false;
	}
	return true ;
}

int main() {

	freopen("//home//mazhar//Desktop//in.txt","r",stdin) ;


	int caseno ;
	bool draw ,res;
	scanf("%d",&caseno) ;
	for(int kase=1;kase<=caseno;kase++){
		printf("Case #%d: ",kase) ;
		draw=false ;
		res=true ;
		for(int i=0;i<4;i++) scanf("%s",board[i]) ;
		for(int i=0;i<4 && res;i++){
			for(int j=0;j<4 && res;j++){
				if(board[i][j]=='.')      draw=true ;
				else if(board[i][j]=='T') continue ;
				else if(check_row(i,j) ||check_hor(i,j) ||check_dia(i,j)){
					if(board[i][j]=='X') cout<<"X won"<<endl ;
					else cout<<"O won"<<endl ;
					res=false;
				}
				else if(check_row_r(i,j) ||check_hor_r(i,j) ||check_dia_r(i,j)){
					if(board[i][j]=='X') cout<<"X won"<<endl ;
								else cout<<"O won"<<endl ;
								res=false;

				}
			}
		}
		if(res){
			if(draw) printf("Game has not completed\n") ;
			else printf("Draw\n") ;
		}

	}



	return 0;
}
