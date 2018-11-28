//
//  main.cpp
//  ticTacToeTomec
//
//  Created by Nirbhai Singh on 13/04/13.
//  Copyright (c) 2013 Nirbhai Singh. All rights reserved.
//

#include <iostream>
using namespace std;
int main(int argc, const char * argv[])
{
    int no_of_tcases;
    cin >> no_of_tcases;
    for (int i=0; i<no_of_tcases; i++) {
        long long r,t,answer=0;
        cin>>r>>t;
        for (long long j=((r+1)*(r+1))-(r*r); j<=t;) {
            answer+=1;
            r+=2;
            j+=((r+1)*(r+1))-(r*r);
        }
        cout<<"Case #"<<i+1<<": "<<answer<<endl;
    }
    
    //    cout << "Hello, World!\n";
    return 0;
}