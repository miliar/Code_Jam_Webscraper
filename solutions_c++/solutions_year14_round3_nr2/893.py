//
//  main.cpp
//  GoogleJam
//
//  Created by Alexandre Decuq on 24/03/14.
//  Copyright (c) 2014 Alexandre Decuq. All rights reserved.
//

//#include "main.h"

#include <vector>
#include <set>
#include <map> //set_intersection()
#include <stdio.h>
#include <iostream>
#include <string>
#include <cstring>
#include <queue>
#include <cassert>
#include <iomanip> //for setprecision()
#include <cmath> //ceil() or floor()

using namespace std; //std::to_string(int)

#define MOD 1000000007

int N;

int test[10];

bool isValid(string s)
{
    int test[26];
    memset(test,0,sizeof(test));
    test[s[0]-'a']=1;
    char prec=s[0];
    for(int i=1;i<s.size();++i) {
        char cur=s[i];
        if(test[cur-'a']==0) {
            test[cur-'a']++;
        } else {
            if(cur==prec) {
                test[cur-'a']++;
            } else {
                return false;
            }
        }
        prec=cur;
    }
    return true;
}

void optim(string & s)
{
    string out;
    char prec=s[0];
    out+=prec;
    for(int i=1;i<s.size();++i) {
        char cur=s[i];
        if(cur!=prec) {
            out+=cur;
        }
        prec=cur;
    }
    s = out;
}

int main()
{
    freopen("/Users/decuqa/Desktop/GoogleJam/GoogleJam/B-small-attempt2.in", "r", stdin);
	freopen("/Users/decuqa/Desktop/GoogleJam/GoogleJam/B-small-attempt2.out", "w", stdout);
    int T;
    cin>> T;
    
    for(int t=1; t<=T; t++)
    {
        
        cin >> N;
        vector<string> cars;
        for(int i=0;i<N;++i) {
            string tmp;
            cin >> tmp;
            optim(tmp);
            cars.push_back(tmp);
        }
        
        //int test[N];
        memset(test,0,sizeof(test));
        for(int i=0;i<N;++i) {
            test[i]=i;
        }
        
        int res=0;
        do {
            string tmp="";
            for(int i=0;i<N;++i) {
                tmp+=cars[test[i]];
            }
            
            if ( isValid(tmp) ) {
                //cout<<tmp<< " is valid"<<endl;
                ++res;
            }
                
            //cout<<res<<",";
        } while(next_permutation(test,test+N));
        cout<<"Case #"<<t<<": "<<res<<endl;
    }
}


