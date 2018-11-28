//
//  main.cpp
//  cj2014
//
//  Created by Boychuk, Petro on 4/11/14.
//  Copyright (c) 2014 Boychuk, Petro. All rights reserved.
//

#include <iostream>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;


void solve() {
    int n;
    double a[2000];
    double b[2000];
    
    cin >> n;
    for (int i=0; i<n; i++) {
        cin >> a[i];
    }
    for (int i=0; i<n; i++) {
        cin >> b[i];
    }
    
    sort(a, a+n);
    sort(b, b+n);
    
    int f = 0;
    int s = 0;
    
    int res0 = 0;
    int res1 = 0;
    
    while(f < n && s < n) {
        if(a[f] > b[s]) {
            res0++;
            s++;
        }
        f++;
    }
    
    f = 0;
    s = 0;
    res1 = n;
    
    while(s < n && f < n) {
        while (a[f] > b[s] && s < n) {
            s++;
        }
        if(s < n){
            res1--;
        }
        f++;
        s++;
    }
    cout << res0 << " " << res1;
}


int main(int argc, const char * argv[])
{
    
    freopen("inputD.txt", "r", stdin);
    freopen("outputD.txt", "w", stdout);
    
    int t;
    cin >> t;
    
    for (int i=0; i<t; i++) {
        cout << "Case #" << i+1 << ": ";
        solve();
        cout << endl;
        
    }
    
    return 0;
}

