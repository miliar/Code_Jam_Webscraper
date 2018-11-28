//
//  FALLSP.cpp
//  
//
//  Created by Manh Le on 9/4/16.
//
//

#include <iostream>
#include <cstdio>
#include <string>
#include <vector>

using namespace std;

bool digits[20];

void openFile() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
}

void markDigits(long long x) {
    
    while (x > 0) {
        digits[x % 10] = true;
        x /= 10;
    }
    
}

bool checkDigits() {
    for(int i = 0; i < 10; i++) {
        if (!digits[i]) {
            return false;
        }
    }
    
    return true;
}

void solve(int n) {
    
    if (n == 0) {
        cout << "INSOMNIA" << endl;
        return;
    }
    
    memset(digits, false, sizeof(digits));
    int counter = 0;
    long long m = 0;
    while (!checkDigits() && counter < 1000) {
        counter++;
        m += n;
        markDigits(m);
    }
    
    if (!checkDigits()) {
        cout << "INSOMNIA" << endl;
    } else {
        cout << m << endl;
    }
    
    
}

void process() {
    
    int test = 0;
    cin >> test;
    for(int t = 1; t <= test; t++) {
        int n;
        cin >> n;
        cout << "Case #" << t << ": ";
        solve(n);
    }
}

int main() {
    
    openFile();
    process();
    return 0;
}
