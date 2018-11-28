#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;
bool checkWin(std::string str, int boardCount);
int main( int argc, char * argv[]){

    FILE *fp;
    fp = fopen("input.dat","r");
    if(fp == NULL){
        printf("Error opening input.dat\n");
        return(1);
    }
    char board[4][4];
    int totalBoardCount = -1;
    fscanf(fp,"%d\n",&totalBoardCount);
    fprintf(stderr,"%d\n",totalBoardCount);
    int x_count = 0;
    int y_count = 0;
    int t_count = 0;
    int dot_count = 0;
    int lineCount = 0;    
    int boardCount = 0;
    start:
    while(boardCount < totalBoardCount){   
        lineCount = 0;           
        x_count = 0;
        y_count = 0;
        t_count = 0;
        dot_count = 0;
        while(lineCount < 4){

            fscanf(fp,"%c%c%c%c\n",&board[lineCount][0],&board[lineCount][1],&board[lineCount][2],&board[lineCount][3]);
            lineCount ++;
            
        }
        boardCount ++;
        fprintf(stderr,"Board %d\n",boardCount);
        for(int i = 0; i < 4; i ++){
            for(int j = 0; j < 4; j++){
                if(board[i][j] == 'X')
                    x_count ++; 
                else if(board[i][j] == 'Y')
                    y_count ++;
                else if(board[i][j] == 'T')
                    t_count ++;
                else if(board[i][j] == '.')
                    dot_count ++;
             }
        }

        //printf("X Count %d Y Count %d\n",x_count,y_count);
        if(x_count < 4 && y_count < 4 && t_count == 0){
            printf("Case #%d: Game has not completed\n",boardCount);
            lineCount = 0;
            //boardCount ++;
            goto start;
        }         
       
        /*for(int i = 0; i < 4; i ++){

            printf("%c%c%c%c\n",board[i][0],board[i][1],board[i][2],board[i][3]);

        }*/

        for(int i = 0; i < 4; i ++){   
            std::string current_board;
            for(int j = 0; j < 4; j ++){
                current_board += board[i][j];
            }
            if(checkWin(current_board,boardCount))
                goto start;
        }
        


        for(int i = 0; i < 4; i ++){   
            std::string current_board;
            for(int j = 0; j < 4; j ++){
                current_board += board[j][i];
            }
            if(checkWin(current_board,boardCount))
                goto start;
        }


        std::string current_board;
        for(int i = 0, j = 0; i < 4; i ++, j ++){   
            current_board += board[j][i];
        }
        if(checkWin(current_board,boardCount))
                goto start;


        current_board.clear();
        for(int i = 0, j = 3; i < 4; i ++, j --){   
            current_board += board[i][j];
        }
        if(checkWin(current_board,boardCount))
                goto start;
        
        if(dot_count != 0){
             printf("Case #%d: Game has not completed\n",boardCount);
        }
        else{
            printf("Case #%d: Draw\n",boardCount);
        }
        
        lineCount = 0;
        //boardCount ++;
       
    }
}

bool checkWin(std::string str,int boardCount){
    //std::cout << "Checking String " << str << std::endl;
    unsigned fi = str.find(".");
    if(!fi == std::string::npos){
            fprintf(stderr,"Found a \".\"\n");
            return false;
    }else if(str.compare("XXXX") == 0){
        printf("Case #%d: X won\n",boardCount);
        //std::cout << str << std::endl;
        return true;
    }else if(str.compare("XXXT") == 0){
        printf("Case #%d: X won\n",boardCount);
        //std::cout << str << std::endl;
        return true;
    }else if(str.compare("XXTX") == 0){
        printf("Case #%d: X won\n",boardCount);
        //std::cout << str << std::endl;
        return true;
    }else if(str.compare("XTXX") == 0){
        printf("Case #%d: X won\n",boardCount);
        //std::cout << str << std::endl;
        return true;
    }else if(str.compare("TXXX") == 0){
        printf("Case #%d: X won\n",boardCount);
        //std::cout << str << std::endl;
        return true;
    }else if(str.compare("OOOO") == 0){
        printf("Case #%d: O won\n",boardCount);
        //std::cout << str << std::endl;
        return true;
    }else if(str.compare("OOOT") == 0){
        printf("Case #%d: O won\n",boardCount);
        //std::cout << str << std::endl;
        return true;
    }else if(str.compare("OOTO") == 0){
        printf("Case #%d: O won\n",boardCount);
        //std::cout << str << std::endl;
        return true;
    }else if(str.compare("OTOO") == 0){
        printf("Case #%d: O won\n",boardCount);
        //std::cout << str << std::endl;
        return true;
    }else if(str.compare("TOOO") == 0){
        printf("Case #%d: O won\n",boardCount);
        //std::cout << str << std::endl;
        return true;
    }else{
        return false;
    }
}

