#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

int getRes(string ip[]);

int main( )
{
	int t,T;
	int p,q;
	string ip[4];
	string temp;
	int res;
	
	scanf("%d",&T);
	
	for(int t=1;t<=T;t++){
		
		for(int i=0;i<4;i++){
			cin>>ip[i];
		}
		getline(cin,temp);
		
		p = 5;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(ip[i][j]=='T') {
					p = i;
					q = j;
				}
			}
		}
		
		if(p==5){
			res = getRes(ip);
		} else {
			ip[p][q] = 'X';
			res = getRes(ip);
			if( res < 2 ) {
				ip[p][q] = 'O';
				res = getRes(ip);
			}
		}
		
		switch ( res ) {
			case 0:
				printf("Case #%d: Draw\n",t);
				break;
			case 1:				
				printf("Case #%d: Game has not completed\n",t);
				break;
			case 2:
				printf("Case #%d: X won\n",t);
				break;
			case 3:
				printf("Case #%d: O won\n",t);
				break;
		}
	}	
	
	return 0;
}

int getRes(string ip[])
{
	for(int i=0;i<4;i++){
		// check horizontal
		if( ip[i][0] == ip[i][1] && ip[i][1] == ip[i][2] && ip[i][2] == ip[i][3] ) {
			if( ip[i][0]=='X') {
				return 2;
			}
			if( ip[i][0]=='O') {
				return 3;
			}
		}
		
		// check vertical 
		if( ip[0][i] == ip[1][i] && ip[1][i] == ip[2][i] && ip[2][i] == ip[3][i] ) {
			if( ip[0][i]=='X') {
				return 2;
			}
			if( ip[0][i]=='O') {
				return 3;
			}
		}
	}
	
	// check diagonal 1 
	if( ip[0][0] == ip[1][1] && ip[1][1] == ip[2][2] && ip[2][2] == ip[3][3] ) {
		if( ip[0][0]=='X') {
			return 2;
		}
		if( ip[0][0]=='O') {
			return 3;
		}
	}
	
	// check diagonal 2
	if( ip[3][0] == ip[2][1] && ip[2][1] == ip[1][2] && ip[1][2] == ip[0][3] ) {
		if( ip[3][0]=='X') {
			return 2;
		}
		if( ip[3][0]=='O') {
			return 3;
		}
	}
	
	// check for incomplete game
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			if(ip[i][j]=='.'){
				return 1;
			}
		}
	}
	
	// by default return draw
	return 0;
}

