//
//  main.cpp
//  b
//
//  Created by ram on 09/04/16.
//  Copyright © 2016 mac. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <vector>
#include <array>
#include <string>
#include <math.h>
#include <algorithm>

using namespace std;

int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w'", stdout);
    int t,ans;
    cin>>t;
    vector<char> vec;
    vec.reserve(100);
    string str;
    str.reserve(100);
    for (int i = 1; i<=t ; i++) {
        ans = 0;
        cout<<"Case #"<<i<<": ";
        cin>>str;
        for (int a = 0; a<str.length(); a++) {
            vec.push_back(str[a]);
        }
        while (vec[vec.size() - 1] == '+') {
            vec.erase(vec.begin() + vec.size() - 1);
        }
        while (vec.size() != 0 && find(vec.begin(), vec.end(), '-') != vec.end()) {
            for (int a = 0; a<vec.size(); a++) {
                if (vec[a] == '+') {
                    vec[a] = '-';
                }
                else{
                    vec[a] = '+';
                }
            }
            ans++;
            while (vec.size() != 0 && vec[vec.size() - 1] == '+') {
                vec.erase(vec.begin() + vec.size() - 1);
            }
        }
        cout<<ans<<endl;
        vec.clear();
        str.clear();
    }
    return 0;
}
