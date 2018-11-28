#include<iostream>
#include<string>
using namespace std;

const int PlayerO = 1;
const int PlayerX = 2;
int main(int argc, char* argv[]){
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++){
        char board[4][4];
        for(int i=0;i<4;i++) cin >> board[i];
        
        bool contable= false;
        bool next = false;
        
        // row
        for(int k=0;k<4;k++){
            bool miss=false;
            char check = ' ';
            for(int i=0;i<4;i++){
                if(board[k][i]=='T')continue;
                else if(board[k][i]=='.') {
                    contable=true;
                    miss=true;
                    break;
                }
                else if (check == ' ') {
                    check = board[k][i];                    
                }
                else if (board[k][i] != check) {
                    miss = true;
                    break;
                }
            }
            if(!miss){
                cout << "Case #" << t << ": " << check << " won" << endl;
                next = true;
                break;
            }
        }
        if(next) continue;
        next=false;
        
        // col
        for(int k=0;k<4;k++){
            bool miss=false;
            char check = ' ';
            for(int i=0;i<4;i++){
                if(board[i][k]=='T')continue;
                else if(board[i][k]=='.') {
                    contable=true;
                    miss=true;
                    break;
                }
                else if (check == ' ') {
                    check = board[i][k];
                }
                else if (board[i][k] != check) {
                    miss = true;
                    break;
                }
            }
            if(!miss){
                cout << "Case #" << t << ": " << check << " won" << endl;
                next = true;
                break;
            }
        }
        if(next) continue;
        next=false;

        // X
        for(int k=0;k<2;k++){
            bool miss=false;
            char check = ' ';
            for(int i=0;i<4;i++){
                int l;
                if(k) l=i; else l=3-i;
                if(board[i][l]=='T')continue;
                else if(board[i][l]=='.') {
                    contable=true;
                    miss=true;
                    break;
                }
                else if (check == ' ') {
                    check = board[i][l];
                }
                else if (board[i][l] != check) {
                    miss = true;
                    break;
                }
            }
            if(!miss){
                cout << "Case #" << t << ": " << check << " won" << endl;
                next = true;
                break;
            }
        }
        if(next) continue;
        next=false;
        
        if(contable){
            cout << "Case #" << t << ": Game has not completed" << endl;            
        }else{
            cout << "Case #" << t << ": Draw" << endl;
        }
    }
    return 0;
}