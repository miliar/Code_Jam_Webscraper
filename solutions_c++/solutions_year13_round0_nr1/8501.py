#include<stdio.h>
int main(){
    char board[4][4], aux;
    int t, test_n=1;
    int i, j;
    int result=3; //0-X won | 1-O won | 2-draw | 3-not ended
    bool jump=false;
    bool can_b_draw=true;
    scanf("%d", &t);
    for(test_n=1;test_n<=t;test_n++){
        result=3;
        can_b_draw=true;
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                scanf(" %c", &board[i][j]);
                if(board[i][j] == '.')can_b_draw=false;
                //printf("i=%d, j=%d ", i, j);
            }
        }
        //colunas
        for(i=0;i<4;i++){
            aux=board[i][0];
            if(aux =='T') aux=board[i][1];
            if(aux == '.') continue;
            for(j=1;j<4;j++){
                if(board[i][j] != aux && board[i][j] != 'T'){
                    jump=true;
                    break;
                }
            }
            if(jump){
                jump=false;
                continue;
            }
            if(j>=4){
                if(aux == 'X') result=0;
                else result=1;
                break;
            }
        }
        //linhas
        if(result==3) for(j=0;j<4;j++){
            aux=board[0][j];
            if(aux =='T') aux=board[1][j];
            if(aux == '.') continue;
            for(i=1;i<4;i++){
                if(board[i][j] != aux && board[i][j] != 'T'){
                    jump=true;
                    break;
                }
            }
            if(jump){
                jump=false;
                continue;
            }
            if(i>=4){
                if(aux == 'X') result=0;
                else result=1;
                break;
            }
        }
        //diagonal
        if(result==3){
            aux=board[0][0];
            if(aux =='T') aux=board[1][1];
            if(aux == '.') aux='N';
            if(aux == board[1][1] && aux == board[2][2] && aux == board[3][3]){
                if(aux == 'X') result=0;
                else result=1;
            }
            
            aux=board[3][0];
            if(aux =='T') aux=board[2][1];
            if(aux == '.') aux='N';
            if(aux == board[2][1] && aux == board[1][2] && aux == board[0][3]){
                if(aux == 'X') result=0;
                else result=1;
            }
        }    
        
        if(result==3 && can_b_draw == true) result=2;
        printf("Case #%d: ",test_n);
        if(result==0){
            printf("X won");
        }
        else if(result==1){
            printf("O won");
        }
        else if(result==2){
            printf("Draw");
        }
        else if(result==3){
            printf("Game has not completed");
        }
        printf("\n");
        
    }
}
    
