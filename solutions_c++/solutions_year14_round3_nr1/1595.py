//
//  main.cpp
//  A
//
//  Created by Dmytro Kotsur on 5/11/14.
//  Copyright (c) 2014 Dmytro Kotsur. All rights reserved.
//

#include <iostream>
#include <string>
#include <fstream>

using namespace std;

long long T, P, Q;
char c;

ifstream in("/Users/dkotsur/Projects/Contests/Google Code Jam 2014/Round 1C/A/A/in.txt");
ofstream out("/Users/dkotsur/Projects/Contests/Google Code Jam 2014/Round 1C/A/A/out.txt");

long long degree(long long n) {
    long long  deg = 0, p = 1;
    while (p < n) {
        p = p << 1;
        deg++;
    }
    if (p > n)
        return -1;
    return deg;
}

long long  less_degree(long long n) {
    long long deg = 0, p = 1;
    while (p < n) {
        p = p << 1;
        deg++;
    }
    if (p > n)
        return deg-1;
    return deg;
}

long long gcd(long long a, long long b) {
    while (b != 0) {
        long long r = a % b;
        a = b;
        b = r;
    }
    return a;
}

long long multiplier(long long q) {
    
    long long deg = 0, p = 1;
    while (deg <= 40) {
        if (p % q == 0) {
            break;
        }
        p = p << 1;
        deg++;
    }
    if (deg <= 40)
        return p;
    return -1;
}


int main(int argc, const char * argv[])
{
    in >> T;
    for (int t = 1; t <= T; ++t) {
        in >> P >> c >> Q;
        
        out << "Case #" << t << ": ";
        
        long long g = gcd(P, Q);
        P /= g; Q /= g;
        
        long long d = degree(Q);
        long long q = less_degree(P);
        
        cout << q << " " << d << " " << d - q << endl;
        
        if (d == -1) {
            out << "impossible " << endl;
            cout << "impossible " << d << endl;
        } else {
            cout << d << endl;
            out << d - q << endl;
        }
        
    }
    
    return 0;
}

