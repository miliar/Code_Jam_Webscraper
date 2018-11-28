//
//  main.cpp
//  A-small-problem
//
//  Created by Shreyas Sinha on 10/04/15.
//  Copyright (c) 2015 Shreyas Sinha. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main() {
    int t,sum,ans,n;
    string s;
    ofstream outfile;
    ifstream infile;
    infile.open("A-large.in");
    outfile.open("output.in");
    infile>>t;
    for (int k=1; k<=t; k++) {
        infile>>n;
        infile>>s;
        sum=0;
        ans=0;
        for (int i=0; i<=n; i++) {
            if (sum<i) {
                ans+=(i-sum);
                sum+=(i-sum);
            }
            sum+=s[i]-'0';
        }
        outfile<<"Case #"<<k<<": "<<ans<<"\n";
        s.clear();
    }
    outfile.close();
    infile.close();
    return 0;
}
