#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<stack>

using namespace std;

int** mat;
int emptcnt;

int rowStatus(int num){
    int cunt[4] = {0};
    for(int i=0; i<4; i++){
        cunt[mat[num][i]]++;
    }
    if(cunt[3]>0) emptcnt=1;
    if(cunt[0]==4 || (cunt[0]==3 && cunt[2]==1)) return 0;
    else if(cunt[1]==4 || (cunt[1]==3 && cunt[2]==1)) return 1;
    else return 2;
}

int columnStatus(int num){
    int cunt[4] = {0};
    for(int i=0; i<4; i++){
        cunt[mat[i][num]]++;
    }
    if(cunt[3]>0) emptcnt=1;
    if(cunt[0]==4 || (cunt[0]==3 && cunt[2]==1)) return 0;
    else if(cunt[1]==4 || (cunt[1]==3 && cunt[2]==1)) return 1;
    else return 2;
}

int diagonalStatus(int num){
    int cunt[4] = {0};
    if(num==0){
        for(int i=0; i<4; i++){
            cunt[mat[i][i]]++;
        }
    }
    else{
        for(int i=0; i<4; i++){
            cunt[mat[i][3-i]]++;
        }
    }
    if(cunt[3]>0) emptcnt=1;
    if(cunt[0]==4 || (cunt[0]==3 && cunt[2]==1)) return 0;
    else if(cunt[1]==4 || (cunt[1]==3 && cunt[2]==1)) return 1;
    else return 2;
    
}


int gameStatus(){ //0: X, 1: O, 2: D, 3: N 
    emptcnt=0;
    for(int i=0; i<4; i++){
        int rs = rowStatus(i);
        int cs = columnStatus(i);
        if(rs==0) return 0;
        else if(rs==1) return 1;
        else if(cs==0) return 0;
        else if(cs==1) return 1;
    }
    int d1s = diagonalStatus(0);
    int d2s = diagonalStatus(1);
    if(d1s==0) return 0;
    if(d1s==1) return 1;
    if(d2s==0) return 0;
    if(d2s==1) return 1;
    if(emptcnt>0) return 3;
    else return 2;
}

int mapc(char x){
    if(x=='X') return 0;
    if(x=='O') return 1;
    if(x=='T') return 2;
    if(x=='.') return 3;
}

int main(){
    mat = new int*[4];
    for(int i=0; i<4; i++) mat[i] = new int[4];
    int T;
    scanf("%d", &T);
    string s;
    for(int t=1; t<=T; t++){
        for(int i=0; i<4; i++){
            cin>>s;
            for(int j=0; j<4; j++){
                mat[i][j] = mapc(s[j]);
            }
        }
        int s = gameStatus();
        if(s==0) printf("Case #%d: X won\n", t);
        if(s==1) printf("Case #%d: O won\n", t);
        if(s==2) printf("Case #%d: Draw\n", t);
        if(s==3) printf("Case #%d: Game has not completed\n", t);
    }
    return 0;
}
