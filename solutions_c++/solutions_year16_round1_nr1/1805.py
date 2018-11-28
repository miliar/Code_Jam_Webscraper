//
//  Round1A_problemA.cpp
//  Google_Code_jam
//
//  Created by xys on 4/16/16.
//  Copyright © 2016 xys. All rights reserved.
//

#include <fstream>
#include <string>
using namespace std;

int main(){
    ifstream infile("/Users/xys/Coding/Google_Code_jam/Google_Code_jam/Round1A_testCase/A-large.in");
    ofstream outfile("/Users/xys/Coding/Google_Code_jam/Google_Code_jam/Round1A_testCase/A-large.out");
    int T;
    string S;
    
    infile >> T;
    
    for (int i = 1; i <= T; i++) {
        infile >> S;
        int len = S.length();
        string lastWord(1, S[0]);
        //char head = lastWord[0];
        
        for (int j = 1; j < len; j++) {
            if (S[j] >= lastWord[0]) {
                lastWord = S[j] + lastWord;
            }
            else lastWord = lastWord + S[j];
        }
        
        outfile << "Case #" << i << ": " << lastWord << endl;
    }
    infile.close();
    outfile.close();
    return 0;
}
