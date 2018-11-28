//============================================================================
// File        : main.cpp
// Author      : AHMED HANI IBRAHIM
// Copyright   : AHani
// Version     : UVa - Accepted - 0.032
// Created on April 11, 2013, 2:33 AM
//============================================================================

#include <cstdlib>
#include <stdio.h>
#include <string.h>
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <functional>
#include <map>
#define Max 1000 + 5
#define INF 1000000000
//#define INT_MAX 2147483647
#define FOR(i, N) for( int i = 0 ; i < N ; i++ )
#define FOR1e(i, N) for( int i = 1 ; i <= N ; i++ )
#define FORe(i, N) for(int i = 0 ; i <= N ; i++ )
#define FOR1(i, N) for(int i = 1 ; i < N ; i++ )

using namespace std;

char Grid[Max][Max];
int TestCases;
bool Complete;

int CheckRow() {
    bool XWin = false;
    bool OWin = false;
    int Counter = 0;
    FOR(i, 4) {
        FOR(j, 4) {
            if(Grid[i][j] == 'X' || Grid[i][j] == 'T') Counter++;
        }
        if(Counter == 4) XWin = true;
        Counter = 0;
    }
    Counter = 0;
    FOR(i, 4) {
        FOR(j, 4) {
            if(Grid[i][j] == 'O' || Grid[i][j] == 'T')  Counter++;
        }
        if(Counter == 4) OWin = true;
        Counter = 0;
    }
    if(XWin && OWin)                 return 3;
    else if(XWin && !OWin)           return 1;
    else if(!XWin && OWin)           return 2;
    else                             return 0;
}

int CheckColumn() {
    bool XWin = false;
    bool OWin = false;
    int Counter = 0;
    FOR(i, 4) {
        FOR(j, 4) {
            if(Grid[j][i] == 'X' || Grid[j][i] == 'T') Counter++;
        }
        if(Counter == 4) XWin = true;
        Counter = 0;
    }
    Counter = 0;
    FOR(i, 4) {
        FOR(j, 4) {
            if(Grid[j][i] == 'O' || Grid[j][i] == 'T')  Counter++;
        }
        if(Counter == 4) OWin = true;
        Counter = 0;
    }
    if(XWin && OWin)                 return 3;
    else if(XWin && !OWin)           return 1;
    else if(!XWin && OWin)           return 2;
    else                             return 0;
}

int ChechDigonal() {
    bool XWin = false;
    bool OWin = false;
    if((Grid[0][0] == 'X' || Grid[0][0] == 'T') && (Grid[1][1] == 'X' || Grid[1][1] == 'T') 
            && (Grid[2][2] == 'X' || Grid[2][2] == 'T') && (Grid[3][3] == 'X' || Grid[3][3] == 'T'))
        XWin = true;
    if((Grid[0][0] == 'O' || Grid[0][0] == 'T') && (Grid[1][1] == 'O' || Grid[1][1] == 'T') 
            && (Grid[2][2] == 'O' || Grid[2][2] == 'T') && (Grid[3][3] == 'O' || Grid[3][3] == 'T'))
        OWin = true;
    if((Grid[0][3] == 'X' || Grid[0][3] == 'T') && (Grid[1][2] == 'X' || Grid[1][2] == 'T') 
            && (Grid[2][1] == 'X' || Grid[2][1] == 'T') && (Grid[3][0] == 'X' || Grid[3][0] == 'T'))
        XWin = true;
    if((Grid[0][3] == 'O' || Grid[0][3] == 'T') && (Grid[1][2] == 'O' || Grid[1][2] == 'T') 
            && (Grid[2][1] == 'O' || Grid[2][1] == 'T') && (Grid[3][0] == 'O' || Grid[3][0] == 'T'))
        OWin = true;
    if(XWin && OWin)                 return 3;
    else if(XWin && !OWin)           return 1;
    else if(!XWin && OWin)           return 2;
    else                             return 0;
}

int main(int argc, char** argv) {
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int Cases = 1;
    cin >> TestCases;
    cin.ignore();
    while(TestCases-- > 0) {
        Complete = true;
        FOR(i, 4) {
            FOR(j, 4) {
                cin >> Grid[i][j];
                if(Grid[i][j] == '.') Complete = false;
            }
        }
        int Row = CheckRow();
        int Col = CheckColumn();
        int Dia = ChechDigonal();
        printf("Case #%d: ", Cases++);
        if(Row == 1) {
            puts("X won");
            continue;
        }
        if(Row == 2) {
            puts("O won");
            continue;
        }
        if(Col == 1) {
            puts("X won");
            continue;
        }
        if(Col == 2) {
            puts("O won");
            continue;
        }
        if(Dia == 1) {
            puts("X won");
            continue;
        }
        if(Dia == 2) {
            puts("O won");
            continue;
        }
        if(!Complete) {
            puts("Game has not completed");
            continue;
        }
        puts("Draw");
    }     
    
    return 0;
}

