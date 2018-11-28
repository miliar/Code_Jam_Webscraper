//
//  main.cpp
//  QualificationRound2016
//
//  Created by Wenfeng G on 4/9/16.
//  Copyright © 2016 Wenfeng G. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <bitset>
using namespace std;

int getDivisor(long long n, int j) {
//    cout << "n:" << n << " j:" << j << endl;
    long long X(0);
    while (n) {
        X <<= 1;
        X |= (n & 1);
        n >>= 1;
    }
    
    for (int i = 3; i < 1000; ++i) {
        int res(0);
        long long x(X);
//        cout << "x:" << bitset<16>(x) << " j:" << j << " i:" << i << endl;
        while (x) {
            res = (res * j) % i;
            if (x & 1)
                res++;
            x >>= 1;
//            cout << "after shifting:" << bitset<16>(x);
//            cout << " res:" << res << endl;;
        }
        res %= i;
        if (!res)
            return i;
    }
    return 0;
}

int main(int argc, const char * argv[]) {
    ofstream outfile("/Users/Wenfeng/Desktop/a-small-out.txt");
    if (!outfile.is_open()) {
        cout << "file not open" << endl;
        return -1;
    }
    
    int T, N, J;
    
    cin >> T >> N >> J;
    for (int i = 1; i <= T; ++i) {
        outfile << "Case #" << i << ":" << endl;
        
        long long n = (1 << (N-1)) + 1;
        while (J) {
            int divisor[11];
            int j(0);
            for (j = 2; j < 11; ++j) {
                int r = getDivisor(n, j);
                if (r)
                    divisor[j] = r;
                else
                    break;
            }
            
            if (j == 11) {
                outfile << bitset<16>(n) << " ";
                for (int k = 2; k < 11; ++k)
                    outfile << divisor[k] << " ";
                outfile << endl;
                --J;
            }
            n += 2;
        }
    }
    outfile.close();
    return 0;
}
