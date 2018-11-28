#include <iostream>
#include <string.h>
#include <stdio.h>
using namespace std;
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.txt","w",stdout);
	int x;
	char s[4][4];
	int T[15];
	cin >> x;
	int Xw1 = 'X' + 'X' + 'X' + 'X';
	int Xw2 = 'X' + 'X' + 'X' + 'T';
	int Ow1 = 'O' + 'O' + 'O' + 'O';
	int Ow2 = 'O' + 'O' + 'O' + 'T';
	int z=0;
	while(x--){
		++z;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cin >> s[i][j];
			}
		}
		T[0] = s[0][0] + s[0][1] + s[0][2] + s[0][3];
		T[1] = s[1][0] + s[1][1] + s[1][2] + s[1][3];
		T[2] = s[2][0] + s[2][1] + s[2][2] + s[2][3];
		T[3] = s[3][0] + s[3][1] + s[3][2] + s[3][3];
		T[4] = s[0][0] + s[1][0] + s[2][0] + s[3][0];
		T[5] = s[0][1] + s[1][1] + s[2][1] + s[3][1];
		T[6] = s[0][2] + s[1][2] + s[2][2] + s[3][2];
		T[7] = s[0][3] + s[1][3] + s[2][3] + s[3][3];
		T[8] = s[0][0] + s[1][1] + s[2][2] + s[3][3];
		T[9] = s[0][3] + s[1][2] + s[2][1] + s[3][0];
		bool flagx = 0,flago = 0;
		for(int i=0;i<10;i++){
			if(T[i]== Xw1 || T[i]== Xw2){
				flagx = 1;
				break;
			}
			if(T[i]== Ow1 || T[i]== Ow2){
				flago = 1;
				break;
			}
		}
		if(flagx) printf("Case #%d: X won\n",z);
		else if(flago) printf("Case #%d: O won\n",z);
		else{
			int flag = 0;
			for(int i=0;i<4;i++){
				for(int j=0;j<4;j++){
					if(s[i][j] == '.'){
						flag = 1;
						break;
					}
				}
				if(flag) break;
			}
			if(flag)  printf("Case #%d: Game has not completed\n",z);
			else printf("Case #%d: Draw\n",z);
		}
	}
	return 0;
}
