//
//  main.cpp
//  CodeJam2015Qualification
//
//  Created by TangNing on 4/11/15.
//  Copyright (c) 2015 Ning Tang. All rights reserved.
//

#include <iostream>
#include <cstdlib>
#include <sstream>
#include <cstring>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <math.h>
#include <bitset>

using namespace std;
typedef long long ll;

int main(int argc, const char * argv[]) {
    freopen("/Users/tangning/in","r",stdin);
    FILE *ofile = fopen("/Users/tangning/output", "w");
    int T, Smax;
    string audience;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cin >> Smax >> audience;
        int cnt = 0, j = 0, friends = 0;
        for (; j <= Smax; ++j) {
            if (cnt >= j)
                cnt += (audience[j] - '0');
            else {
                friends += (j - cnt);
                cnt = j + (audience[j] - '0');
            }
        }
        fprintf(ofile, "Case #%d: %d\n", i, friends);
    }
    
    return 0;
}