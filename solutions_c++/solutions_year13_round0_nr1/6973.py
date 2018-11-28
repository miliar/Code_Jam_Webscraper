#include<cstdio>
#include<algorithm>

#define XWIN 1
#define YWIN 2
#define DRAW 3

#define XX 0
#define YY 1
#define Tnum 2 
#define DOT 3

using namespace std;

char board[4][4];
char in[10];

int row[4][4];
int col[4][4];
int d[2][4];

int t;
int CT;

int main(){
    scanf("%d", &t);	
	CT = 0;
	while(t--){
		for(int i = 0; i < 4; ++i){
			scanf("%s", in);
			for(int j = 0; j < 4; ++j){
				board[i][j] = in[j];
			}
		}
   
    for(int i = 0; i < 4; ++i){
	    fill(row[i], row[i]+4, 0);
	    fill(col[i], col[i]+4, 0);
	}
	fill(d[0], d[0]+4, 0);
	fill(d[1], d[1]+4, 0);

	bool has_dot = false;

    for(int i = 0; i < 4; ++i){
		for(int j = 0; j < 4; ++j){
		    if(board[i][j] == 'X'){
				row[i][XX]++;
				col[j][XX]++;
				if(i == j)
				    d[0][XX]++;
				if( i+j == 3)
				    d[1][XX]++;
			} else if (board[i][j] == 'O') {
				row[i][YY]++;
				col[j][YY]++;
				if(i == j)
				    d[0][YY]++;
				if( i+j == 3)
				    d[1][YY]++;
			} else if (board[i][j] == '.'){
			    has_dot = true;
				row[i][DOT]++;
				col[j][DOT]++;
				if(i == j)
				    d[0][DOT]++;
				if( i+j == 3)
				    d[1][DOT]++;
			} else {
				row[i][Tnum]++;
				col[j][Tnum]++;
				if(i == j)
				    d[0][Tnum]++;
				if( i+j == 3)
				    d[1][Tnum]++;
			}
		}
	}

	int result = DRAW;

	for(int i = 0; i < 4; ++i){
	    if(row[i][DOT] == 0){
		    if(row[i][XX] + row[i][Tnum] == 4){
				result = XWIN;
				break;
			} else if(row[i][YY] + row[i][Tnum] == 4){
				result = YWIN;
				break;
			} 
		}

	    if(col[i][DOT] == 0){
		    if(col[i][XX] + col[i][Tnum] == 4){
				result = XWIN;
				break;
			} else if(col[i][YY] + col[i][Tnum] == 4){
				result = YWIN;
				break;
			} 
		}
	}

    if(result == DRAW){
		
	if(d[0][DOT] == 0){
	    if(d[0][XX] + d[0][Tnum] == 4){
			result = XWIN;
		} else if(d[0][YY] + d[0][Tnum] == 4){
			result = YWIN;
		} 
	}

	if(d[1][DOT] == 0){
	    if(d[1][XX] + d[1][Tnum] == 4){
			result = XWIN;
		} else if(d[1][YY] + d[1][Tnum] == 4){
			result = YWIN;
		} 
	}
	}
    
	printf("Case #%d: ", ++CT);
	if(result == DRAW){
	    if(has_dot){
		    printf("Game has not completed\n");	
		} else {
		    printf("Draw\n");	
		}
	} else if( result == XWIN ) {
	     printf("X won\n");	
	} else {
	     printf("O won\n");	
	}
	
    }
}
