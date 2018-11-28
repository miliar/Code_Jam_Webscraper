/* 
 * File:   b.cpp
 * Author: Anton Boytsov
 *
 * Created on 14 Апрель 2013 г., 2:31
 */

#include <vector>


#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

int n;

const long long all[39] = {1, 2, 3, 11, 22, 101, 111, 121, 202, 212, 1001, 1111, 2002, 10001, 10101, 10201, 11011, 11111, 11211, 20002, 20102, 100001, 101101, 110011, 111111, 200002, 1000001, 1001001, 1002001, 1010101, 1011101, 1012101, 1100011, 1101011, 1102011, 1110111, 1111111, 2000002, 2001002};

bool isfair(long long a) {
    
    vector<long long> v;
    
    while (a > 0) {
        v.push_back(a % 10LL);
        a /= 10;
    }
    
    for (int i = 0; i < v.size(); i++) {
        if (v[i] != v[v.size() - i - 1])
            return false;
    }
    
    return true;
    
}


int main() {

    
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    cin >> n;

    for (int q = 1; q <= n; q++) {
        
        long long a, b;
        cin >> a >> b;
        int k = 0;
        for (int i = 0; i < 39; i++) {
            if (all[i] * all[i] >= a && all[i] * all[i] <= b)
                k++;
        }
        
        cout << "Case #" << q << ": " << k << endl;

    }

    return 0;
}