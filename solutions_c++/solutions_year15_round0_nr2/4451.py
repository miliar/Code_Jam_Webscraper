//
//  main.cpp
//  standing ovation
//
//  Created by Saras Gupta on 11/04/15.
//  Copyright (c) 2015 sarasgupta. All rights reserved.
//

#include <iostream>
#include <cstring>
#include <vector>

using namespace std;

int main(int argc, const char * argv[]) {
    int t,ctr=1;
    cin>>t;
    while (t--) {
        int n,mx,ind,ans=1000000000,ct=0;
        vector<int> a;
        vector<int> b;
        cin>>n;
        for (int i=0; i<n; i++) {
            cin>>mx;
            a.push_back(mx);
            b.push_back(mx);
        }
        while (a.size()) {
            mx=0;ind=-1;
            for (int i=0; i<a.size(); i++) {
                if (mx<a[i]) {
                    mx=a[i];
                    ind=i;
                }
            }
            ans=min(ans, ct+mx);
            if (mx<=1) {
                break;
            }
            a.push_back(a[ind]/2);
            a[ind]=a[ind]-(a[ind]/2);
            ct++;
        }
        ct=0;
        while (b.size()) {
            mx=0;ind=-1;
            for (int i=0; i<b.size(); i++) {
                if (mx<b[i]) {
                    mx=b[i];
                    ind=i;
                }
            }
            ans=min(ans, ct+mx);
            if (mx<=1) {
                break;
            }
            if (mx==9) {
                b[ind]=6;
                b.push_back(3);
            }
            else {
                b.push_back(b[ind]/2);
                b[ind]=b[ind]-(b[ind]/2);
            }
            ct++;
        }
        cout<<"Case #"<<ctr<<": "<<ans<<endl;
        ctr++;
    }
    return 0;
}
