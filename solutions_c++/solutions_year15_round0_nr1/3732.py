//
//  main.cpp
//  CodeJam
//
//  Created by akhilesh chaudhary on 11/04/15.
//  Copyright (c) 2015 Codenation. All rights reserved.
//

#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main(int argc, const char * argv[]) {
    ofstream cout;
    ifstream cin;
    cin.open("//Users//akhileshchaudhary//Desktop//in.in",ios::in);
    cout.open("//Users//akhileshchaudhary//Desktop//out.txt",ios::out);
    int t, max_level ;
    string str;
    cin>>t ;
    int cnt=0 ;
    while (t--) {
        cnt++;
        cin>>max_level;
        cin>>str;
        int total = -1 ;
        int ans = 0 ;
        for (int i=0; i<=max_level; i++) {
            total += str[i]-'0';
            if (total<i) {
                ans+=i-total;
                total += i-total;
            }
        }
        cout <<"Case #"<<cnt<<": " <<ans<<endl;
    }
    return 0;
}
