//
//  main.cpp
//  Codejam2
//
//  Created by Zulkarnine Mahmud on 4/13/13.
//  Copyright (c) 2013 Zulkarnine Mahmud. All rights reserved.
//

#include <iostream>
#include <stdio.h>
#include <fstream>
#include <iomanip>
#include "math.h"
#include <algorithm>
#include <vector>
#include <string>
#include <array>

unsigned int T;
int N;
int M;
int field[100][100];
int Maxheight=100;
int x_value=0;
int y_value=0;
int presentHeight=1;


using namespace std;

/*int WhereToStart(int row,int column,int height){
    
    for (int h=height; h<=Maxheight; h++) {
        for (int i=row; i<N; i++) {
            for (int j=column; j<M; j++) {
                if (field[i][j]==h) {
                    x_value=i;
                    y_value=j;
                    return h;
                }
                
            }
        }
        
    }
}*/
string TrueFalse(bool b){
    return (b? "true":"false");
    
}

bool isHorizontalOrVerticalpossibleAt(int x,int y){
    bool value1=true,value2=true,value;
    int i,j;
    for (i=0; i<M; i++) {
        
        if (field[x][i]>field[x][y]) {
            value1=false;
        }
        
    }
    
    for (j=0; j<N; j++) {
        if (field[j][y]>field[x][y]) {
            value2=false;
        }
    }
    if (value1==false&&value2==false) {
        value=false;
    }else value=true;

    return value;
}

int solveCase(){
    for (int height=1; height<=Maxheight; height++) {
        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                //cout<<"isHorizontalOrVerticalpossibleAt("<<i<<","<< j<<") = "<<TrueFalse(isHorizontalOrVerticalpossibleAt(i, j))<<endl;
                
                if (isHorizontalOrVerticalpossibleAt(i, j)==false) {
                    return 2;
                }
            }
        }
    }
    return 1;
    
    
    
}

string statement(int a){
    string s;
    switch (a) {
        case 1:
            s="YES";
            break;
        case 2:
            s="NO";
            break;
        default:
            s="error";
            break;
    }
    return s;
}

int main(){
    
    freopen("B-large.in", "r", stdin);
    freopen("2_2.out", "w", stdout);

    cin>>T;
    for (int cas=1; cas<=T; cas++) {
        cin>>N;
        cin>>M;
        for (int l=0; l<N; l++) {
            for (int m=0; m<M; m++) {
                cin>>field[l][m];
                
            }
        }
        /*cout<<"N="<<N<<endl;
        cout<<"M="<<M<<endl;
        for (int l=0; l<N; l++) {
         for (int m=0; m<M; m++) {
         cout<<field[l][m];
         }
         cout<<endl;
         }*/
        cout<<"Case #"<<cas<<": "<<statement(solveCase())<<endl;
        
        
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
    
}