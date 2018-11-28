#include <stdio.h>
#include <stdlib.h>
int checkWin(char player,char Board[4][5]){
    int winFlag = 0;
    int checkFlag;
    //row
    for( int i=0; i<4; i++ ){
        checkFlag = 1;
        for( int j=0; j<4; j++){
            if( Board[i][j]!=player && Board[i][j]!='T' ){
                checkFlag = 0;
                break;
            }
        }
        if( checkFlag == 1 ){
            return 1;
        }
    }
    //col
    for( int i=0; i<4; i++ ){
        checkFlag = 1;
        for( int j=0; j<4; j++){
            if( Board[j][i]!=player && Board[j][i]!='T' ){
                checkFlag = 0;
                break;
            }
        }
        if( checkFlag == 1 ){
            return 1;
        }
    }
    //dig
    int start[2][2] = { { 0 , 0 } ,
                        { 0 , 3 } };
    int dir[2][2] = { { 1 , 1 } ,
                      { 1 , -1 } };
    for( int i=0; i<2; i++){
        checkFlag = 1;
        for( int j=0; j<4; j++){
            if( Board[ start[i][0] + dir[i][0]*j ][ start[i][1] + dir[i][1]*j ]!=player
             && Board[ start[i][0] + dir[i][0]*j ][ start[i][1] + dir[i][1]*j ]!='T' ){
                checkFlag = 0;
                break;
            }
        }
        if( checkFlag == 1 ){
            return 1;
        }
    }

}

int checkFull(char Board[4][5]){
    for(int i=0; i<4; i++){
        for(int j=0; j<4; j++){
            if( Board[i][j] == '.' ){
                return 0;
            }
        }
    }
    return 1;
}

int main(void){
    int Total;
    int r;
    char inBoard[4][5];
    char tmp[10];
    scanf("%s\n",tmp);
    sscanf( tmp,"%d",&Total);
    //scanf("");
    //printf("!T!%x!\n",Total);
    //printf("!tmp!%s\n",tmp);
    for( r=1; r<=Total; r++ ){
        //get input board
        for( int i=0; i<4; i++){
            //scanf("%s\n",inBoard[i]);
            gets( inBoard[i] );
            //printf("!B!%s!\n", inBoard[i] );
        }
        gets( tmp );
        //printf("!tmp!%s!\n", tmp );

        printf("Case #%d: ", r);
        if( checkWin('X',inBoard) == 1 ){
            printf("X won\n");
        }
        else if( checkWin('O',inBoard) == 1 ){
            printf("O won\n");
        }
        else if( checkFull( inBoard ) ){
            printf("Draw\n");
        }
        else {
            printf("Game has not completed\n");
        }

    }
    return 0;
}
