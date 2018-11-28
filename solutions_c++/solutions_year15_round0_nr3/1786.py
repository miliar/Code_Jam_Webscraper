//
//  main.cpp
//  Dijkstra
//
//  Created by Loc Ngo on 4/10/15.
//  Copyright (c) 2015 Loc Ngo. All rights reserved.
//

#include <iostream>
#include <vector>
#include <fstream>
using namespace std;
ifstream fin("/Users/locngo/Documents/Codejam/Dijkstra/C-small-attempt1.in");
#define MAX 1000000
int F[5][5];
int P[100000];

void init(){
    F[1][1] = 1;
    F[1][2] = 2;
    F[1][3] = 3;
    F[1][4] = 4;
    F[2][1] = 2;
    F[2][2] = -1;
    F[2][3] = 4;
    F[2][4] = -3;
    F[3][1] = 3;
    F[3][2] = -4;
    F[3][3] = -1;
    F[3][4] = 2;
    F[4][1] = 4;
    F[4][2] = 3;
    F[4][3] = -2;
    F[4][4] = -1;
}

int g(int a,int b){
    int s = 1;
    if(a<0)
        s*=-1;
    if(b<0)
        s*=-1;
    return s*F[abs(a)][abs(b)];
}

int rg(int lv,int rv){
    switch(lv){
        case 1:
            switch(rv){
                case 1:
                    return 1;
                case 2:
                    return 2;
                case 3:
                    return 3;
                case 4:
                    return 4;
            }
            break;
        case 2:
            switch(rv){
                case 2:
                    return 1;
                case -1:
                    return 2;
                case 4:
                    return 3;
                case -3:
                    return 4;
            }
            break;
        case 3:
            switch(rv){
                case 3:
                    return 1;
                case -4:
                    return 2;
                case -1:
                    return 3;
                case 2:
                    return 4;
            }
            break;
        case 4:
            switch(rv){
                case 4:
                    return 1;
                case 3:
                    return 2;
                case -2:
                    return 3;
                case -1:
                    return 4;
            }
            break;
    }
    return 0;
}

int f(int a,int b){
    if(a==0)
        return P[b];
    return rg(P[a-1],P[b]);
}

void process(int t){
    int l,x;
    string tmp;
    fin>>l>>x;
    fin>>tmp;
    string s = "";
    for(int i=0;i<x;i++)
        s+=tmp;
    vector<int> v;
    for(int i=0;i<s.length();i++){
        switch(s[i]){
            case 'i':
                v.push_back(2);
                break;
            case 'j':
                v.push_back(3);
                break;
            case 'k':
                v.push_back(4);
                break;
        }
    }
    int k = 1;
    for(int i=0;i<l*x;i++){
        k = g(k,v[i]);
        P[i] = k;
    }

    string ret = "NO";
    for(int i=1;i<v.size()-1;i++){
        for(int j=i+1;j<v.size();j++){
            if(f(0,i-1)==2&&f(i,j-1)==3&&f(j,v.size()-1)==4){
                ret = "YES";
                break;
            }
        }
        if(ret=="YES")
            break;
    }
    cout<<"Case #"<<t<<": "<<ret<<endl;
}

int main(int argc, const char * argv[]) {
    // insert code here...
    init();
    int T;
    fin>>T;
    for(int i=1;i<=T;i++)
        process(i);
    return 0;
}
