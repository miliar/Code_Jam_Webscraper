//
//  main.cpp
//  codejam-tictactomek
//
//  Created by Rajat on 4/13/13.
//  Copyright (c) 2013 Rajat. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <cstdlib>
#include <sstream>
using namespace std;

char checkWinnerX(string s){
    char flag = 'x';
    for(int i = 0; i<4; i++)
    {
        if(s[i] == 'X' || s[i] == 'T')
            continue;
        else{
            return '0';
        }
    }
    return flag;
}

char checkWinnerO(string s){
    char flag = 'o';
    for(int i = 0; i<4; i++)
    {
        if(s[i] == 'O' || s[i] == 'T')
            continue;
        else{
            return '0';
        }
    }
    return flag;
}


char resultof(string game[]){
    
    char flag = 'd';
    
    //check diagonal
    string d1 = "";
    d1.append(1, game[0][0]);
    d1.append(1, game[1][1]);
    d1.append(1, game[2][2]);
    d1.append(1, game[3][3]);

    string d2 = ""; // + game[3][0] + game[2][1] +  game[1][2] + game[0][3];
    d2.append(1, game[3][0]);
    d2.append(1, game[2][1]);
    d2.append(1, game[1][2]);
    d2.append(1, game[0][3]);
    char sx = checkWinnerX(d1);
    if(sx == 'x')
        return sx;
    char so = checkWinnerO(d1);
    if(so == 'o')
        return so;
    sx = checkWinnerX(d2);
    if(sx == 'x')
        return sx;
    so = checkWinnerO(d2);
    if(so == 'o')
        return so;
    
    
    //check horizontal
    for(int i = 0; i<4; i++)
    {
        char sx = checkWinnerX(game[i]);
        if(sx == 'x')
            return 'x';
        char so = checkWinnerO(game[i]);
        if(so == 'o')
            return 'o';
    }
    
    
    //check vertical
    string gamev[4];
    for(int j = 0; j<4; j++){
        for(int i = 0; i<4; i++)
        {
            gamev[j][i] = game[i][j];
        }
    }
    for(int i = 0; i<4; i++)
    {
        
        char sx = checkWinnerX(gamev[i]);
        if(sx == 'x')
            return sx;
        char so = checkWinnerO(gamev[i]);
        if(so == 'o')
            return so;
    }
    
    
    
    
    
    
    
    
    //check draw
    for(int i = 0; i<4; i++){
        for(int j = 0; j<4; j++){
            if(game[i][j] == '.')
                return 'i';
        }
    }
    
    return flag;
}

int main(int argc, const char * argv[])
{
    ifstream infile;
    infile.open("/Users/rajat/Documents/xcode/codejam/codejam-tictactomek/problem.in");
    ofstream outfile;
    outfile.open("/Users/rajat/Documents/xcode/codejam/codejam-tictactomek/problem1out.txt");

    int t, ctr = 0;
    infile>>t;
    while(t--){
        string game[4];
        for(int i = 0; i<4; i++)
        {
            infile>>game[i];
        }
        
        char c = resultof(game);
        outfile<<"Case #"<<++ctr<<": ";
        if(c=='x')
            outfile<<"X won"<<endl;
        else if(c=='o')
            outfile<<"O won"<<endl;
        else if(c=='d')
            outfile<<"Draw"<<endl;
        else
            outfile<<"Game has not completed"<<endl;
    }
    
    return 0;
}

