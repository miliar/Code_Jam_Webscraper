#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define WIDTH (4)
#define HEIGHT (4)
#define PLAYERS (2)
#define PLAYER_O 0
#define PLAYER_X 1

char board[PLAYERS][WIDTH][HEIGHT];
char inputCount=0;

void inputProcess()
{
    int x,y;
    char data[128];
    
    inputCount = 0;
    for(y=0; y < HEIGHT ;  y++ ){
        scanf("%s", data );
        for(x=0; x < WIDTH ;  x++ ){
            switch (data[x]) {
                case 'O':
                    board[PLAYER_O][x][y] = 1;
                    inputCount++;
                    break;
                case 'X':
                    board[PLAYER_X][x][y] = 1;
                    inputCount++;
                    break;
                case 'T':
                    board[PLAYER_O][x][y] = 1;
                    board[PLAYER_X][x][y] = 1;
                    inputCount++;
                    break;
                default:
                    break;
            }
        }
    }
}

int checkLine(char b[][HEIGHT],int sx,int sy,int isrow)
{
    int x,y;
    
    if( isrow ){
        y = sy;
        for( x=0 ; x < WIDTH ; x++){
            if ( b[x][y] == 0 ){
                return 0;
            }
        }
    }else{
        x = sx;
        for( y=0 ; y < HEIGHT ; y++){
            if ( b[x][y] == 0 ){
                return 0;
            }
        }
    }
    return 1;
}

int checkDiagonal(char b[][HEIGHT], int order)
{
    int x,y;
 
    if ( order ){
        for(x=0,y=0; x < WIDTH && y < HEIGHT ; x++,y++ ){
            if ( b[x][y] == 0 ){
                return 0;
            }
        }
    }else{
        for(x=WIDTH-1,y=0; x >= 0 && y < HEIGHT ; x--,y++ ){
            if ( b[x][y] == 0 ){
                return 0;
            }
        }
    }
    return 1;
}

int checkWinner(char b[][HEIGHT] )
{
    int x,y;
    
    //row
    for(y=0; y < HEIGHT ;  y++ ){
        if ( checkLine(b, 0, y, 1) ){
            return 1;
        }
    }

    //column
    for(x=0; x < WIDTH ;  x++ ){
        if ( checkLine(b, x, 0, 0) ){
            return 1;
        }
    }
    if ( checkDiagonal(b,0) )
        return 1;
    if ( checkDiagonal(b,1) )
        return 1;
    
    return 0;
}


int main(void)
{
	int testcases;
    
	scanf("%d",&testcases);
	for(int testcase = 1; testcase <= testcases; testcase ++){
        memset( board , 0, sizeof(board) );
        inputProcess();
        
        printf("Case #%d: ",testcase);
        if ( checkWinner( board[PLAYER_O] ) ){
            printf( "O won\n");
        }else if( checkWinner( board[PLAYER_X] ) ){
            printf( "X won\n");
        }else if( inputCount==(WIDTH*HEIGHT) ){
            printf( "Draw\n");
        }else{
            printf( "Game has not completed\n");
        }
	}
	return 0;
}