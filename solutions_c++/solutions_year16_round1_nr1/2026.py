//
//  main.cpp
//  problem4
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

// ABCDEFGHIJKLMNOPQRSTUVWXYZ
string solve(string S)
{
    // find max
//    char max_char = 'A';
//    for (int i = 0; i < S.length(); i++) {
//        if (max_char < S.at(i))
//            max_char = S.at(i);
//    }
    
    string result = "";
    result.push_back(S.at(0));

    for (int i = 1; i < S.length(); i++) {
//        if (max_char == S.at(i))
//            result = S.at(i) + result;
//        else
//            result = result + S.at(i);
        char c = S.at(i);
        if (c < result.at(0))
            result = result + S.at(i);
        else
            result = S.at(i) + result;
    }
    
    return result;
}

int main(int argc, const char * argv[]) {
    int T;
    cin >> T;
    
    for (int i = 0; i < T; i++) {
        string S;
        cin >> S;
        string ans = solve(S);
        cout << "Case #" << i+1 << ": " << ans << endl;
    }

//    cout << solve("CAB") << endl;
//    cout << solve("JAM") << endl;
//    cout << solve("CODE") << endl;
//    cout << solve("ABAAB") << endl;
//    cout << solve("CABCBBABC") << endl;
    
    return 0;
}
