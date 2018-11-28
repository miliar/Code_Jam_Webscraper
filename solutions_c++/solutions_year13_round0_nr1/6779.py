//
//  main.cpp
//  Google Code Jam
//
//  Created by Zhuo Li on 4/12/13.
//  Copyright (c) 2013 Zhuo Li. All rights reserved.
//
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

#define m_N 4
bool ifCompleted(char scaffold[4][4]);
string statusCheck(char scaffold[4][4]);


int main () {
    char scaffold[4][4];
    int input_size, temp;
    string empty_line;
    stringstream ss;
    ifstream myfile("A-large.in");
    string first_line;
    getline(myfile, first_line);
    ss << first_line;
    ss >> input_size;
    temp = input_size;
    string *input = new string[input_size];
    int case_num = 0;
    while (temp!=0) {
        myfile>>scaffold[0];
        myfile>>scaffold[1];
        myfile>>scaffold[2];
        myfile>>scaffold[3];
        getline(myfile, empty_line);
        input[case_num] = statusCheck(scaffold);
        case_num++;
        temp--;
    }
    int num = 1;
    while (input_size!=0) {
        cout<<"Case #"<<num<<": "<<input[num-1]<<"\n";
        num++;
        input_size--;
    }
    delete [] input;
    return 0;
}

string statusCheck(char scaffold[4][4])
{
    for (int i = 0; i < 4; i++) {
        int N = 0;
        for (int j = 0; j < 4; j++) {
            if (scaffold[i][j]=='X' || scaffold[i][j]=='T') {
                N++;
               if (N==m_N) return "X won";
            }
        }
    }
    
    for (int j = 0; j < 4; j++) {
        int N = 0;
        for (int i = 0; i < 4; i++) {
            if (scaffold[i][j]=='X' || scaffold[i][j]=='T') {
                N++;
                if (N==m_N) return "X won";
            }
        }
    }
    
    int c = 0;
    int N = 0;
    for (int i = 0 ; i < 4 ; i++) {
        
        if (scaffold[i][c]=='X' || scaffold[i][c]=='T') {
            N++;
            if (N==m_N) return "X won";
        }
        c++;
    }
    
    c = 3;
    N = 0;
    for (int i = 0 ; i < 4 ; i++) {
        
        if (scaffold[i][c]=='X' || scaffold[i][c]=='T') {
            N++;
            if (N==m_N) return "X won";
        }
        c--;
    }
    
    for (int i = 0; i < 4; i++) {
        int N = 0;
        for (int j = 0; j < 4; j++) {
            if (scaffold[i][j]=='O' || scaffold[i][j]=='T') {
                N++;
                if (N==m_N) return "O won";
            }
        }
    }
    
    for (int j = 0; j < 4; j++) {
        int N = 0;
        for (int i = 0; i < 4; i++) {
            if (scaffold[i][j]=='O' || scaffold[i][j]=='T') {
                N++;
                if (N==m_N) return "O won";
            }
        }
    }
    
    c = 0;
    N = 0;
    for (int i = 0 ; i < 4 ; i++) {
        
        if (scaffold[i][c]=='O' || scaffold[i][c]=='T') {
            N++;
            if (N==m_N) return "O won";
        }
        c++;
    }
    
    c = 3;
    N = 0;
    for (int i = 0 ; i < 4 ; i++) {
      
        if (scaffold[i][c]=='O' || scaffold[i][c]=='T') {
            N++;
            if (N==m_N) return "O won";
        }
        c--;
    }
    
    if (ifCompleted(scaffold)) return "Draw";
    else return "Game has not completed";
}

bool ifCompleted(char scaffold[4][4])
{
    for (int i = 0;i < 4;i++) {
        for (int j = 0; j < 4; j++) {
            if (scaffold[i][j]=='.') return false;
        }
    }
    return true;
}