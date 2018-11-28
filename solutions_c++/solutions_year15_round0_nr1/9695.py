//
//  main.cpp
//  codejam_A
//
//  Created by Junxing Wang on 4/11/15.
//  Copyright (c) 2015 Junxing Wang. All rights reserved.
//

#include <iostream>

using namespace std;

int t,n;

int main(int argc, const char * argv[]) {
    
    cin>>t;
    string st;
    for (int ti=0; ti<t; ti++){
        cin>>n>>st;
        int ans = 0, now = 0;
        for (int i=0; i<=n; i++){
            int k = st[i]-'0';
            if (now<i){
                ans = ans+i-now;
                now = i;
            }
            now = now+k;
        }
        cout<<"Case #"<<ti+1<<": "<<ans<<endl;
    }
    return 0;
}
