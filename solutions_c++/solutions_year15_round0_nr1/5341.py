//
//  main.cpp
//  standing ovation
//
//  Created by Saras Gupta on 11/04/15.
//  Copyright (c) 2015 sarasgupta. All rights reserved.
//

#include <iostream>
#include <cstring>

using namespace std;

int main(int argc, const char * argv[]) {
    int t,ctr=1;
    cin>>t;
    while (t--) {
        int n,len,mx=0,cur=0;
        char s[1005];
        cin>>n>>s;
        len=strlen(s);
        cur=s[0]-'0';
        for (int i=1; i<len; i++) {
            if (i>cur) {
                mx+=i-cur;
                cur+=i-cur;
            }
            cur+=s[i]-'0';
        }
        cout<<"Case #"<<ctr<<": "<<mx<<endl;
        ctr++;
    }
    return 0;
}
