//
//  main.cpp
//  codejam
//
//  Created by Adam Bielski on 09.04.2016.
//  Copyright © 2016 Adam Bielski. All rights reserved.
//

#include <iostream>
#include <unordered_set>
using std::cin;
using std::cout;
using std::unordered_set;

unordered_set<unsigned long long> digits(unsigned long long n) {
    unordered_set<unsigned long long> digs;
    while (n!=0 && digs.size() < 10) {
        digs.insert(n%10);
        n/=10;
    }
    return digs;
}

unsigned long long solve(unsigned long long K) {
    if (K==0)
        return 0LL;
    unordered_set<unsigned long long> digs;
    unsigned long long KK = 0;
    while (digs.size() < 10) {
        KK += K;
        unordered_set<unsigned long long> tmp = digits(KK);
        digs.insert(tmp.begin(), tmp.end());
    }
    return KK;
}

int main(int argc, const char * argv[]) {
    int N;
    cin >> N;
    for (int i=0; i<N; ++i) {
        unsigned long long K;
        cin >> K;
        unsigned long long result = solve(K);
        if (result == 0LL) {
            cout << "Case #" << i+1 << ": " << "INSOMNIA" << std::endl;
        }
        else {
            cout << "Case #" << i+1 << ": " << result << std::endl;
        }
        
    }
    
    
    return 0;
}
