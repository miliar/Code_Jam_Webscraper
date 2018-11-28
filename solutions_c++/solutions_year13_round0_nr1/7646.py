//
//  main.cpp
//  GoogleCodeJamQualification
//
//  Created by Jain, Archit on 4/13/13.
//  Copyright (c) 2013 Jain, Archit. All rights reserved.
//

#include <iostream>
#include <stdio.h>
using namespace std;

char* solve(){
    char a[4][6] ;
    for (int i=0; i<4; i++) {
        std::cin>>a[i];
    }
    bool isBlank =0;
    for (int i=0; i<4; i++) {
        int x=0;
        int o=0;
        for (int j=0; j<4; j++) {
            char c=a[i][j];
            if(c=='X'){
                x++;
            } else if (c=='O'){
                o++;
            } else if (c=='T'){
                x++; o++;
            } else {
                isBlank = true;
            }
        }
        if(x==4){
            return "X won";
        }
        if(o==4){
            return "O won";
        }
        
    }
    for (int i=0; i<4; i++) {
        int x=0;
        int o=0;
        for (int j=0; j<4; j++) {
            char c=a[j][i];
            if(c=='X'){
                x++;
            } else if (c=='O'){
                o++;
            } else if (c=='T'){
                x++; o++;
            } else {
                isBlank = true;
            }
        }
        if(x==4){
            return "X won";
        }
        if(o==4){
            return "O won";
        }
        
    }
    {
        int x=0;
        int o=0;
        for (int j=0; j<4; j++) {
            char c=a[j][3-j];
            if(c=='X'){
                x++;
            } else if (c=='O'){
                o++;
            } else if (c=='T'){
                x++; o++;
            } else {
                isBlank = true;
            }
        }
        if(x==4){
            return "X won";
        }
        if(o==4){
            return "O won";
        }
    }
    {
        int x=0;
        int o=0;
        for (int j=0; j<4; j++) {
            char c=a[j][j];
            if(c=='X'){
                x++;
            } else if (c=='O'){
                o++;
            } else if (c=='T'){
                x++; o++;
            } else {
                isBlank = true;
            }
        }
        if(x==4){
            return "X won";
        }
        if(o==4){
            return "O won";
        }
    }
    if(isBlank){
        return "Game has not completed";
    }
    else
        return "Draw";
    
}

int main(int argc, const char * argv[])
{

    int tc=0;
    std::cin>>tc;
    for (int i=1; i<=tc; i++) {
        char* result = solve();
        cout<<"Case #"<<i<<": "<<result<<"\n";
    }
    return 0;
}

