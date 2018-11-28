//
//  main.cpp
//  tictactoeCodejam
//
//  Created by Fahim Chandurwala on 4/13/13.
//  Copyright (c) 2013 Fahim Chandurwala. All rights reserved.
//

#include <iostream>
#define ROW 0
#define COL 1
#define DIAG1 2
#define DIAG2 3
class tictac{
public:
    unsigned char d1[4];
    FILE* fpin;
    FILE* fpout;
    int cases;

    unsigned char token;
    unsigned char* board;
    unsigned char acase[16];

    int GameStatus(){
        int result;
        std::cout<<"Output\n\n";
        for (int casenum= 0;casenum < this->cases; casenum++) {
            result = caseStatus(casenum);
            switch (result) {
                case -1:
                    fprintf(this->fpout,"Case #%d: Game has not completed\n",casenum+1);
                    std::cout<<"case# "<<casenum+1<<": Game has not completed"<<std::endl;
                    break;
                case 0:
                    fprintf(this->fpout,"Case #%d: Draw\n",casenum+1);
                    std::cout<<"case# "<<casenum+1<<": draw"<<std::endl;
                    break;
                case 1:
                    fprintf(this->fpout,"Case #%d: X won\n",casenum+1);
                    std::cout<<"case# "<<casenum+1<<": X won"<<std::endl;
                    break;
                case 2:
                    fprintf(fpout,"Case #%d: O won\n",casenum+1);
                    std::cout<<"case# "<<casenum+1<<": O won"<<std::endl;
                    break;
                    
                default:
                    break;
            }

        }
        fclose(this->fpout);
        return 1;
    }
    int caseStatus(int caseNum){
        int res;
        bool incomplete;
        for (int at = 0; at<4; at++) {
            switch (at) {
                case ROW:
                    for (int i = 0; i < 4; i++) {
                        res = arrayStatus(caseNum, at, i);
                        if (res>0) {
                            return res;
                        }
                        if (res==-1) {
                            incomplete = true;
                        }
                    }
                    
                    break;
                case COL:
                    for (int i = 0; i < 4; i++) {
                        res = arrayStatus(caseNum, at, i);
                        if (res>0) {
                            return res;
                        }
                        if (res ==-1) {
                            incomplete = true;
                        }
                    }
                    break;
                case DIAG1:
                    res =arrayStatus(caseNum, at, 0);
                    if (res>0) {
                        return res;
                    }
                    if (res ==-1) {
                        incomplete = true;
                    }
                    break;
                case DIAG2:
                    res = arrayStatus(caseNum, at, 0);
                    if (res>0) {
                        return res;
                    }
                    if (res) {
                        incomplete = true;
                    }
                    break;
                default:
                    break;
            }
            
        }
        if (incomplete) {
            return -1;
        }
        return 0;
    }
    int arrayStatus(int caseNum,int arrayType,int elem)
    {
        int x = 0,o = 0;
        int countX=0,countO = 0,countT = 0;
        unsigned const char* a =NULL;
        unsigned char array[4];
        a = getArray(caseNum, arrayType, elem);
        for (int i = 0; i < 4; i++) {
            array[i] = *a;
            a++;
        }
        //std::cout<<"\nans->"<<array<<std::endl;
        for (int i = 0; i<4; i++) {
            if (array[i] == 'X') {
                countX++;
                //std::cout<<" X-> "<<array[i]<<" "<<countX<<" ";
            }
            if (array[i] == 'O') {
                countO++;
                //std::cout<<" X-> "<<array[i]<<" "<<countX<<" ";
            }
            if (array[i] == 'T') {
                countT++;
                //std::cout<<" T-> "<<array[i]<<" "<<countX<<" ";
            }
            if (array[i] == '.') {
                //std::cout<<" Dot-> "<<array[i]<<" "<<countX<<" ";
                return -1;
            }
   

        }
        x = countX + countT;
        o = countO + countT;
        if (x==4) {
            x=0;
            countT=0;
            countX =0;
            countO =0;
            return 1;
        }
        if (o==4) {
            o=0;
            x=0;
            countT=0;
            countX =0;
            countO =0;
            return 2;
        }

        return 0;
    }
    
    unsigned char* getArray(int caseNum,int c,int elem){
        int offset = caseNum*16;
        unsigned char array[4];
        switch (c) {
            case DIAG1:
                //d1
                for (int i = 0; i < 4; i++) {
                    array[i] = this->board[offset + 4*i + i];
                }

                break;
            case DIAG2:
                //d2
                for (int i = 0; i < 4; i++) {
                    array[i] = this->board[offset + 4*i + (4-i-1)];

                }
                break;
            case ROW:
                //row
                for (int i = 0; i < 4; i++) {
                    array[i] = this->board[offset + 4*elem + i];
                    
                }
                break;
            case COL:
                //col
                for (int i = 0; i < 4; i++) {
                    array[i] = this->board[offset + 4*i + elem];


                }
                break;
            default:
                break;
        }
        return array;
    }
        
    tictac(const char* filepathIn,const char* filepathOut){
        this->fpin = fopen(filepathIn, "r");
        this->fpout = fopen(filepathOut, "w");
        if (this->fpin != NULL) {
            fscanf(this->fpin, "%i",&this->cases);
            //printf("%i\n",this->cases);
            this->board = (unsigned char*)malloc((this->cases)*16);
            for (int i = 0; i < cases; i++) {
                fscanf(this->fpin, "%c",&this->token);
                fscanf(this->fpin, "%4c",&this->board[0+16*i]);
                fscanf(this->fpin, "%c",&this->token);
                fscanf(this->fpin, "%4c",&this->board[4+16*i]);
                fscanf(this->fpin, "%c",&this->token);
                fscanf(this->fpin, "%4c",&this->board[8+16*i]);
                fscanf(this->fpin, "%c",&this->token);
                fscanf(this->fpin, "%4c",&this->board[12+16*i]);
                fscanf(this->fpin, "%c",&this->token);
            }
            //std::cout<<board<<std::endl;
        }
        fclose(this->fpin);
        this->GameStatus();

    };
private:
    
    
    
};

int main(int argc, const char * argv[])
{

    // insert code here...
    fopen("/Users/fchandur/Desktop/ticSol.txt", "w");
    tictac *t;
    t = new tictac("/Users/fchandur/Desktop/tic.txt","/Users/fchandur/Desktop/ticSol.txt");
    //t->GameStatus();


    
    return 0;
}

