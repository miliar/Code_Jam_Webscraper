//
//  main.cpp
//  Word
//
//  Created by MichelleShieh on 4/16/16.
//  Copyright (c) 2016 MichelleShieh. All rights reserved.
//

#include <iostream>
#include <string>
using namespace std;

int main() {
    int t;
    string s,ss;
    cin>>t;
    for (int i=1;i<=t;i++) {
        cin>>s;
        cout<<"Case #"<<i<<": ";
        ss = s[0];
        for (int j = 1; j<s.length(); j++) {
            if (s[j]>=ss[0]) {
                ss.insert(ss.begin(),s[j]);
            }
            else {
                ss += s[j];
            }
        }
        cout<<ss<<endl;
    }
    return 0;
}
