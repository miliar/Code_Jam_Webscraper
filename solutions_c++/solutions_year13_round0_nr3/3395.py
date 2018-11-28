//
//  main.cpp
//  codejam2013qual
//
//  Created by Petro Boychuk on 4/13/13.
//  Copyright (c) 2013 Petro Boychuk. All rights reserved.
//

#include <iostream>
using namespace std;


bool palindrome(int n) {
    
    int a[1000];
    int c = 0;
    while(n){
        a[c++] = n % 10;
        n /= 10;
    }
    
    for (int i=0; 2*i < c; i++) {
        if(a[i] != a[c-i-1]){
            return false;
        }
    }
    
    return true;
    
}

int lessthan(int a) {
    int res = 0;
    for (int i=1; i*i <= a; i++) {
        if(palindrome(i) && palindrome(i*i)) {
            res++;
        }
    }
    return res;
}

void solve() {
 
    int a,b;
    cin >> a >> b;
    cout << lessthan(b) - lessthan(a-1);
    
}


int main(int argc, const char * argv[])
{
    
    freopen("inputC.txt", "r", stdin);
    freopen("outputC.txt", "w", stdout);

    int t;
    cin >> t;
    
    for (int i=0; i<t; i++) {
        cout << "Case #" << i+1 << ": ";
        solve();
        cout << endl;
    }
    
    
    return 0;
}

