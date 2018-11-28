//
//  main.cpp
//  Fractiles
//
//  Created by MichelleShieh on 4/9/16.
//  Copyright (c) 2016 MichelleShieh. All rights reserved.
//

#include <iostream>

using namespace std;

int main() {
    int t,k,c,s;
    cin>>t;
    for (int i=1;i<=t;i++) {
        cin>>k>>c>>s;
        cout<<"Case #"<<i<<":";
        for (int i=1;i<=k;i++) {
            cout<<" "<<i;
        }
        cout<<endl;
    }
    return 0;
}
