#include <iostream>
#include <stdio.h>

using namespace std;

#define FOR(i,a,b) for(int i=a; i<=b ; i++)
#define REP(i,n) FOR(i,0,n-1)
#define MIN 1000000009
#define INF 1000000010
#define MOD 1000000007

typedef long int LL;
typedef unsigned int uint;
typedef unsigned long int ULL;

char matrix[4][4];
char dummy;

inline void fastRead(int *a){
 register char c=0;
 while (c<33) c=getchar_unlocked();
 *a=0;
 while (c>33)
 {
     *a=*a*10+c-'0';
     c=getchar_unlocked();
 }
}

void intialize(){
	REP(i,4){
		scanf("%c",&dummy);
		REP(j,4){
			scanf("%c",&matrix[i][j]);
		}
	}
}
// 0 for x win , 1 for O win 2 for DRAW , 3 for Not completed 
int solve(){  
	char check1,check2,count_row, count_column;
	// horizontal and vertical
	REP(i,4){
		count_row =0;
		count_column = 0;
		check1 = matrix[i][0];
		check2 = matrix[0][i];
		if(matrix[i][0] == 'T')
			check1 = matrix[i][1];
		if(matrix[0][i] == 'T')
			check2 = matrix[1][i];
		REP(j,4){
			if(matrix[i][j] == check1 || matrix[i][j] == 'T')
				count_row++;
			if(matrix[j][i] == check2 || matrix[j][i] == 'T')
				count_column++;
		}
		if(count_row == 4){
			switch(check1){
				case 'X' : return 0;
				case 'O' : return 1;
				default: break;
			}
		}
		if(count_column == 4){
			switch(check2){
				case 'X' : return 0;
				case 'O' : return 1;
				default: break;
			}
		}
	}
	// diagonal
	count_row = 0;
	count_column = 0;
	check1 = matrix[0][0];
	check2 = matrix[0][3];
	if(matrix[0][0] == 'T')
		check1 = matrix[3][3];
	if(matrix[0][3] == 'T')
		check2 = matrix[3][0];
	REP(i,4){
		if(matrix[i][i] == check1 || matrix[i][i] == 'T')
			count_row++;
		if(matrix[3-i][i] == check2 || matrix[3-i][i] == 'T')
			count_column++;		
	}
	if(count_row == 4){
		switch(check1){
			case 'X' : return 0;
			case 'O' : return 1;
			default: break;
		}
	}
	else if(count_column == 4){
		switch(check2){
			case 'X' : return 0;
			case 'O' : return 1;
			default: break;
		}
	}

	// blank check
	REP(i,4)
	REP(j,4){
		if(matrix[i][j] == '.')
			return 3;
	}
	return 2;
}
int main(){
	int t;
	int count = 0;
	int result;
	scanf("%d",&t);
	while(t--){
		count++;
		intialize();
		result = solve();
		printf("Case #%d: ",count);
		switch(result){
			case 0: printf("X won\n");
					break;
			case 1: printf("O won\n"); break;
			case 2: printf("Draw\n"); break;
			case 3: printf("Game has not completed\n"); break;
			default : break;
		}
		scanf("%c",&dummy);
	}
	return 0;
}