//
//  main.cpp
//  MagicTrick
//
//  Created by Minghui Liu on 4/12/14.
//  Copyright (c) 2014 Minghui Liu. All rights reserved.
//

#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

typedef vector<int> vi;
typedef vector<vector<int>> vvi;

void solve(int i, int firstGuess, int secondGuess, vvi & arrangement1, vvi & arrangement2){
    vi possible1 = arrangement1[firstGuess-1];
    vi possible2 = arrangement2[secondGuess-1];
    int countequal = 0;
    vi sameNums;
    for(auto num1 : possible1){
        for(auto num2 : possible2){
            if(num2==num1){
                countequal+=1;
                sameNums.push_back(num1);
            }
        }
    }
    if(countequal==0){
        cout << "Case #"<<i+1<<": Volunteer cheated!"<<endl;
    }else if(countequal==1){
        cout << "Case #"<<i+1<<": "<<sameNums[0]<<endl;
    }else{
        cout << "Case #"<<i+1<<": Bad magician!"<<endl;
    }
    
    
    
}


int main(int argc, const char * argv[])
{

    freopen("/Users/minghui/Documents/C++/MagicTrick/MagicTrick/A-small-attempt0.in.txt", "r", stdin);
    freopen("/Users/minghui/Documents/C++/MagicTrick/MagicTrick/A-small-attempt0.out.txt", "w", stdout);
    
    int T;
    cin >> T;
    int i,j,k;
    for(i=0;i<T;i++){
        int firstGuess,secondGuess;
        vvi arrangement1(4,vector<int>(4));
        vvi arrangement2(4,vector<int>(4));
        cin >> firstGuess;
        for(j=0;j<4;j++){
            for(k=0;k<4;k++){
                cin>>arrangement1[j][k];
            }
        }
        cin >> secondGuess;
        for(j=0;j<4;j++){
            for(k=0;k<4;k++){
                cin>>arrangement2[j][k];
            }
        }
        solve(i,firstGuess,secondGuess,arrangement1,arrangement2);
    }
    return 0;
}

