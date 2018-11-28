//
// Created by Santiago on 08/04/2016.
//

#include <iostream>
#include <bits/stdc++.h>

using namespace std;

void proc_digits(long long k, set<int> &digits) {
    while(k != 0) {
        digits.insert(k%10);
        k /=10;
    }
}

int main() {
    freopen("sheeps.in", "r", stdin);
    freopen("sheeps.out", "w", stdout);
    int N;
    cin>>N;
    for (int i = 0; i < N; ++i) {
        long long k;
        cin>>k;
        if(k == 0) {
            cout<<"Case #"<<i+1<<": ";
            cout<<"INSOMNIA"<<endl;
        }
        else {
            set<int> digits;
            long long mult = 1;
            long long ans = k;
            while (digits.size() < 10) {
                proc_digits(k*mult, digits);
                ans = k*mult;
                mult++;
            }
            cout<<"Case #"<<i+1<<": ";
            cout<<ans<<endl;
        }
    }
    return 0;
}

