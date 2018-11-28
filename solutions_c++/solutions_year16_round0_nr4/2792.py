//
//  main.cpp
//  codejam
//
//  Created by Todor Lyubomirov Bonchev on 1/1/16.
//

#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <cmath>
#include <queue>

using namespace std;

unsigned long long kc(int k, int c) {
    unsigned long long rez=1;
    unsigned long long val=(unsigned long long)k;
    int pow = c;
    while(pow>0) {
        if (pow%2==1) {
            rez*=val;
        }
        val*=val;
        pow/=2;
    }
    return rez;
}

void solve() {
    int k,c,s;
    cin >>k>>c>>s;
    unsigned long long mx = kc(k,c);
    unsigned long long interval=mx/s;
    vector<unsigned long long> rz;
    unsigned long long cur=1;
    for (int i=1;i<=s;++i) {
        rz.push_back(cur);
        cur += interval;
    }
    for (int i=0;i<rz.size();++i) {
        putchar(' ');
        cout << rz[i];
    }
    cout << endl;
}

int main(int argc, const char * argv[]) {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);

    int tests;
    scanf("%d\n", &tests);
    for (int test=1;test<=tests;++test) {
        printf("Case #%d:", test);
        solve();
    }

    return 0;
}
