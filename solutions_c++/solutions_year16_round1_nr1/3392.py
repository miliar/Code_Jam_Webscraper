//
//  main.cpp
//  a
//
//  Created by ram on 16/04/16.
//  Copyright © 2016 mac. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <vector>
#include <array>
#include <string>
#include <string.h>
#include <math.h>
#include <algorithm>

using namespace std;

int main(){
    freopen("in.txt", "r", stdin);
    freopen("output.txt", "w'", stdout);
    int t;
    cin>>t;
    string str,strh;
    for (int i = 1; i<=t; i++) {
        cin>>str;
        strh += str[0];
        for (int a = 1; a<str.length(); a++) {
            if (str[a] >= strh[0]) {
                string temp;
                temp = str[a];
                temp += strh;
                strh = temp;
            }
            else{
                strh += str[a];
            }
        }
        cout<<"Case #"<<i<<": "<<strh<<endl;
        str.clear();
        strh.clear();
    }
    return 0;
}
