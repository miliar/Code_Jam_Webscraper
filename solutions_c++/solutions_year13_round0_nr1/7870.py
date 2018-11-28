//
//  main.cpp
//  google code jam 2013
//
//  Created by Mahmoud Hosny on 4/13/13.
//  Copyright (c) 2013 Mahmoud Hosny. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

int main(int argc, const char * argv[])
{
    ifstream in ("m.in");
    ofstream out ("out.out");
    int T, Trow = -1, Tcol = -1, Xcount = 0, Ocount = 0;
    in >> T;
    //cout << T<<endl;
    for (int h = 0 ; h < T ; h++){
        Trow = -1;
        Tcol = -1;
        Xcount = 0;
        Ocount = 0;
        char arr [4][4];
        for (int i = 0 ; i < 4 ; i++){
            
            for (int j = 0 ; j <4 ; j++){
                in >> arr[i][j];
                //cout << arr[i][j] << " ";
                if (arr[i][j] == 'T'){
                    // case we have T
                    Trow = i;
                    Tcol = j;
                }else if (arr[i][j] == 'X'){
                    Xcount ++;
                }else if (arr[i][j] == 'O'){
                    Ocount ++;
                }
            }
            //cout << endl;
        }
        if (Xcount < 4 && Ocount < 4 && Tcol == -1){
            // game not yet finished
            //cout << "entered first if" <<endl;
            out << "Case #"<< h+1 <<": "<< "Game has not completed"<<endl;
            cout << "Case #"<< h+1 <<": "<< "Game has not completed"<<endl;
            continue;
        }
        // case X win
        // rows
        bool Xwon = false, Owon  = false;
        for (int i = 0 ; i < 4 ; i ++){
            Xwon = true;
            for (int j = 0 ; j < 4 ; j ++){
                if (arr[i][j] != 'X' ){
                    if (arr[i][j] !='T' && (arr[i][j] == '.' || arr[i][j] == 'O')){
                        Xwon = false;
                        break;
                    }
                }
            }
            if (Xwon){
                break;
            }
        }
        //cout << "1-Xwon is now "<<Xwon<<endl;
        // if not collected rows check cols
        if (!Xwon){
            for (int i = 0 ; i < 4 ; i ++){
                Xwon = true;
                for (int j = 0 ; j < 4 ; j ++){
                    if (arr[j][i] != 'X'){
                        if (arr[j][i] !='T' && (arr[j][i] == '.' || arr[j][i] == 'O')){
                            Xwon = false;
                            break;
                        }
                    }
                }
                if (Xwon){
                    break;
                }
            }
        }
        //cout << "2-Xwon is now "<<Xwon<<endl;
        
        // now check diagonals
        
        // this diagonal \
        
        if (!Xwon){
            for (int i = 0 ; i < 4 ; i ++){
                Xwon = true;
                if (arr[i][i] != 'X'){
                    if (arr[i][i] !='T' && (arr[i][i] == '.' || arr[i][i] == 'O')){
                        
                        Xwon = false;
                        break;
                    }
                }
            }
        }
        //cout << "2.5-Xwon is now "<<Xwon<<endl;
        // this diagonal /
        if (!Xwon){
            for (int i = 3 ; i >=0   ; i --){
                Xwon = true;
                if (arr[abs(3-i)][i] != 'X'){
                    if (arr[abs(3-i)][i] !='T' && (arr[abs(3-i)][i] == '.' || arr[abs(3-i)][i] == 'O')){
                        Xwon = false;
                        break;
                    }
                }
            }
        }
        //cout << "3-Xwon is now "<<Xwon<<endl;
        //------------
        // check for O
        for (int i = 0 ; i < 4 ; i ++){
            Owon = true;
            for (int j = 0 ; j < 4 ; j ++){
                if (arr[i][j] != 'O'){
                    if (arr[i][j] !='T' && (arr[i][j] == '.' || arr[i][j] == 'X')){
                        Owon = false;
                        break;
                    }
                }
            }
            if (Owon){
                break;
            }
        }
        //cout << "1-Owon is now "<<Owon<<endl;
        if (!Owon){
            for (int i = 0 ; i < 4 ; i ++){
                Owon = true;
                for (int j = 0 ; j < 4 ; j ++){
                    if (arr[j][i] != 'O'){
                        if (arr[j][i] !='T' && (arr[j][i] == '.' || arr[j][i] == 'X')){
                            Owon = false;
                            break;
                        }
                    }
                }
                if (Owon){
                    break;
                }
            }
        }
        //cout << "2-Owon is now "<<Owon<<endl;
        // this diagonal \
        
        if (!Owon){
            for (int i = 0 ; i < 4 ; i ++){
                Owon = true;
                if (arr[i][i] != 'O'){
                    if (arr[i][i] !='T' && (arr[i][i] == '.' || arr[i][i] == 'X')){
                        Owon = false;
                        break;
                    }
                }
            }
        }
        //cout << "2.5-Owon is now "<<Owon<<endl;
        // this diagonal /
        if (!Owon){
            for (int i = 3 ; i >=0   ; i --){
                Owon = true;
                if (arr[abs(3-i)][i] != 'O'){
                    if (arr[abs(3-i)][i] !='T' && (arr[abs(3-i)][i] == '.' || arr[abs(3-i)][i] == 'X')){
                        Owon = false;
                        break;
                    }
                }
            }
        }
        //cout << "3-Owon is now "<<Owon<<endl;
        int temp = 0;
        if (Tcol != -1){
            temp = 1;
            //cout << "temp = "<< temp << endl;
            //cout << "Xcount + Ocount + temp == " << Xcount + Ocount + temp <<endl;
        }
        if (!Owon && !Xwon && (Xcount + Ocount + temp == 16)){
            out << "Case #"<< h+1 <<": "<< "Draw"<<endl;
            cout << "Case #"<< h+1 <<": "<< "Draw"<<endl;

        }else if (Owon && !Xwon){
            out << "Case #"<< h+1 <<": "<< "O won"<<endl;
            cout << "Case #"<< h+1 <<": "<< "O won"<<endl;
        }else if (!Owon && Xwon){
            out << "Case #"<< h+1 <<": "<< "X won"<<endl;
            cout << "Case #"<< h+1 <<": "<< "X won"<<endl;
        }else {
            out << "Case #"<< h+1 <<": "<< "Game has not completed"<<endl;
            cout << "Case #"<< h+1 <<": "<< "Game has not completed"<<endl;
            
        }
    }
    
}

