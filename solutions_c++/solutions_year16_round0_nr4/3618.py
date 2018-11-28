//
//  main.cpp
//  codejam2016A
//
//  Created by Daniel Pompe on 09.04.16.
//  Copyright © 2016 DP. All rights reserved.
//

#include <cstdio>
#include <cstdlib>
#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    FILE *fin = freopen("test.in", "r", stdin);
    FILE *fout = freopen("test.out", "w", stdout);
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++){
        cout << "Case #" << t << ": ";
        int k, c, s;
        cin >> k >> c >> s;
        cout << 1;
        for(int i=2; i<=k; ++i)
            cout << " " << i;
        cout << "" << endl;
    }
    exit(0);
}
