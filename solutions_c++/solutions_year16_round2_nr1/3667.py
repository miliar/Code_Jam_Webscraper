//
//  main.cpp
//  CodeJam1bq1
//
//  Created by VIVEK GANGWAR on 30/04/16.
//  Copyright © 2016 VIVEK GANGWAR. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <climits>
#include <algorithm>
#include <queue>
#include <cstring>
#include <cmath>
#include <vector>
#include <list>
#include <stack>
#include <bitset>
#include <string>
#include <stack>
#include <set>
#include <map>
#include <assert.h>
#include <deque>
#include <ctime>

#define ALL(i,n)    for(i = 0; i < (n); i++)
#define FOR(i,a,b)  for(i = (a); i < (b); i++)
#define SET(p)      memset(p,-1,sizeof(p))
#define CLR(p)      memset(p,0,sizeof(p))
#define S(n)	    scanf("%d",&n)
#define P(n)	    printf("%d\n",n)
#define Sl(n)	    scanf("%lld",&n)
#define Pl(n)	    printf("%lld\n",n)
#define Sf(n)       scanf("%lf",&n)
#define Ss(n)       scanf("%s",n)
#define LL long long
#define ULL unsigned long long
#define pb push_back
using namespace std;
int main() {
    int tc;
    cin>>tc;
    vector<int>ph;
    string s;
    for (int i = 1;i <= tc;i++) {
        
        
        cin>>s;
        ph.clear();
        
        size_t f = s.find("Z");
        while(f != string::npos){
            s.replace(f,1,"");
            f = s.find("E");
            s.replace(f,1,"");
            f = s.find("R");
            s.replace(f,1,"");
            f = s.find("O");
            s.replace(f,1,"");
            f = s.find("Z");
            ph.push_back(0);
        }
        
        f = s.find("X");
        while(f != string::npos){
            s.replace(f,1,"");
            f = s.find("S");
            s.replace(f,1,"");
            f = s.find("I");
            s.replace(f,1,"");
            
            f = s.find("X");
            ph.push_back(6);
        }
        f = s.find("W");
        while(f != string::npos){
            s.replace(f,1,"");
            f = s.find("T");
            s.replace(f,1,"");
            f = s.find("O");
            s.replace(f,1,"");
            
            f = s.find("W");
            ph.push_back(2);
        }
        f = s.find("G");
        while(f != string::npos){
            s.replace(f,1,"");
            f = s.find("E");
            s.replace(f,1,"");
            f = s.find("I");
            s.replace(f,1,"");
            f = s.find("H");
            s.replace(f,1,"");
            f = s.find("T");
            s.replace(f,1,"");
            
            f = s.find("G");
            ph.push_back(8);
        }
        f = s.find("H");
        while(f != string::npos){
            s.replace(f,1,"");
            f = s.find("T");
            s.replace(f,1,"");
            f = s.find("R");
            s.replace(f,1,"");
            f = s.find("E");
            s.replace(f,1,"");
            f = s.find("E");
            s.replace(f,1,"");
            
            f = s.find("H");
            ph.push_back(3);
            
        }
        f = s.find("F");
        while(f != string::npos){
            if(s.find("U") != string::npos){
                s.replace(f,1,"");
                f = s.find("U");
                s.replace(f,1,"");
                f = s.find("O");
                s.replace(f,1,"");
                f = s.find("R");
                s.replace(f,1,"");
                ph.push_back(4);
                
            }else{
                s.replace(f,1,"");
                f = s.find("I");
                s.replace(f,1,"");
                f = s.find("V");
                s.replace(f,1,"");
                f = s.find("E");
                s.replace(f,1,"");
                ph.push_back(5);
                
                
            }
            f = s.find("F");
        }
        
        f = s.find("V");
        while(f != string::npos){
            s.replace(f,1,"");
            f = s.find("S");
            s.replace(f,1,"");
            f = s.find("E");
            s.replace(f,1,"");
            f = s.find("E");
            s.replace(f,1,"");
            f = s.find("N");
            s.replace(f,1,"");
            f = s.find("V");
            
            ph.push_back(7);
            
        }
        f = s.find("O");
        while(f != string::npos){
            s.replace(f,1,"");
            f = s.find("N");
            s.replace(f,1,"");
            f = s.find("E");
            s.replace(f,1,"");
            f = s.find("O");
            ph.push_back(1);
            
        }
        f = s.find("N");
        while(f != string::npos){
            s.replace(f,1,"");
            f = s.find("I");
            s.replace(f,1,"");
            f = s.find("N");
            s.replace(f,1,"");
            f = s.find("E");
            s.replace(f,1,"");
            f = s.find("N");
            ph.push_back(9);
            
        }
        sort(ph.begin(),ph.end());
        
        cout<<"Case #"<<i<<": ";
        for(int j=0;j<ph.size();j++){
            cout<<ph[j];
        }
        cout<<endl;
    }
    return 0;
}