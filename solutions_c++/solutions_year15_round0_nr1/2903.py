//
//  main.cpp
//  CodeJam15P
//
//  Created by Ningchen Ying on 4/11/15.
//  Copyright (c) 2015 Ningchen Ying. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <string>
using namespace std;


int main(int argc, const char * argv[]) {
    int T;
    freopen("/Users/YNingC/Documents/CodeForces/CodeJam15P/CodeJam15P/A-large.in","r",stdin);
    freopen("/Users/YNingC/Documents/CodeForces/CodeJam15P/CodeJam15P/A-large.out","w",stdout);
    cin>>T;
    for(int cas=1;cas<=T;cas++){
        int ans,sm;
        cin>>sm;
        ans=0;
        string s;
        cin>>s;
        int cnt = 0;
        for(int j=0;j<=sm;j++){
            int a = s[j]-'0';
            if(cnt<j){
                ans+=j-cnt;
                cnt = j;
            }
            cnt+=a;
        }
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
