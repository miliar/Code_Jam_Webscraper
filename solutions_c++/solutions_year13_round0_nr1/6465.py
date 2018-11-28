#include<iostream>
#include <fstream>
#include <string>
using namespace std;

char checkValid(char board[4][4]);
//char checkValid3(char board[4][4], int i, int j);

int main(){
    ifstream in("A-large.in");
	cin.rdbuf(in.rdbuf());

	ofstream out("output.txt");
    cout.rdbuf(out.rdbuf());


    int testcases, i, j, k;
    char temp;
    char board[4][4];
    cin >> testcases;
    for(i=0;i<testcases;i++){
        for(j=0;j<4;j++){
            for(k=0;k<4;k++){
                cin >> board[j][k];
            }
        }
        /*for(j=0;j<4;j++){
            for(k=0;k<4;k++){
                cout << board[j][k];
            }
            cout<< endl;
        }*/
        temp = checkValid(board);
        //cout << temp;
        cout << "Case #" << i+1 << ": ";
        switch(temp){
            case 'X': cout << "X won" << endl;
                    break;
            case 'O': cout << "O won" << endl;
                    break;
            case '.': cout << "Game has not completed" << endl;
                    break;
            case 'D': cout << "Draw" << endl;
                    break;
        }

    }
	cout << endl;

	//cin.rdbuf(cinbuf);   //reset to standard input again
    //cout.rdbuf(coutbuf); //reset to standard output again

}
char checkValid(char board[4][4]){
    char temp;
    int x, tIndex, i, j;
    for(x=0;x<4;x++){
            //cout << "row Computation" << endl;
        for(i=0;i<4;i++){
            if(board[x][i] == 'T'){
                tIndex = i;
                break;
            }
            tIndex = -1;
        }
        if(tIndex>-1){
           switch(tIndex){
               case 0: if(board[x][1] == board[x][2] && board[x][2] == board[x][3] ){
                            if(board[x][1] != '.')
                                return board[x][1];
                        };
                        break;
               case 1: if(board[x][0] == board[x][2] && board[x][2] == board[x][3] ){
                            if(board[x][0] != '.')
                           return board[x][0];
                        };
                        break;
               case 2: if(board[x][1] == board[x][0] && board[x][0] == board[x][3] ){
                            if(board[x][0] != '.')
                                return board[x][0];
                        };
                        break;
               case 3: if(board[x][1] == board[x][2] && board[x][2] == board[x][0] ){
                            if(board[x][0] != '.')
                                return board[x][0];
                        };
                        break;
           }
        } else{
            temp = board[x][0];
            if(temp != '.' && temp == board[x][1] && temp == board[x][2] && temp == board[x][3] ){
                return temp;
            }
        }
    }
    /*column Check*/
    for(x=0;x<4;x++){
            //cout << "column Computation" << endl;
       for(i=0;i<4;i++){
            if(board[i][x] == 'T'){
                tIndex = i;
                break;
            }
            tIndex = -1;
        }
       // cout << "tIndex" << tIndex << endl;
        if(tIndex>-1){
           switch(tIndex){
               case 0: if(board[1][x] == board[2][x] && board[2][x] == board[3][x] ){
                            if(board[1][x] != '.')
                                return board[1][x];
                        };
                        break;
               case 1: if(board[0][x] == board[2][x] && board[2][x] == board[3][x] ){
                            if(board[0][x] != '.')
                                return board[0][x];
                        };
                        break;
               case 2: if(board[0][x] == board[1][x] && board[1][x] == board[3][x] ){
                            if(board[0][x] != '.')
                                return board[0][x];
                        };
                        break;
               case 3: if(board[0][x] == board[1][x] && board[1][x] == board[2][x] ){
                            if(board[0][x] != '.')
                                return board[0][x];
                        };
                        break;
           }
        } else{
            temp = board[0][x];
            if(temp != '.' && temp == board[1][x] && temp == board[2][x] && temp == board[3][x] ){
                return temp;
            }
        }
    }
    /* Checking for First Diagnol */
    //cout << "Diagnol 1 Computation" << endl;
    temp = board[0][0];
    if(temp != '.' && temp == board[1][1] && temp == board[2][2] && temp == board[3][3]){
        return temp;
    }
     if(temp != '.' && board[1][1] == 'T' && temp == board[2][2] && temp == board[3][3]){
        return temp;
    }
     if(temp != '.' && temp == board[1][1] && board[2][2] == 'T' && temp == board[3][3]){
        return temp;
    }
     if(temp != '.' && temp == board[1][1] && temp == board[2][2] && board[3][3] == 'T'){
        return temp;
    }
    if(board[0][0] == 'T'){
        temp = board[1][1];
        if(temp != '.' && temp == board[2][2] && temp == board[3][3]){
            return temp;
        }
    }

    /* Checking for Next Diagnol*/
    //cout << "Diagnol2 Computation" << endl;
    temp = board[0][3];
    //cout << temp << board[3][0] << board[1][2] << board[2][1] << board[3][0] << endl;
    if(temp != '.' && temp == board[1][2] && temp == board[2][1] && temp == board[3][0]){
        return temp;
    }
     if(temp != '.' && board[1][2] == 'T' && temp == board[2][1] && temp == board[3][0]){
        return temp;
    }
     if(temp != '.' && temp == board[1][2] && board[2][1] == 'T' && temp == board[3][0]){
        return temp;
    }
     if(temp != '.' && temp == board[1][2] && temp == board[2][1] && board[3][0] == 'T'){
        return temp;
    }
    if(board[0][3] == 'T'){
        temp = board[1][2];
        if(temp != '.' && temp == board[2][1] && temp == board[3][0]){
            return temp;
        }
    }

    for(i=0;i<4;i++)
        for(j=0;j<4;j++)
            if(board[i][j] == '.' )
                return '.';

    return 'D';
}
