//
//  main.cpp
//  CJ2
//
//  Created by Aayush Goel on 4/8/16.
//  Copyright © 2016 Aayush Goel. All rights reserved.
//

#include <iostream>
#include <vector>

using namespace std;

int flips(string str){
    int count = 0;
    if(str[str.size()-1]!='+') count++;
    
    for(int i=(int)str.size()-2; i>=0; i--){
        if(str[i]!=str[i+1]) count++;
    }
    return count;
}

int main(int argc, const char * argv[]) {
    // insert code here...
    int t;
    string x;
    vector<string> S;
    
    cin >> t;
    for(int i=0; i<t; i++){
        cin >> x;
        S.push_back(x);
    }
    
    string str;
    for(int i=1; i<=S.size(); i++){
        int out = flips(S[i-1]);
        str = to_string(out);
        cout<< "Case #" << i <<": " <<str<< endl;
    }
    
    return 0;
}

