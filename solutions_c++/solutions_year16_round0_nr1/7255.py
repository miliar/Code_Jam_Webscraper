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

string solve(int N)
{
    if (N == 0)
        return "INSOMNIA";

    bool occur[10];
    memset(&occur, 0, sizeof(occur));
    int occur_count = 0;

    int i = 1;
    string num;
    
    while (i > 0) {
        num = to_string(i * N);
//        cout << num << endl;
        
        for (int j = 0; j < num.length(); j++) {
            int digit = num.at(j) - '0';
            if (!occur[digit]) {
                occur[digit] = true;
                occur_count++;
            }
//            printf("%d occur\n", digit);
        }
        
        if (occur_count == 10)
            break;
        i++;
    }
    
    return num;
}

int main(int argc, const char * argv[]) {
    int T;
    cin >> T;
    
    for (int i = 0; i < T; i++) {
        int N;
        cin >> N;
        string ans = solve(N);
        cout << "Case #" << i+1 << ": " << ans << endl;
    }

//    for (int i = 0; i < 100001; i++)
//        cout << solve(i) << endl;
//    cout << solve(99999) << endl;
    
    return 0;
}
