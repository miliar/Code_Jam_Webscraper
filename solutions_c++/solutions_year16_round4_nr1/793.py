//
//  main.cpp
//  codejam_2016
//
//  Created by fchowdhu on 4/9/16.
//  Copyright © 2016 fchowdhu. All rights reserved.
//

#include<iostream>
#include<stdio.h>
#include<math.h>
#include<string.h>
#include<algorithm>
#include<string>
#include<vector>
#include<map>
#include<queue>
#include<stack>
#include<sstream>
#include<set>
#include<fstream>
#include<cfloat>
using namespace std;

typedef long long  LL;
typedef vector<int>   vi;
typedef pair<int,int>  pii;
map<long long, int > vis;

string solve(int ind, int X ){
    string ret1 = "", ret2="";
    if(ind == 1){
        if(X == 0 ){
            return "RS";
        }else if(X==1){
            return "PR";
        }else if(X==2){
            return "PS";
        }

    }
    if(X == 0 ){
        ret1 = solve(ind-1, X) + solve(ind-1, 2);
        ret2 = solve(ind-1, 2) + solve(ind-1, X);
    }else if(X==1){
        ret1 = solve(ind-1, X) + solve(ind-1, 0);
        ret2 = solve(ind-1, 0) + solve(ind-1, X);
    }else if(X==2){
        ret1 = solve(ind-1, X) + solve(ind-1, 1);
        ret2 = solve(ind-1, 1) + solve(ind-1, X);
    }
    ret1 = min(ret1, ret2);
    return ret1;
}
bool check(string str, int r, int p, int s){
    
    for (int i=0; i<str.size(); i++) {
        if(str[i]=='R') r--;
        if(str[i]=='P') p--;
        if(str[i]=='S') s--;
    }
    if( r==0 && p==0 &&s ==0)return true;
    return false;
}
int main() {
    //freopen("/Users/fchowdhu/Downloads/A-small-attempt0.in", "r", stdin);
    freopen("/Users/fchowdhu/Downloads/A-large.in", "r", stdin);
    freopen("/Users/fchowdhu/Downloads/AL.out", "w", stdout);
    int t,cn=1;
   // srand (time(NULL));

    cin>>t;
    

    while (t--) {
        int n, r, p, s;
        cin>>n>>r>>p>>s;
        string str = "Z";
        for (int i=0; i<3; i++) {
            string str1 = solve(n, i);
           // cerr<<str1<<endl;
            if(check(str1, r, p, s)){
                str = min(str, str1);
            }
        }
        cout<<"Case #"<<cn++<<":";
        if(str =="Z" ){
            cout<<" IMPOSSIBLE";
        }else{
            cout<<" "<<str;
        }
        cout<<endl;
    }
    
    return 0;
}
