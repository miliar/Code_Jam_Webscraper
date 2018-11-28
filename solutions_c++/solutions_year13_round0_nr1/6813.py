#include <stdio.h>
#include <string.h>
using namespace std;
char table[5][5];
bool hor(int i, char p){
	if((table[i][0]==p || table[i][0]=='T') && (table[i][1]==p || table[i][1]=='T') && (table[i][2]==p || table[i][2]=='T') && (table[i][3]==p || table[i][3]=='T')) return true;
	return false;
}
bool ver(int i, char p){
	if((table[0][i]==p || table[0][i]=='T') && (table[1][i]==p || table[1][i]=='T') && (table[2][i]==p || table[2][i]=='T') && (table[3][i]==p || table[3][i]=='T')) return true;
	return false;
}
int main(){
	int t;
	freopen("A-large.in", "r", stdin);
	freopen("output.out", "w", stdout);
	scanf("%d", &t);
	for(int ind=1; ind<=t; ind++){
		printf("Case #%d: ", ind);
		for(int i=0; i<4; i++) scanf("%s", table[i]);
		bool empty_sq=false;
		for(int i=0; i<4; i++){
			for(int j=0; j<4; j++){
				if(table[i][j]=='.'){
					empty_sq=true;
					i=4;
					break;
				}
			}
		}
		bool win=false;
		if((table[0][0]=='X' || table[0][0]=='T') && (table[1][1]=='X' || table[1][1]=='T') && (table[2][2]=='X' || table[2][2]=='T') && (table[3][3]=='X' || table[3][3]=='T')){
			printf("X won\n");
			continue;
		}else if((table[0][0]=='O' || table[0][0]=='T') && (table[1][1]=='O' || table[1][1]=='T') && (table[2][2]=='O' || table[2][2]=='T') && (table[3][3]=='O' || table[3][3]=='T')){
			printf("O won\n");
			continue;
		}else if((table[3][0]=='X' || table[3][0]=='T') && (table[2][1]=='X' || table[2][1]=='T') && (table[1][2]=='X' || table[1][2]=='T') && (table[0][3]=='X' || table[0][3]=='T')){
			printf("X won\n");
			continue;
		}else if((table[3][0]=='O' || table[3][0]=='T') && (table[2][1]=='O' || table[2][1]=='T') && (table[1][2]=='O' || table[1][2]=='T') && (table[0][3]=='O' || table[0][3]=='T')){
			printf("O won\n");
			continue;
		}else{
			for(int i=0; i<4; i++){	
				if(hor(i,'X') || ver(i,'X')){
					printf("X won\n");
					win=true;
					break;
				}else if(hor(i,'O') || ver(i,'O')){
					printf("O won\n");
					win=true;
					break;
				}
			}
			if(!win && empty_sq) printf("Game has not completed\n");
			else if(!win) printf("Draw\n");
		}
	}
	return 0;
}
			
		