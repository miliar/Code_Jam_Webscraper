#include<stdio.h>
#include<stdlib.h>
#define SIZE 4
char board[4][4];

int checkLRDiagonalX();
int checkLRDiagonalO();
int checkRLDiagonalO();
int checkRLDiagonalX();
int checkRowsX();
int checkRowsO();
int checkColsX();
int checkColsO();
int checkIncomplete();
void initializeBoard();
int main(){
    FILE* in = fopen("A-large.in", "r");
    FILE*out = fopen("output.txt", "w");
    
    char sym, space;
    int i, j, T, t;
    
    fscanf(in, "%d", &T);
    fscanf(in, "%c", &space);
    for(t=0; t<T; t++){
             initializeBoard();
             //read from file.
              for(i =0; i <SIZE; i++){
                    for(j = 0; j <SIZE; j++){
                          fscanf(in, "%c", &sym);
                          board[i][j] = sym;
                          //printf("%c ", board[i][j]);
                    }  
                    fscanf(in, "%c", &space);
                   // printf("\n");      
              }
              
              fscanf(in, "%c", &sym);
             
              if(checkLRDiagonalX() || checkRLDiagonalX() || checkRowsX() ||checkColsX()){
                                    //printf("Case #%d: X won\n", t+1);  
                                    fprintf(out,"Case #%d: X won\n", t+1);                     
              }
              else if(checkLRDiagonalO() || checkRLDiagonalO() || checkRowsO() ||checkColsO()){
                   fprintf(out, "Case #%d: O won\n", t+1);                      
              }
              else if(checkIncomplete()){
                   fprintf(out, "Case #%d: Game has not completed\n", t+1);   
              }
              else if(!checkIncomplete()){
                    fprintf(out, "Case #%d: Draw\n", t+1);
              }
    }
    system("pause");
    return 0;    
}

int checkLRDiagonalX(){
    int i, count_X=0;
    
    for(i = 0; i <SIZE; i++){  
                if(board[i][i] == 'X' || board[i][i]=='T'){
                               count_X++;               
                }  
    }
    if(count_X == SIZE)return 1;
    return 0;
}
void initializeBoard(){
     int i, j;
      for(i =0; i <SIZE; i++){
                    for(j = 0; j <SIZE; j++){
                          board[i][j] = '.';
                    }      
              }   
}

int checkLRDiagonalO(){
    int i, count_O=0;
    
    for(i = 0; i <SIZE; i++){  
                if(board[i][i] == 'O' || board[i][i]=='T'){
                               count_O++;               
                }  
    }
    if(count_O == SIZE)return 1;
    return 0;
}

int checkRLDiagonalX(){
    int i, count_X=0;
    
    for(i=0; i <SIZE; i++){  
                if(board[i][(SIZE-1)-i] == 'X' || board[i][(SIZE-1)-i]=='T'){
                               count_X++;               
                }  
    }
    if(count_X == SIZE)return 1;
    return 0;
}

int checkRLDiagonalO(){
    int i, count_O=0;
    
    for(i = 0; i <SIZE; i++){  
                if(board[i][(SIZE-1)-i] == 'O' || board[i][(SIZE-1)-i]=='T'){
                               count_O++;               
                }  
    }
    if(count_O == SIZE)return 1;
    return 0;
}

int checkRowsX(){
    int i , j, count_X=0;
    
    for(i=0; i <SIZE; i++){
              
             count_X=0;
             for(j = 0; j <SIZE; j++){
                  if(board[i][j] == 'X' || board[i][j]=='T'){
                             count_X++;   
                  }
                  
                
             }
           //  printf("Row %d: %d\n",i+1, count_X);
             if(count_X==SIZE){return 1;}  
                                
    }
    return 0;
}

int checkRowsO(){
    int i , j, count_O=0;
    
    for(i=0; i <SIZE; i++){
             count_O=0;
             for(j = 0; j <SIZE; j++){
                  if(board[i][j] == 'O' || board[i][j]=='T'){
                               count_O++; 
                               if(count_O==SIZE){return 1;}              
                }
             }                      
    }
    return 0;
}

int checkColsX(){
    int i, j, count_X=0;
     for(i=0; i <SIZE; i++){
             count_X=0;
             for(j = 0; j <SIZE; j++){
                  if(board[j][i] == 'X' || board[j][i]=='T'){
                               count_X++; 
                               if(count_X==SIZE){return 1; }             
                }
             }                      
    }
    return 0;
}

int checkColsO(){
    int i, j, count_O=0;
     for(i=0; i <SIZE; i++){
             count_O=0;
             for(j = 0; j <SIZE; j++){
                  if(board[j][i] == 'O' || board[j][i]=='T'){
                               count_O++; 
                               if(count_O==SIZE){return 1;}              
                }
             }                      
    }
    return 0;
}

int checkIncomplete(){
    int i, j;
    for(i=0; i <SIZE; i++){
             for(j = 0; j <SIZE; j++){
                  if(board[i][j]== '.'){
                              return 1;              
                }
             }                      
    } 
    return 0;   
}
