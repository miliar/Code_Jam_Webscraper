//
//  main.cpp
//  CodeJam
//
//  Created by Mousic on 4/11/15.
//  Copyright (c) 2015 Mousic. All rights reserved.
//

#include<string>
#include<vector>
#include<algorithm>
#include<queue>
#include<map>
#include<set>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<sstream>
#include<iostream>
#include<utility>
//#include<bitset>

using namespace std;

#define pi pair<int,int>
#define pis pair<int,string>
#define vi vector<int>
#define vpi vector<pi>
#define vd vector<double>
#define vs vector<string>
#define vsi vector<string>::iterator

#define fst first
#define snd second
#define pb push_back
#define SIZE(a) (int)(a.size())
#define LENGTH(a) (int)(a.length())
#define REP(i,n) for(int i=0;i<(n);i++)
#define REPD(i,n) for(int i=(n);i>=0;i--)
#define FOR(i,n,m) for(int i=(n);i<=(m);i++)
#define FORD(i,n,m) for(int i=(n);i>=(m);i--)
#define MIN(a,b) ((a)<(b) ? (a) : (b))
#define MAX(a,b) ((a)<(b) ? (b) : (a))
#define MIN3(a,b,c) MIN( MIN(a,b),MIN(a,c) )
#define MAX3(a,b,c) MAX( MAX(a,b),MAX(a,c) )
#define ABS(a) ( (a)<0 ? -(a) : (a))
#define STRUMIEN(A,B) istringstream A(B)
#define SORT(A) sort(A.begin(),A.end())

////////////////////////////////////////////////////////////////////////////////
int T,n0,n1,n2,n3,sum,flag;
string s0,s1,s2,s3,sr;
int rs;
map<string, pis> mp;

int main()
{
    mp["i"] = pis(1,"i");
    mp["j"] = pis(1,"j");
    mp["k"] = pis(1,"k");
    mp["ii"] = pis(-1,"");
    mp["jj"] = pis(-1,"");
    mp["kk"] = pis(-1,"");
    mp["ij"] = pis(1,"k");
    mp["jk"] = pis(1,"i");
    mp["ki"] = pis(1,"j");
    mp["ik"] = pis(-1,"j");
    mp["ji"] = pis(-1,"k");
    mp["kj"] = pis(-1,"i");
    
    
    cin>>T;
    REP(i,T) {
        cin >> n1 >> n2 >> s1;
        
        s0 = "";
        n3 = n2%4;
        if (n3==0) {
            n3=4;
        }
        REP(i, n2) {
            s0 += s1;
        }
        sum = 1;
        flag = 0;
        s2 = s0[0];
        REP(i, s0.length()-1) {
            if (s2=="i" && flag==0) {
                s2 = s0[i+1];
                flag = 1;
            } else if (s2=="j" && flag==1) {
                s2 = s0[i+1];
                flag = 2;
            } else {
                s2 += s0[i+1];
                sum *= mp[s2].fst;
                s2 = mp[s2].snd;
            }
        }
        if (s2=="k" && sum==1 && flag==2) {
            sr = "YES";
        } else {
            sr = "NO";
        }
        
        cout << "Case #" << i+1 << ": " << sr <<endl;
    }
    return 0;
}

