//
//  main.cpp
//  Pancake
//
//  Created by Loc Ngo on 4/11/15.
//  Copyright (c) 2015 Loc Ngo. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;
ifstream fin("/Users/locngo/Documents/Codejam/Pancake/B-large.in");
int A[1000];
int n;

void process(int t){
    int n;
    fin>>n;
    int h = 0;
    for(int i=0;i<n;i++){
        fin>>A[i];
        h = max(h,A[i]);
    }
    int ret = 1000000000;
    for(int j=1;j<=h;j++){
        int m = j;
        for(int i=0;i<n;i++){
            int mh = 0;
            if(A[i]%j==0)
                mh=A[i]/j-1;
            else
                mh=A[i]/j;
            m += mh;
        }
        ret = min(ret,m);
    }
    cout<<"Case #"<<t<<": "<<ret<<endl;
}

int main(int argc, const char * argv[]) {
    // insert code here...
    int T;
    fin>>T;
    for(int i=1;i<=T;i++)
        process(i);
    return 0;
}
