//
//  main.cpp
//  codejam
//
//  Created by Сыннер on 09.04.16.
//  Copyright (c) 2016 edu.self. All rights reserved.
//

#include <iostream>
#include <math.h>
#include <string>
#include <string.h>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;

const int N = 1e5;
const int M = 10;

void rev(string &s, int n){
    for(int i = 0;i<n/2;i++){
        swap(s[i],s[n - i - 1]);
    }
    for(int i = 0;i<n;i++){
        s[i] = (s[i] == '-'? '+':'-');
    }
}

int solve(int y){
    string s;
    cin>>s;
    int sz = (int)s.length();
    int i;
    for(i = sz - 1;i>=0;i--){
        if(s[i] == '-'){
            s[i+1] = '\0';
            sz = i+1;
            break;
        }
    }
    if(i < 0) sz = 0;
    int ans = 0;
    while(sz){
        for(i = 0;i<sz;i++){
            if(s[i] == '-') break;
        }
        if(i){
            ans+=2;
            rev(s,i);
        }
        else{
            ans++;
        }
        rev(s,sz);
    
        for(i = sz - 1;i>=0;i--){
            if(s[i] == '-'){
                s[i+1] = '\0';
                sz = i+1;
                break;
            }
        }
        if(i < 0) sz = 0;
    }
    return ans;
}
int main(int argc, const char * argv[]) {
    //freopen("","r",stdin); freopen("","w",stdout);
    int t;
    cin>>t;
    int y = 0;
    while(t--){
        y++;
        int ans = solve(y);
        cout<<"Case #"<<y<<": "<<ans;
        cout<<'\n';
    }
    
    return 0;
}
