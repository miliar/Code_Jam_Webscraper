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
using namespace std;

typedef unsigned long long int LLI;

#define _Test_

int main(int argc, const char * argv[]) {
#ifdef _Test_
    freopen("/Users/huixu/Desktop/APACTEST/test/test/A-large.in", "r", stdin);
    freopen("/Users/huixu/Desktop/APACTEST/test/test/A-large.out", "w", stdout);
#endif
    int T;
    LLI N,Norig;
    int flag=0; ///1111111111 = 说明都找到了
    cin>>T;
    for (int t=0; t<T; t++) {
        cin>>N;
        Norig=N;
        if (N == 0) {
            cout<<"Case #"<<t+1<<": INSOMNIA"<<endl;
        }else{
            while (flag!=1023) {
                LLI Ntemp = N;
                while (Ntemp!=0) {
                    if ( (flag & (1<<(Ntemp%10)) ) == 0) {
                        flag += 1<<(Ntemp%10);
                    }
                    Ntemp=Ntemp/10;
                }
                N+=Norig;
            }
            flag=0;
            cout<<"Case #"<<t+1<<": "<<N-Norig<<endl;
        }
        
    }
    return 0;
}
