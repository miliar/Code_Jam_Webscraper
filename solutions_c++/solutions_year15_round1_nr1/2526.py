//
//  main.cpp
//  Mushroom
//
//  Created by Loc Ngo on 4/17/15.
//  Copyright (c) 2015 Loc Ngo. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <algorithm>
#include <math.h>
using namespace std;
ifstream fin("/Users/locngo/Documents/Codejam/Mushroom/A-large.in");
long long P[10000];
int n;

void process(int t){
    fin>>n;
    for(int i=0;i<n;i++)
        fin>>P[i];
    long long p = 0;
    for(int i=1;i<n;i++)
        if(P[i]<P[i-1])
            p += P[i-1]-P[i];
    long long q=0;
    long long mv = 0;
    for(int i=0;i<n-1;i++)
        mv = max(P[i]-P[i+1],mv);
    
    for(int i=0;i<n-1;i++)
        q += min(P[i],mv);

    cout<<"Case #"<<t<<": "<<p<<" "<<q<<endl;
}

int main(int argc, const char * argv[]) {
    // insert code here...
    int T;
    fin>>T;
    for(int i=1;i<=T;i++)
        process(i);
    return 0;
}
