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
double mem[202][102][102];
int tc[202][102][102], TC, n;
double P[222];
double solve(int ind, int k1, int k2, int msk){
    if(k1==0 && k2==0){
        return 1;
    }else if(ind == n || k1<0 ||k2<0) return 0;
    
    if(tc[ind][k1][k2] == TC) {
        
        return mem[ind][k1][k2];
    }
    tc[ind][k1][k2] = TC;
    double &ret  = mem[ind][k1][k2];
    ret = solve(ind+1, k1, k2, msk);
    if((msk&(1<<ind)));
    else return ret;
    double ret1 = P[ind] * solve(ind+1, k1-1, k2,msk);
    ret1+= (1.-P[ind]) * solve(ind+1, k1, k2-1,msk);
    ret = max(ret, ret1);
    return ret;
}
double BruteB(int k){
    double ret = 0;
    for(int i=0;i<(1<<n);i++){
        int c=0;
        for(int j=0;j<n;j++){
            if(i&(1<<j))c++;
        }
        if(c == k){
            TC++;
            ret = max(solve(0, k/2, k/2, i), ret);
        }
    }
    return ret;
}
int main() {
    freopen("/Users/fchowdhu/Downloads/B-small-attempt0.in", "r", stdin);
    //freopen("/Users/fchowdhu/Downloads/A-large.in", "r", stdin);
    freopen("/Users/fchowdhu/Downloads/B0.out", "w", stdout);
    int t,cn=1;
   // srand (time(NULL));

    cin>>t;
    

    while (t--) {
        TC++;
        int k;
        cin>>n>>k;
        
        for (int i=0; i<n; i++) {
            cin>>P[i];
        }
        cout<<"Case #"<<cn++<<":";
        
        printf(" %.15lf", BruteB(k));
        
        cout<<endl;
    }
    
    return 0;
}
