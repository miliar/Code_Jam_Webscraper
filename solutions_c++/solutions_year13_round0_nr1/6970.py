#include <iostream>
using namespace std;

int checkDiag(char arai[4][4], int dir){
    int cX=0,cO=0,idx;
    switch (dir) {
        case 0:
            for(idx=0;idx<4;idx++){
                if(arai[idx][idx] == 'X')
                    cX++;
                else if(arai[idx][idx] == 'O')
                    cO++;
                else if(arai[idx][idx] == 'T'){
                    cO++;
                    cX++;
                }
            }
            break;
        case 1:
            for(idx=0;idx<4;idx++){
                if(arai[idx][3-idx] == 'X')
                    cX++;
                else if(arai[idx][3-idx] == 'O')
                    cO++;
                else if(arai[idx][3-idx] == 'T'){
                    cO++;
                    cX++;
                }
            }
            break;
    }
    if(cX==4) return 0; else if(cO==4) return 1; else return -1;
}

int checkHor(char arai[4][4], int row){
    int cX=0,cO=0,idx;
    for(idx=0;idx<4;idx++){
        if(arai[row][idx] == 'X')
            cX++;
        else if(arai[row][idx] == 'O')
            cO++;
        else if(arai[row][idx] == 'T'){
            cO++;
            cX++;
        }
    }
    if(cX==4) return 0; else if(cO==4) return 1; else return -1;
}

int checkVer(char arai[4][4], int col){
    int cX=0,cO=0,idx;
    for(idx=0;idx<4;idx++){
        if(arai[idx][col] == 'X')
            cX++;
        else if(arai[idx][col] == 'O')
            cO++;
        else if(arai[idx][col] == 'T'){
            cO++;
            cX++;
        }
    }
    if(cX==4) return 0; else if(cO==4) return 1; else return -1;
}

int main() {
    int idx,T,row,col,cX,cO,cT;
    char arai[4][4];
    string msg;
    
    cin >> T;
    for(idx=1;idx<=T;idx++){
        cO=0;
        cX=0;
        cT=0;
        for(row=0;row<4;row++){
            for(col=0;col<4;col++){
                cin >> arai[row][col];
                if(arai[row][col] == 'O') cO++;
                else if(arai[row][col] == 'X') cX++;
                else if(arai[row][col] == 'T') cT++;
            }
        }
        
        //if(strcmp(arai[1][1],arai2[1])==0) cout << "tets" << endl;
        
        if (cX+cO+cT<16) msg="Game has not completed";
        else if(cX+cO+cT==16) msg="Draw";
        
        // check every lines
        int diag0=checkDiag(arai,0);
        int diag1=checkDiag(arai,1);
        int hor0=checkHor(arai,0);
        int hor1=checkHor(arai,1);
        int hor2=checkHor(arai,2);
        int hor3=checkHor(arai,3);
        int ver0=checkVer(arai,0);
        int ver1=checkVer(arai,1);
        int ver2=checkVer(arai,2);
        int ver3=checkVer(arai,3);
        //cout<<cX<<cO<<diag0<<diag1<<hor0<<hor1<<hor2<<hor3<<ver0<<ver1<<ver2<<ver3<<endl;
        
        // if O win
        if(diag0==1 || diag1==1 || hor0==1 || hor1==1 || hor2==1 || hor3==1 || ver0==1 || ver1==1 || ver2==1 || ver3==1)
            msg="O won";
        // if X win
        else if(diag0==0 || diag1==0 || hor0==0 || hor1==0 || hor2==0 || hor3==0 || ver0==0 || ver1==0 || ver2==0 || ver3==0)
            msg="X won";
        
        cout << "Case #" << idx << ": " << msg << endl;
    }
}
