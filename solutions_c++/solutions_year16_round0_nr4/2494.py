//
//  main.cpp
//  test
//
//  Created by Hui Xu on 3/22/16.
//  Copyright © 2016 Hui Xu. All rights reserved.
//
/*
 
 */

#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

typedef unsigned long long int LLI;

#define _Test_


int main(int argc, const char * argv[]) {
#ifdef _Test_
    freopen("/Users/huixu/Desktop/APACTEST/test/test/D-small-attempt0.in", "r", stdin);
    freopen("/Users/huixu/Desktop/APACTEST/test/test/D-small-attempt0.out", "w", stdout);
#endif
    int T;
    int K,C,S;
    cin>>T;
    for (int t=0; t<T; t++) {
        cin>>K>>C>>S;
        cout<<"Case #"<<t+1<<":";
        for (int k=0; k<K; k++) {
            cout<<' '<<k+1;
        }
        cout<<endl;
        
    }
    return 0;
}
