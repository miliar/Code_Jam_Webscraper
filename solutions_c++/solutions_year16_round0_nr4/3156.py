//
//  main.cpp
//  leetcode_cpp
//
//  Created by Xingying Liu on 4/5/16.
//  Copyright © 2016 Xingying Liu. All rights reserved.
//

# include <iostream>
# include <vector>
# include <math.h>

using namespace std;


int main(){
    int T, id = 1;
    cin>>T;
    int K, C, S;
    while (T--) {
        cout<<"Case #"<<id<<": ";
        id++;
        cin>>K>>C>>S;
        if (C==1)
            for (int i=1; i<=K; i++) cout<<i<<" ";
        else if (K==1)
            cout<<1;
        else
            for (int i=2; i<=K; i++) cout<<i<<" ";
        cout<<endl;
    }
    return 0;
}