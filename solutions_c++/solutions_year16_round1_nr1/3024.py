//
//  main.cpp
//  cpp
//
//  Created by Sean Kim on 4/16/16.
//  Copyright © 2016 topcoder. All rights reserved.
//

#include <iostream>
#include <cmath>
#include <ctime>
#include <string>
#include <vector>
#include <algorithm>
#include <numeric>
#include <set>
#include <limits>
#include <map>
#include <sstream>
#include <iterator>
#include <queue>
#include <stack>
#include <cfloat>
#include <cstring>
#include <limits.h>
using namespace std;

#define FOR(i,a,b) for(int i = a, _b = b; i <= _b; i++)
#define FORD(i,a,b) for(int i = a, _b = b; i >= _b; i--)
#define REP(i,n) for(int i = 0, _n = n; i < _n; i++)
#define MEM(a, b) memset(a, (b), sizeof(a))

#define MOD 1000000007
#define PI 3.14159265359

int main(int argc, const char * argv[]) {
    
    
    int cases;
    
    cin >> cases;
    
    REP(caseN, cases) {
        string S;
        cin >> S;
        
        string r = "";
        
        REP(i,(int)S.length()) {
            if (r[0] > S[i]) {
                r += S[i];
            } else {
                string a = S[i] + r;
                r = a;
            }
        }

        printf("Case #%d: %s\n", caseN+1, r.c_str());
    }
    
    return 0;
}
