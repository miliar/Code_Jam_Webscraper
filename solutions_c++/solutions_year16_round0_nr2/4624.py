//
//  main.cpp
//  GoogleJam
//
//  Created by Alexandre Decuq on 24/03/14.
//  Copyright (c) 2014 Alexandre Decuq. All rights reserved.
//

#include "main.h"

#include <vector>
#include <set>
#include <map> ///set_intersection()
#include <queue>
#include <algorithm>
#include <stdio.h>
#include <iostream>
#include <string>  ///memset
#include <cstring>
#include <cassert>
#include <iomanip> ///setprecision()
#include <cmath> ///ceil() or floor()
#include <climits> ///INT_MAX

using namespace std; ///std::to_string(int)

/*
string flip(string s) {
    string res(s.rbegin(),s.rend());
    //do flip
    for(int i=0;i<s.size();++i) {
        if(res[i]=='-')
            res[i] = '+';
        else
            res[i] = '-';
    }
    return res;
}

int dfs(string s, int n) {
    if(s.size()==0)
        return 0;
    else if (s.size()==1) {
        if(s=="+")
            return 0;
        else
            return 1;
    }
    else {
        char first = s[0];
        char last = s[s.size()-1];
        if(last== '+') {
            string sub = s.substr(0,s.size()-1);
            return dfs(sub,n);
        }
        else {
            //try flip
            int res = INT_MAX-1;
            if (first== '-' && last != '+') {
                string r = flip(s);
                res = dfs(r,n) + 1; //flip cost
            }
            string sub = s.substr(0,s.size()-1);
            int res2 = dfs(sub,n);
            if(last != s[s.size()-2])
                res2++; //flip previous pancakes one more time
            if(s.size() == n && last=='-') {
                res++;
                res2++;
            }
            return min(res, res2);
        }
    }
}
*/

int main()
{
    /** INITIALIZATION */
    FILE *fp = freopen("/home/alex/Projects/googlecodejam/B-large.in", "r", stdin); //small-attempt2
    freopen("/home/alex/Projects/googlecodejam/B-large.out", "w", stdout);
    if(fp==0) cout <<"ERROR reading input file" << endl;

    /** BEGIN ALGORITHM */
    int T;
    cin>> T; /// T test cases follow
    for(int t=1; t<=T; t++)
    {
        string S;
        cin >> S;
        //cout << "Case #"<<t<<": " << dfs(S,S.size()) << endl;

        cout << "Case #"<<t<<": ";

        if(S.size()==1) {
            if(S[0]=='-')
                cout << 1 << endl;
            else
                cout << 0 <<endl;
            continue;
        }

        int res = 0;
        for(int i=1;i<S.size();i++) {
            if(S[i-1]=='-' && S[i]=='+')        //case "-+"
                res += 1;
            else if (S[i-1]=='+' && S[i]=='-')  //case "+-"
                res += 1;
            else                                //case "++"
                continue;
        }
        if(S[S.size()-1] == '-')
            res += 1;

        cout << res << endl;

    }
    /** END ALGORITHM */
}


