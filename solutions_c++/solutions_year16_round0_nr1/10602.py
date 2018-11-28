//
//  main.cpp
//  FirstProgram
//
//  Created by Adeel on 08/04/2016.
//  Copyright © 2016 Adeel. All rights reserved.
//
#include <stdlib.h>
#include <cassert>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

#define REP(i,b,n) for(int i=(int)(b);i<(int)(n);++i)
#define rep(i,n) REP(i,0,n)

int solve(int n);

int main(int argc, const char * argv[]) {
    FILE *fin = freopen("A-large.in", "r", stdin);
    FILE *fout = freopen("A-large.out", "w", stdout);
    assert( fin!=NULL );
    int n;
    int t;
    int c = 0;
    cin >> t;
    
    while(cin >> n){
        int p = solve(n);
        if(p == -1){
            cout << "Case #"<<++c<<": INSOMNIA" << endl;
        }
        else{
            cout << "Case #"<<++c<<": "<< p << endl;
        }
        //break;
    }
    
       fclose(fout);
    return 0;
}

int solve(int n){
    if(n == 0)
        return -1;
    bool one = false, two = false, three= false, four =false, five = false;
    bool six = false, seven = false,eight = false,nine = false,zero = false;
    int inc = 1;
    int mul = n;
    while(true){
        mul = (inc++) * n;
        string s = to_string(mul);
    int i = 0;
    
    rep(i,s.size()){
        int t = s[i] - '0';
        if(t == 1){
            one = true;
        }
        else if(t == 2)
            two = true;
        else if(t == 3)
            three = true;
        else if(t == 4)
            four = true;
        else if(t == 5)
            five = true;
        else if(t == 6)
            six = true;
        else if(t == 7)
            seven = true;
        else if(t == 8)
            eight = true;
        else if(t == 9)
            nine = true;
        else if(t == 0)
            zero = true;
        
    }
    if(zero && one && two && three && four && five && six && seven && eight && nine){
        break;
    }
    
        
    }
    
    return mul;
}

