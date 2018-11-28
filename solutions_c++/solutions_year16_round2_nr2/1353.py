//
//  main.cpp
//  pb
//
//  Created by Rongbin Li on 4/30/16.
//  Copyright © 2016 Rongbin Li. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <cassert>
#include <cmath>
#include <iomanip>
using namespace std;

bool match(long long x, string s) {
    int n = s.size();
    for (int i=n-1; i>=0; i--) {
        int d = x % 10;
        x /= 10;
        if (s[i] != '?' && s[i] != '0'+d)
            return false;
    }
    return true;
}

void getAns(const string& s1, const string& s2, long long & x, long long & y) {
    size_t n = s1.size();
    unsigned long long power = 1;
    for (int i=1; i<=n; i++) {
        power *= 10;
    }
    for (long long diff = 0; diff < power; diff++) {
        for (long long i=0; i<power; i++) {
            if (match(i, s1)) {
                long long j = i - diff;
                if (j>=0 && match(j, s2)) {
                    x = i;
                    y = j;
                    return;
                }
                j = i + diff;
                if (j<power && match(j, s2)) {
                    x = i;
                    y = j;
                    return;
                }
            }
        }
    }
}

int main(int argc, const char * argv[]) {
    ifstream fin("B-small-attempt0.in");
    assert(fin);
    ofstream fout("pb-small.out");
    assert(fout);
    int test;
    fin >> test;
    for (int k = 1; k <= test; k++) {
        string s1, s2;
        fin >> s1 >> s2;
        long long ans1, ans2;
        getAns(s1, s2, ans1, ans2);
        const int n = s1.size();
        fout << "Case #" << k << ": " << setfill('0') << setw(n) << ans1 << ' ' << setw(n) << ans2 << endl;
    }
    fin.close();
    fout.close();
    return 0;
}
