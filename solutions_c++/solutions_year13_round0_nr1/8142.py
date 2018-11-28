//
//  main.cpp
//  Tic-Tac-Toe-Tomek
//
//  Created by Emrah SARI on 4/13/13.
//  Copyright (c) 2013 Emrah SARI. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;

#define X 'X'
#define O 'O'
#define T 'T'

int test(char g[4][4], int a){
    int win = 0;
    int dot = 0;
    ofstream out("/Users/emrahsari/Desktop/output-file.txt", ios_base::out | ios_base::app);

    for(int m=0; m<4; m++){
            if (g[m][0] == X && g[m][1] == X && g[m][2] == X && g[m][3] == X) {
                cout << "Case #"<<a<<": X won" << endl;
                out << "Case #"<<a<<": X won" << endl;
                win = 1;
            }
            else if (g[m][0] == O && g[m][1] == O && g[m][2] == O && g[m][3] == O){
                cout << "Case #"<<a<<": O won" << endl;
                out << "Case #"<<a<<": O won" << endl;
                win = 1;
            }
            else if (g[0][m] == X && g[1][m] == X && g[2][m] == X && g[3][m] == X) {
                cout << "Case #"<<a<<": X won" << endl;
                out << "Case #"<<a<<": X won" << endl;
                win = 1;
            }
            else if (g[0][m] == O && g[1][m] == O && g[2][m] == O && g[3][m] == O) {
                cout << "Case #"<<a<<": O won" << endl;
                out << "Case #"<<a<<": O won" << endl;
                win = 1;
            }
        
        if (g[m][0] == X && g[m][1] == X && g[m][2] == X && g[m][3] == T) {
            cout << "Case #"<<a<<": X won" << endl;
            out << "Case #"<<a<<": X won" << endl;
            win = 1;
        }
        else if (g[m][0] == O && g[m][1] == O && g[m][2] == O && g[m][3] == T){
            cout << "Case #"<<a<<": O won" << endl;
            out << "Case #"<<a<<": O won" << endl;
            win = 1;
        }
        else if (g[0][m] == X && g[1][m] == X && g[2][m] == X && g[3][m] == T) {
            cout << "Case #"<<a<<": X won" << endl;
            out << "Case #"<<a<<": X won" << endl;
            win = 1;
        }
        else if (g[0][m] == O && g[1][m] == O && g[2][m] == O && g[3][m] == T) {
            cout << "Case #"<<a<<": O won" << endl;
            out << "Case #"<<a<<": O won" << endl;
            win = 1;
        }
        
        if (g[m][0] == T && g[m][1] == X && g[m][2] == X && g[m][3] == X) {
            cout << "Case #"<<a<<": X won" << endl;
            out << "Case #"<<a<<": X won" << endl;
            win = 1;
        }
        else if (g[m][0] == T && g[m][1] == O && g[m][2] == O && g[m][3] == O){
            cout << "Case #"<<a<<": O won" << endl;
            out << "Case #"<<a<<": O won" << endl;
            win = 1;
        }
        else if (g[0][m] == T && g[1][m] == X && g[2][m] == X && g[3][m] == X) {
            cout << "Case #"<<a<<": X won" << endl;
            out << "Case #"<<a<<": X won" << endl;
            win = 1;
        }
        else if (g[0][m] == T && g[1][m] == O && g[2][m] == O && g[3][m] == O) {
            cout << "Case #"<<a<<": O won" << endl;
            out << "Case #"<<a<<": O won" << endl;
            win = 1;
        }
        
        }
    
        if (g[0][3]==X && g[1][2]==X && g[2][1]==X && g[3][0]==X) {
            cout << "Case #"<<a<<": X won" << endl;
            out << "Case #"<<a<<": X won" << endl;
            win = 1;
        }
        else if (g[0][3]==O && g[1][2]==O && g[2][1]==O && g[3][0]==O) {
            cout << "Case #"<<a<<": O won" << endl;
            out << "Case #"<<a<<": O won" << endl;
            win = 1;
        }
        else if (g[0][0]==X && g[1][1]==X && g[2][2]==X && g[3][3]==X) {
            cout << "Case #"<<a<<": X won" << endl;
            out << "Case #"<<a<<": X won" << endl;
            win = 1;
        }
        else if (g[0][0]==O && g[1][1]==O && g[2][2]==O && g[3][3]==O) {
            cout << "Case #"<<a<<": O won" << endl;
            out << "Case #"<<a<<": O won" << endl;
            win = 1;
        }
    
    if (g[0][3]==X && g[1][2]==X && g[2][1]==X && g[3][0]==T) {
        cout << "Case #"<<a<<": X won" << endl;
        out << "Case #"<<a<<": X won" << endl;
        win = 1;
    }
    else if (g[0][3]==O && g[1][2]==O && g[2][1]==O && g[3][0]==T) {
        cout << "Case #"<<a<<": O won" << endl;
        out << "Case #"<<a<<": O won" << endl;
        win = 1;
    }
    else if (g[0][0]==X && g[1][1]==X && g[2][2]==X && g[3][3]==T) {
        cout << "Case #"<<a<<": X won" << endl;
        out << "Case #"<<a<<": X won" << endl;
        win = 1;
    }
    else if (g[0][0]==O && g[1][1]==O && g[2][2]==O && g[3][3]==T) {
        cout << "Case #"<<a<<": O won" << endl;
        out << "Case #"<<a<<": O won" << endl;
        win = 1;
    }
    
    if (g[0][3]==T && g[1][2]==X && g[2][1]==X && g[3][0]==X) {
        cout << "Case #"<<a<<": X won" << endl;
        out << "Case #"<<a<<": X won" << endl;
        win = 1;
    }
    else if (g[0][3]==T && g[1][2]==O && g[2][1]==O && g[3][0]==O) {
        cout << "Case #"<<a<<": O won" << endl;
        out << "Case #"<<a<<": O won" << endl;
        win = 1;
    }
    else if (g[0][0]==T && g[1][1]==X && g[2][2]==X && g[3][3]==X) {
        cout << "Case #"<<a<<": X won" << endl;
        out << "Case #"<<a<<": X won" << endl;
        win = 1;
    }
    else if (g[0][0]==T && g[1][1]==O && g[2][2]==O && g[3][3]==O) {
        cout << "Case #"<<a<<": O won" << endl;
        out << "Case #"<<a<<": O won" << endl;
        win = 1;
    }

    if (!win){
        for(int m=0; m<4; m++){
            if (g[0][m] == '.' || g[1][m] == '.' || g[2][m] == '.' || g[3][m] == '.') {
                cout << "Case #"<<a<<": Game has not completed" << endl;
                out << "Case #"<<a<<": Game has not completed" << endl;
                dot = 1;
                break;
            }
        }
        if(!dot) {
                cout << "Case #"<<a<<": Draw" << endl;
                out << "Case #"<<a<<": Draw" << endl;
        }
    }


//    cout << g[0][0] << g[0][1] << g[0][2] << g[0][3] << endl;
//    cout << g[1][0] << g[1][1] << g[1][2] << g[1][3] << endl;
//    cout << g[2][0] << g[2][1] << g[2][2] << g[2][3] << endl;
//    cout << g[3][0] << g[3][1] << g[3][2] << g[3][3] << endl;
    
    return 0;
}

int main(int argc, const char * argv[])
{
    string line;
    ifstream myfile;
    string strFirst;
    int e,m,r,a,h=0;
    int sari;
    char g[4][4];
    myfile.open("/Users/emrahsari/Desktop/sample.txt");
    getline (myfile,line);
    strFirst = line;
    stringstream (strFirst) >> sari;
 
    if (myfile.is_open()){
        for (a=1; a<sari; a++){}
        
            for(e=0; e<a; e++){
                for(m=0; m<5; m++){
                    getline (myfile,line);
                    for(r=0; r<4; r++){
                        g[m][r] = line[r];
                    }
                }
            test(g, e+1);
            }
        myfile.close();
    }
   return 0;
}




