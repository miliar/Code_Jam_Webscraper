#include<stdio.h>
#include<stdlib.h>

using namespace std;
char table[4][4];
int  start_x[9][2];
int  start_o[9][2];

bool line(int row,char sim){
	for (int x = 0; x < 4; x++) if ( (sim != table [x][row] ) && ('T' != table [x][row]) ) return false;	
	return true;
}

bool row(int lin,char sim){
	for (int x = 0; x < 4; x++) if ( (sim != table [lin][x]) && ('T' != table [lin][x]) ) return false;	
	return true;
}

bool primary(char sim){
	for (int x = 0; x < 4; x++) if ( (sim != table [x][x]) && ('T' != table [x][x]) ) return false;	
	return true;
}

bool secondary(char sim){
	for (int x = 0; x < 4; x++) if ( (sim != table [(3 - x)][x]) && ('T' != table [(3 - x)][x] )) return false;	
	return true;
}

bool draw(){
	for (int x = 0; x < 4; x++)
	    for (int y = 0 ; y < 4; y++) if ('.' == table[x][y]) return false;
	return true;
}

int main(){
	char c;
	int l,k,m,n;
	bool res = false;	

	scanf("%d\n",&n);
	for (int i = 1; i <= n; i++){
		l = 0 ;
		m = 0;
		for (int k = 0; k < 4; k++)
			for (int j = 0; j <  4; j++){	
				scanf(" %c",&c);
				if ('X' == c){
					start_x[l][0] = k;
					start_x[l++][1] = j;
				} else if('O' == c){
					 start_o[m][0] = k;
					 start_o[m++][1] = j;
					}
				table[k][j] = c;
			}		
		res = false;
		for (int k= 0; k < l; k++){
				int pos_x = start_x[k][0];
				int pos_y = start_x[k][1];
			
					res = line(pos_y,'X');
					if (res) break;
			
					res = row(pos_x,'X');
					if (res) break;

					res = primary('X');
					if (res) break;
		
					res = secondary('X');
					if (res) break;
		}
		if (!res) {
			for (int k= 0; k < m; k++){
				int pos_x = start_o[k][0];
				int pos_y = start_o[k][1];
			
					res = line(pos_y,'O');
					if (res) break;
			
					res = row(pos_x,'O');
					if (res) break;

					res = primary('O');
					if (res) break;
		
					res = secondary('O');
					if (res) break;
			}
			if (!res) {
				res = draw();
				if (res) printf("Case #%d: Draw\n",i);
				else printf("Case #%d: Game has not completed\n",i);
			} else { printf("Case #%d: O won\n",i);}
		} else { printf("Case #%d: X won\n",i);}
	}
}
