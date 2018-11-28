//
//  main.cpp
//  test
//
//  Created by Hyunjun Kim on 2016. 4. 9..
//  Copyright © 2016년 Hyunjun Kim. All rights reserved.
//

#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <ctime>
#include <climits>
#include <cassert>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <map>
#include <bitset>
#include <utility>
#include <algorithm>

using namespace std;

long solve(string S) {
    int num_flip = 0;

    unsigned long len = S.length();
    char *str =(char *) malloc(sizeof(char) * len + 1);
    memset(str, 0, sizeof(char) * len + 1);
    memcpy(str, S.c_str(), sizeof(char) * len);
    
    long i = len - 1; // where to flip
    while (i >= 0) {
        // find - that is closest to the bottom
        for (i = len - 1; i >= 0; i--) {
            if (str[i] == '-') {
                break;
            }
        }
        
        // do flip
        if (i >= 0) {
            num_flip++;
            for (long j = i; j >= 0; j--) {
                if (str[j] == '-') str[j] = '+';
                else str[j] = '-';
            }
        } else {
            break;
        }
    }

    return num_flip;
}

int main(int argc, const char * argv[]) {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        string S;
        cin >> S;
        cout << "Case #" << i+1 << ": " << solve(S) << endl;
    }
//    cout << solve("-") << endl;
//    cout << solve("-+") << endl;
//    cout << solve("+-") << endl;
//    cout << solve("+++") << endl;
//    cout << solve("--+-") << endl;
//    cout << solve("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") << endl;
//    cout << solve("----------------------------------------------------------------------------------------------------") << endl;
//    cout << solve("-------------------------------------------------------------++-----------------------------------+-") << endl;
    return 0;
}
