//
//  main.cpp
//  digits
//
//  Created by MichelleShieh on 4/30/16.
//  Copyright (c) 2016 MichelleShieh. All rights reserved.
//

#include <iostream>
using namespace std;

int main() {
    int t;
    int alphabet[26];
    int num[10];
    cin >> t;
    string s;
    int cnt;
    for (int i=1;i<=t;i++) {
        cin>>s;
        cnt=0;
        for (int j=0;j<26;j++) {
            alphabet[j]=0;
        }
        for (int j=0;j<10;j++) {
            num[j]=0;
        }
        for (int j=0;j<s.length();j++) {
            alphabet[s[j]-'A']++;
            cnt++;
        }
        cout<<"Case #"<<i<<": ";
        //cout<<cnt<<endl;
        //cout<<alphabet['Z'-'A']<<endl;
        while (cnt>0) {
            while (cnt>0 && alphabet['Z'-'A']!=0) {
                cnt-=4;
                alphabet['Z'-'A']--;
                alphabet['O'-'A']--;
                alphabet['N'-'A']--;
                alphabet['E'-'A']--;
                num[0]++;
            }
            while (cnt>0 && alphabet['W'-'A']!=0) {
                cnt-=3;
                alphabet['T'-'A']--;
                alphabet['W'-'A']--;
                alphabet['O'-'A']--;
                num[2]++;
            }
            while (cnt>0 && alphabet['U'-'A']!=0) {
                cnt-=4;
                alphabet['F'-'A']--;
                alphabet['O'-'A']--;
                alphabet['U'-'A']--;
                alphabet['R'-'A']--;
                num[4]++;
            }
            while (cnt>0 && alphabet['X'-'A']!=0) {
                cnt-=3;
                alphabet['S'-'A']--;
                alphabet['I'-'A']--;
                alphabet['X'-'A']--;
                num[6]++;
            }
            while (cnt>0 && alphabet['G'-'A']!=0) {
                cnt-=5;
                alphabet['E'-'A']--;
                alphabet['I'-'A']--;
                alphabet['G'-'A']--;
                alphabet['H'-'A']--;
                alphabet['T'-'A']--;
                num[8]++;
            }
            while (cnt>0 && alphabet['O'-'A']!=0) {
                cnt-=3;
                alphabet['O'-'A']--;
                alphabet['N'-'A']--;
                alphabet['E'-'A']--;
                num[1]++;
            }
            while (cnt>0 && alphabet['T'-'A']!=0) {
                cnt-=5;
                alphabet['T'-'A']--;
                alphabet['H'-'A']--;
                alphabet['R'-'A']--;
                alphabet['E'-'A']--;
                alphabet['E'-'A']--;
                num[3]++;
            }
            while (cnt>0 && alphabet['F'-'A']!=0) {
                cnt-=4;
                alphabet['F'-'A']--;
                alphabet['I'-'A']--;
                alphabet['V'-'A']--;
                alphabet['E'-'A']--;
                num[5]++;
            }
            while (cnt>0 && alphabet['S'-'A']!=0) {
                cnt-=5;
                alphabet['S'-'A']--;
                alphabet['E'-'A']--;
                alphabet['V'-'A']--;
                alphabet['E'-'A']--;
                alphabet['N'-'A']--;
                num[7]++;
            }
            while (cnt>0 && alphabet['N'-'A']!=0) {
                cnt-=4;
                alphabet['N'-'A']--;
                alphabet['I'-'A']--;
                alphabet['N'-'A']--;
                alphabet['E'-'A']--;
                num[9]++;
            }
        }
        for (int j=0;j<10;j++) {
            for (int k=0;k<num[j];k++) {
                cout<<j;
            }
        }
        cout<<endl;
    }
    return 0;
}
