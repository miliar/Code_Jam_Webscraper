#include<iostream>
#include<cstdio>
#include<cstdlib>
using namespace std;
int winCount = 4;
void declXWin(int c){
    char buffer[64];
    sprintf(buffer, "Case #%d: X won\n", c);
    cout<<buffer;
}

void declOWin(int c){
    char buffer[64];
    sprintf(buffer, "Case #%d: O won\n", c);
    cout<<buffer;
}

void draw(int c){
    char buffer[64];
    sprintf(buffer, "Case #%d: Draw\n", c);
    cout<<buffer;    
}

void notCompleted(int c){
    char buffer[64];
    sprintf(buffer, "Case #%d: Game has not completed\n", c);
    cout<<buffer;
}

void print(int arr[][4]){
    for(int i = 0; i < winCount; i++){
        for(int j = 0; j < winCount; j++){
            cout<<arr[i][j]<<" ";
        }
        cout<<endl;
    }
}

bool check(int xc, int oc, int c){
    if(xc == winCount){
        declXWin(c);
        return true;
    }
    else if(oc == winCount){
        declOWin(c);
        return true;
    }
    return false;   
}

int main(){
    int xc = 0, oc = 0, dxc = 0, doc = 0;
    int c, buffer[26];
    bool zeroSeen = false;
    // read test case count.
    cin>>c;
    int i = 1, row = 4, col = 4;
    char sym;
    scanf("%c", &sym);
    while(i <= c){
    int X[4][4] = {0};
    int O[4][4] = {0};
    zeroSeen = false;
        for(int j = 0; j < row + 1; j++){
            for(int k = 0; k < col + 1; k++){
                //sym = buffer[j * (winCount+1) + k];
                scanf("%c", &sym);
                //cout<<sym;
                if(sym == '\n' && k == col){
                    break;
                }
                else{
                    if(sym == 'X')
                        X[j][k] = 1;
                    else if(sym == 'O'){
                        O[j][k] = 1;
                    }
                    else if(sym == 'T'){
                        X[j][k] = O[j][k] = 1;
                    }
                    else{
                        X[j][k] = O[j][k] = 0;
                        zeroSeen = true;
                    }
                }
            }            
            if(sym == '\n' && j == row - 1){
                break;
            }
        }
        //execcise newline.
        scanf("%c", &sym);
        
        //cout<<"X: "<<endl;
        //print(X);
        //cout<<endl<<"O: "<<endl;
        //print(O);
        
        // row wise checking.
        for(int j = 0; j < row; j++){
            xc = oc = 0;
            for(int k = 0; k < col; k++){
                xc += X[j][k];
                oc += O[j][k];
                //if((oc + xc) < winCount)
                  //  zeroSeen = true;
            }
            if(check(xc, oc, i))
                goto INCR;
        }
        // column wise counting.
        for(int j = 0; j < row; j++){
            xc = oc = 0;
            for(int k = 0; k < col; k++){
                xc += X[k][j];
                oc += O[k][j];
                //if((oc + xc) < winCount)
                    //zeroSeen = true;
            }
            if(check(xc, oc, i))
                goto INCR;
        }
        // check diagonally from left.
        xc = oc = 0;
        for(int j = 0; j < row; j++){
            xc += X[j][j];
            oc += O[j][j];
            //if((oc + xc) < winCount)
                //zeroSeen = true;
        }
        if(check(xc, oc, i))
            goto INCR;
        // check diagonally from right.
        xc = oc = 0;
        for(int j = 0, k = row - 1; j < row; j++, k--){
            xc += X[j][k];
            oc += O[j][k];
            //if((oc + xc) < winCount)
                //zeroSeen = true;            
        }
        if(check(xc, oc, i))
            goto INCR;
        if(zeroSeen){
            notCompleted(i);
        }
        else{
            draw(i);
        }
        INCR:
            i++;
    }
    return 0;
}
