//
//  R1A_ProblemA.cpp
//  R1A_ProblemA
//
//  Created by meltaweel on 4/11/15.
//  Copyright (c) 2015 meltaweel. All rights reserved.
//

#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <iterator>

using namespace std;

#define toDigit(c) (c-'0')


int ReadNumbers( const string & s, vector <int> & v ) {
    istringstream is( s );
    int n;
    while( is >> n ) {
        v.push_back( n );
    }
    
    //std::sort (v.begin(), v.end());
    //std::reverse(v.begin(),v.end());
    
    return (int)v.size();
}

int T,i;
int main(int argc, char *args[]) {
    
    if (argc == 2 && strcmp(args[1], "small") == 0) {
        freopen("small.in","rt",stdin);
        freopen("small.out","wt",stdout);
    }
    else if (argc == 2 && strcmp(args[1], "large") == 0) {
        freopen("large.in","rt",stdin);
        freopen("large.out","wt",stdout);
    }
    else {
        freopen("test.in", "r", stdin);
        
    }
    
    cin>>T;
    int j,minA,minB,N,mi,temp_m,max_B,max_B_i;
    string mushroms;
    int B_rate;
     vector<int> m;

    for (i=1; i<T+1; i++) {
        minA=0;
        minB=0;
        cin>>N;
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

        getline(cin,mushroms);
        ReadNumbers(mushroms, m);
        mi = temp_m = m[0];
        /*
        max_B=*max_element(m.begin(),m.end());
        max_B_i = (int) distance(m.begin(), max_element(m.begin(), m.end() ));
        if(max_B_i < (N-1)){
            B_rate = (max_B - m[max_B_i+1]);
            if(B_rate == 0 && max_B_i != N-2)
                B_rate = max_B;
        }else{
            B_rate = 0;
        }
        
        if(B_rate > 0 && (mi<=B_rate)){
            minB = mi;
            cout<<minB<<"-";
        }*/
        
        B_rate = m[0]-m[1];

        for(j=1;j<N;j++){
            B_rate = max(B_rate,(m[j-1] - m[j]));
        
        }
        //cout<<B_rate;
        
        //B_rate = m[N-2]-m[N-1];
        if(B_rate > 0 && (mi<=B_rate)){
            minB = mi;
            //cout<<minB<<"-";
        }else if(B_rate > 0 && (mi>B_rate) && mi > 0){
            minB += B_rate;
//            cout<<minB<<"---";
        }
        
        for(j=1;j<N;j++){
            
            mi=m[j];
            if(temp_m>mi)
                minA += temp_m - mi ;
         
            
            temp_m = mi;
            
            if(j<N-1){
            if(B_rate > 0 && (mi<=B_rate)){
                minB += mi;
//                            cout<<minB<<"--";
            }else if(B_rate > 0 && (mi>B_rate) && mi > 0){
                minB += B_rate;
                           // cout<<minB<<"---";
            }
            }
            
        }

        
        
        printf("Case #%d: %d %d", i,minA,minB);
        cout<<endl;
        m.clear();
    }
    
    return 0;
}


