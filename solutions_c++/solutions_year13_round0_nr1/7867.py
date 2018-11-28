#include<iostream>

using namespace std;

char tictac[4][4];

struct list{
    int ld,rd,up,lf;
}jb[4][4];

bool valid(int a,int b){
    if(a>=0 && a<4 && b>=0 && b<4) return true;
    return false;
}

void judge(int a,int b){
    if(valid(a-1,b-1)){
        if(tictac[a][b]=='T'){
            jb[a][b].ld = jb[a-1][b-1].ld+1;
        }
        else{
            if(tictac[a][b]==tictac[a-1][b-1] || tictac[a-1][b-1]=='T'){
                if(tictac[a-1][b-1]=='T'){
                    if(valid(a-2,b-2)){
                        if(tictac[a][b]==tictac[a-2][b-2]){
                            jb[a][b].ld = jb[a-1][b-1].ld+1;
                        }
                    }
                }
                else{
                    jb[a][b].ld = jb[a-1][b-1].ld+1;
                }
            }
        }
    }
    if(valid(a-1,b)){
        if(tictac[a][b]=='T'){
            jb[a][b].up = jb[a-1][b].up+1;
        }
        else{
            if(tictac[a][b]==tictac[a-1][b] || tictac[a-1][b]=='T'){
                if(tictac[a-1][b]=='T'){
                    if(valid(a-2,b)){
                        if(tictac[a][b]==tictac[a-2][b]){
                            jb[a][b].up = jb[a-1][b].up+1;
                        }
                    }
                }
                else{
                    jb[a][b].up = jb[a-1][b].up+1;
                }
            }
        }
    }
    if(valid(a-1,b+1)){
        if(tictac[a][b]=='T'){
            jb[a][b].rd = jb[a-1][b+1].rd+1;
        }
        else{
            if(tictac[a][b]==tictac[a-1][b+1] || tictac[a-1][b+1]=='T'){
                if(tictac[a-1][b+1]=='T'){
                    if(valid(a-2,b+2)){
                        if(tictac[a][b]==tictac[a-2][b+2]){
                            jb[a][b].rd = jb[a-1][b+1].rd+1;
                        }
                    }
                }
                else{
                    jb[a][b].rd = jb[a-1][b+1].rd+1;
                }
            }
        }
    }
    if(valid(a,b-1)){
        if(tictac[a][b]=='T'){
            jb[a][b].lf = jb[a][b-1].lf+1;
        }
        else{
            if(tictac[a][b]==tictac[a][b-1] || tictac[a][b-1]=='T'){
                if(tictac[a][b-1]=='T'){
                    if(valid(a,b-2)){
                        if(tictac[a][b]==tictac[a][b-2]){
                            jb[a][b].lf = jb[a][b-1].lf+1;
                        }
                    }
                }
                else{
                    jb[a][b].lf = jb[a][b-1].lf+1;
                }
            }
        }
    }
}

int main(){
    int T,cases = 1;
    cin>>T;
    while(T--){
        bool dotgate = false,xWin=false,oWin=false;
        for(int i=0; i<4; i++){
            for(int j=0; j<4; j++){
                cin>>tictac[i][j];
                if(tictac[i][j]=='.') dotgate = true;
                jb[i][j].ld=jb[i][j].rd=jb[i][j].up=jb[i][j].lf=0;
            }
        }
        for(int i=0; i<4; i++){
            for(int j=0; j<4; j++){
                if(tictac[i][j]!='.'){
                    judge(i,j);
                }
            }
        }
        for(int i=0; i<=3; i++){
            if(jb[i][3].ld==3){
                if(tictac[i][3]=='X') xWin = true;
                if(tictac[i][3]=='O') oWin = true;
                if(tictac[i][3]=='T'){
                    if(tictac[i-1][2]=='X') xWin = true;
                    if(tictac[i-1][2]=='O') oWin = true;
                }
                break;
            }
            if(jb[i][3].lf==3){
                if(tictac[i][3]=='X') xWin = true;
                if(tictac[i][3]=='O') oWin = true;
                if(tictac[i][3]=='T'){
                    if(tictac[i][2]=='X') xWin = true;
                    if(tictac[i][2]=='O') oWin = true;
                }
                break;
            }
        }
        for(int i=0; i<=3; i++){
            if(jb[3][i].rd==3){
                if(tictac[3][i]=='X') xWin = true;
                if(tictac[3][i]=='O') oWin = true;
                if(tictac[3][i]=='T'){
                    if(tictac[2][1]=='X') xWin = true;
                    if(tictac[2][1]=='O') oWin = true;
                }
                break;
            }
            if(jb[3][i].up==3){
                if(tictac[3][i]=='X') xWin = true;
                if(tictac[3][i]=='O') oWin = true;
                if(tictac[3][i]=='T'){
                    if(tictac[2][i]=='X') xWin = true;
                    if(tictac[2][i]=='O') oWin = true;
                }
                break;
            }
        }
        if(xWin) cout<<"Case #"<<cases++<<": X won"<<endl;
        else if(oWin) cout<<"Case #"<<cases++<<": O won"<<endl;
        else if(dotgate) cout<<"Case #"<<cases++<<": "<<"Game has not completed"<<endl;
        else cout<<"Case #"<<cases++<<": Draw"<<endl;
    }
    return 0;
}
