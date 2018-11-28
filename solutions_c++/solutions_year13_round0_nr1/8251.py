#include <stdio.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>

#define forr(I, N) for(int I = 0; I < N; I++)

using namespace std;
int lineSum(int x[4]){
    int aux = 0;
    forr(i,4) aux+= x[i];
    return aux;
}

int columnSum( int x[4][4], int index){
    int aux = 0;
    forr(i,4) aux+= x[i][index];
    return aux;
}


int whoWon(int mapa[4][4], bool thereIsRoomToPlay){
    int line[4], column[4], diagonal[2];
    forr(i,4) line[i] = lineSum(mapa[i]);
    forr(i,4) column[i] = columnSum(mapa,i);
    diagonal[0] = mapa[0][0] + mapa[1][1] + mapa[2][2] + mapa[3][3];
    diagonal[1] = mapa[3][0] + mapa[2][1] + mapa[1][2] + mapa[0][3];

    forr(i,4){
        if(line[i] == 4 || line[i] == 13 || column[i] == 4 || column[i] == 13) return 1;
        else if(line[i] == 20 || line[i] == 35 || column[i] == 20 || column[i] == 25) return 2;
    }
    forr(i,2){
        if(diagonal[i] == 4 || diagonal[i] == 13) return 1;
        else if(diagonal[i] == 20 || diagonal[i] == 25) return 2;
    }
    if(thereIsRoomToPlay) return 3;
    else return 4;
}

int main(){
    char table[4][5];
    int n;
    bool thereIsRoomToPlay = false;
    int mapa[4][4];
    ifstream infile;
    ofstream outfile;
    outfile.open("output.txt");
    infile.open("A-small-attempt0.in");

    //cin >> n;
    infile >> n;

    forr(i,n){
        thereIsRoomToPlay = false;
        //leitura
        forr(j,4){
            //cin >> aux;
            infile >> table[j];
            //cout << table[j] << endl;
        }
        //verificacao
        forr(j,4){
            forr(k,4){
                switch(table[j][k]){
                    case 'X': mapa[j][k] = 1; break;
                    case 'O': mapa[j][k] = 5; break;
                    case 'T': mapa[j][k] = 10; break;
                    case '.': mapa[j][k] = 0; thereIsRoomToPlay = true; break;
                }
            }
        }

        outfile << "Case #" << i+1 <<": ";
        switch(whoWon(mapa, thereIsRoomToPlay)){
            case 1: outfile << "X won" << endl; break;
            case 2: outfile << "O won" << endl; break;
            case 3: outfile << "Game has not completed" << endl; break;
            case 4: outfile << "Draw" << endl; break;
        }

    }
    infile.close();
    outfile.close();
    return 1;
}
