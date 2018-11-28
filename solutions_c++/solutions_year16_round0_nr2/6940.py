//
//  pancake.cpp
//  nn
//
//  Created by Haoru Zhao on 4/9/16.
//  Copyright © 2016 Haoru Zhao. All rights reserved.
//

#include <iostream>
#include <fstream>

using namespace std;

int pancake(string pk){
    int ret = 0;
    size_t t = pk.size();
    for(size_t i = 0; i < t; ++i){
        if(i + 1 == t && pk[i] == '-'){
            ++ret;
        }else if(i + 1 < t && pk[i] != pk[i+1]){
            ++ret;
        }
    }
    return ret;
}

int main(){
    
    int n;
    string argv;
    cin >> n;
    for(int i = 1; i <= n; ++i){
        cin >> argv;
        int ret = pancake(argv);

        cout << "Case #" << i <<": " << ret << endl;

    }
}