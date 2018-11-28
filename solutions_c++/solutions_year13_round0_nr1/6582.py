#include <iostream>

#define STATUS1 1
#define STATUS2 2
#define STATUS3 3
#define STATUS4 4


/*
1. check col win,
2. check row win,
3. check diag win,
4. check more move state
*/

int getResult(char m[4][4]){
        int val = 4, space = 0;;
        int xrow1 =0, orow1 = 0, trow1 = 0;
        int xrow2 =0, orow2 = 0, trow2 = 0;
        int xrow3 =0, orow3 = 0, trow3 = 0;
        int xrow4 =0, orow4 = 0, trow4 = 0;
/*
XOXT
XOXO
OXOT
XOXO
*/
        //row
        for(int i=0;i<4;i++){
                for(int j=0;j<4;j++){
                        if(m[i][j]=='.') space++;
                        if(m[i][j]=='X') xrow1++;
                        if(m[i][j]=='O') orow1++;
                        if(m[i][j]=='T') trow1++;
                        /////////////////
                        if(m[j][i]=='X') xrow4++;
                        if(m[j][i]=='O') orow4++;
                        if(m[j][i]=='T') trow4++;

                        if(i==j){ // diag r->l
                                if(m[i][j]=='X') xrow2++;
                                if(m[i][j]=='O') orow2++;
                                if(m[i][j]=='T') trow2++;
                        }
                        if(i+j==3){//diag l -> r
                                if(m[i][j]=='X') xrow3++;
                                if(m[i][j]=='O') orow3++;
                                if(m[i][j]=='T') trow3++;
                        }

                }
                if((xrow1==3 && trow1>0)|| xrow1==4){ return STATUS1; }
                if((orow1==3 && trow1>0)|| orow1==4){ return STATUS2; }
                xrow1 = orow1 = trow1 = 0;
                if((xrow4==3 && trow4>0)|| xrow4==4){ return STATUS1; }
                if((orow4==3 && trow4>0)|| orow4==4){ return STATUS2; }
                xrow4 = orow4 = trow4 = 0;
        }
        if((xrow2==3 && trow2>0)|| xrow2==4){ return STATUS1; }
        if((orow2==3 && trow2>0)|| orow2==4){ return STATUS2; }
        if((xrow3==3 && trow3>0)|| xrow3==4){ return STATUS1; }
        if((orow3==3 && trow3>0)|| orow3==4){ return STATUS2; }
        //here means no one has win .. check for more move or say draw
        if(space > 0) return STATUS4;
        return 3;
}

int results(char m[4][4], std::string &result){
        int bit = 0;
        bit = getResult(m);
        switch(bit){
                case STATUS1:
                                result = "X won";
                                break;
                case STATUS2:
                                result = "O won";
                                break;
                case STATUS3:
                                result = "Draw";
                                break;
                case STATUS4:
                                result = "Game has not completed";
                                break;
        }
        return 1;
}

int main(int argc, char **argv){

        int T = 0;
        std::string result("");
        std::cin>>T;
        char matrix[4][4] = {0};
        for(int i =0; i < T; i++){
                for(int j =0; j<4;j++){
                        for(int k=0;k<4;k++){
                                std::cin>>matrix[j][k];
                        }
                }
                /*std::cout<<"Inputs #"<<i+1<<std::endl;
                for(int j =0; j<4;j++){
                        for(int k=0;k<4;k++){
                                std::cout<<matrix[j][k];
                        }
                        std::cout<<std::endl;
                }*/
                results(matrix,result);
                std::cout<<"Case #"<<i+1<<": "<<result<<std::endl;
                result = "";
        }
}
