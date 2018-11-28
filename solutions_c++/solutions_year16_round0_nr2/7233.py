//
//  QualificationRoundB.cpp
//  Google_Code_jam
//
//  Created by xys on 4/9/16.
//  Copyright © 2016 xys. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(){
    int T;
    string S;
    ifstream input("/Users/xys/Coding/Google_Code_jam/Google_Code_jam/B-large.in");
    ofstream output("/Users/xys/Coding/Google_Code_jam/Google_Code_jam/B-large.out");
    input >> T;
    for (int i = 1; i <= T; i++) {
        input >> S;
        int len = S.length();
        int blockCnt = 1;
        int idx = len - 1;
        while (S[idx] == '+' && idx >= 0) {
            idx--;
        }
        if (idx < 0) {
            output << "Case #" << i << ": 0" << endl;
            continue;
        }
        for (int j = 1; j <= idx; j++) {
            if (S[j] != S[j - 1]) {
                blockCnt++;
            }
        }
        output << "Case #" << i << ": " << blockCnt << endl;
        
    }
    output.close();
}
