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
int T(0),n0(0),n1(0),n2(0),n3(0),sum(0),flag(0),num(0);
string s0,s1,s2,s3,sr;
vi v,vsum;

int find(vi v) {
    int num = 0;
    int min = v[0];
    REP(i, SIZE(v)) {
        min = MIN(min,v[i]);
    }
    REPD(i, SIZE(v)) {
        if (min == v[i]) {
            num = i;
        }
    }
    //cout << num << ":"<<min << endl;
    return num;
}

int main()
{
    
    cin>>T;
    REP(i,T) {
        int rs = 0;
        int large = 0;
        int m(0),n(0),a(0),b(0),c(0);
        int all(0);
        v.clear();
        vsum.clear();
        cin >> n1 >> n2;
        REP(j, n1) {
            cin >> n3;
            v.pb(n3);
            vsum.pb(0);
        }
        a = v[0];
        REP(i, n1-1) {
            m = a;
            n = b = v[i+1];
            while(b!=0)
            {
                c=a%b;
                a=b;
                b=c;
            }
            a = m*n/a;
        }
        large = a;
        
        REP(i, n1) {
            all += (large/v[i]);
        }
        
        REP(i, (n2-1)%all) {
            flag = find(vsum);
            vsum[flag] += v[flag];
        }
        
        rs = find(vsum) + 1;
        
        
        cout << "Case #" << i+1 << ": " << rs <<endl;
    }
    return 0;
}