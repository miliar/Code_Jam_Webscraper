//
//  main.cpp
//  1B_C
//
//  Created by Zulkarnine on 5/4/14.
//  Copyright (c) 2014 Zulkarnine Mahmud. All rights reserved.
//

#include <iostream>
#include <cstdlib>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <deque>
#include <list>


using namespace std;

typedef int int_type;

int maxLimit;

void solvecase(int_type A,int_type B,int_type C){
    
    int_type minNum=min(A, B);
    
    int_type count=0;
    for (int_type i=0; i<A; i++) {
        for (int_type j=0; j<B; j++) {
            if ((i&j)<C) {
                count++;
            }
        }
    }
    
    cout<<count<<"\n";
}


int main(int argc, const char * argv[])
{
    int T;
    int cas=0;
    //==============FINAL OUT================
        freopen("B-small-attempt0.in.txt", "r", stdin);
        freopen("test_b.out", "w", stdout);
    
    
    //================TEST==================
//    freopen("/Users/rezan_mahmud/Desktop/B-small-attempt0.in.txt", "r", stdin);
//    freopen("/Users/rezan_mahmud/Desktop/test_b.out", "w", stdout);
    
    
    cin>>T;
   
    while (T--) {
        int_type A,B,K;
        cin>>A>>B>>K;
        
        
        
        printf("Case #%d: ",++cas);
        solvecase(A,B,K);
    }
    
    
    
    return 0;
}

