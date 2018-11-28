//
//  main.cpp
//  B
//
//  Created by Kotsur on 03.05.14.
//  Copyright (c) 2014 Dmytro Kotsur. All rights reserved.
//

#include <iostream>
#include <fstream>

using namespace std;

ifstream in("/Users/userMac/Projects/Contests/Google Code Jam 2014/Round 1B/B/B/small_in.txt");
ofstream out("/Users/userMac/Projects/Contests/Google Code Jam 2014/Round 1B/B/B/small_out.txt");

long long T, A, B, K;

long long solve_brute(long long A, long long B, long long K);
long long solve_brute2(long long A, long long B, long long K);

int main(int argc, const char * argv[])
{
//    int r = 0;
//    for (int i = 0; i < 100; ++i) {
//        for (int j = 0; j < 1000000000; ++j)
//            for (int k = 0; k < 1000000000; ++k) {
//                if ((k & j) < 1000000000) {
//                    r++;
//                }
//            }
//    }
//    
    in >> T;
    for (int t = 1; t <= T; ++t) {
        in >> A >> B >> K;
        out << "Case #" << t << ": " << solve_brute(A, B, K) << endl;
    }
    return 0;
}

long long solve_brute(long long A, long long B, long long K) {
    
    long long result = 0;
    for (long long a = 0; a < A; ++a) {
        for (long long b = 0; b < B; ++b) {
            if ((a & b) < K)
                result++;
        }
    }
    return result;
    
}

long long solve_brute2(long long A, long long B, long long K) {
    
    long long result = K * K + (A - K) * K + (B - K) * K;
    for (long long a = K; a < A; ++a) {
        for (long long b = K; b < B; ++b) {
            if ((a & b) < K) {
                result++;
            }
        }
    }
    return result;
    
}