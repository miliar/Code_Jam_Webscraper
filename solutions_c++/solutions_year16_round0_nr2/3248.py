//
//  main.cpp
//  Pancake
//
//  Created by MichelleShieh on 4/9/16.
//  Copyright (c) 2016 MichelleShieh. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;


int main() {
    int t;
    char s[101];
    cin >> t;
    for (int i=1;i<=t;i++) {
        cin>>s;
        int ans = 0;
        int j = 0;
        for (; s[j]!='\0';) {
            int k = j+1;
            while (s[k]!='\0' && s[k]==s[j]) {
                k++;
            }
            if (s[k]!='\0' && s[k] != s[j]) {
                ans++;
            }
            j=k;
        }
        if (s[j-1] == '-') {
            ans++;
        }
        cout << "Case #"<<i<<": "<<ans <<endl;
    }
    return 0;
}
