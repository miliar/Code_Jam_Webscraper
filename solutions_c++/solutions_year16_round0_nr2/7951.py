//
//  main.cpp
//  test
//
//  Created by Shreyas Sinha on 09/04/16.
//  Copyright © 2016 Shreyas Sinha. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

typedef long long ll;

ll t,n;

int main() {
    ll count;
    ifstream infile;
    ofstream outfile;
    infile.open("B-large.in");
    outfile.open("output.in");
    string s;
    infile>>t;
    getline(infile,s);
    for(int y=1;y<=t;y++){
        getline(infile,s);
        char prev=s[0];
        count=0;
        for (int i=0; i<s.size(); i++) {
            if (prev!=s[i]) {
                prev=s[i];
                count++;
            }
        }
        if (prev!='+') {
            count++;
        }
        outfile<<"Case #"<<y<<": "<<count<<endl;
    }
    return 0;
}
