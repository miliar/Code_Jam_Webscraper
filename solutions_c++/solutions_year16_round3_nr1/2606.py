//
//  Round1C_problemA.cpp
//  Google_Code_jam
//
//  Created by xys on 5/8/16.
//  Copyright © 2016 xys. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

struct Party {
    char name;
    int cnt;
};

bool myCompare(Party A, Party B) {
    return A.cnt <= B.cnt;
}

int main(){
    ifstream infile("/Users/xys/Coding/Google_Code_jam/Google_Code_jam/Round1C_testCase/A-large.in");
    ofstream outfile("/Users/xys/Coding/Google_Code_jam/Google_Code_jam/Round1C_testCase/A-large.out");
    
    int T;
    int partyNum;
    infile >> T;
    
    for (int i = 1; i <= T; i++) {
        Party party;
        infile >> partyNum;
        int total = 0;
        
        vector<Party> pVec(partyNum);
        for (int j = 0; j < partyNum; j++) {
            pVec[j].name = (char)('A' + j);
            infile >> pVec[j].cnt;
            total += pVec[j].cnt;
        }
        
        make_heap(pVec.begin(), pVec.end(), myCompare);
        
        outfile << "Case #" << i << ":";
        while (total > 3) {
            outfile << " " << pVec.front().name;
            pVec.front().cnt -= 1;
            if (pVec.front().cnt == 0) {
                pop_heap(pVec.begin(), pVec.end(), myCompare);
                pVec.pop_back();
            }
            make_heap(pVec.begin(), pVec.end(), myCompare);
            
            outfile << pVec.front().name;
            pVec.front().cnt -= 1;
            if (pVec.front().cnt == 0) {
                pop_heap(pVec.begin(), pVec.end(), myCompare);
                pVec.pop_back();
            }
            make_heap(pVec.begin(), pVec.end(), myCompare);
            total -= 2;
        }
        
        // must be 1 1 1 or 1 1
        if (total == 3) {
            outfile << " " << pVec.front().name;
        }
        
        outfile << " " << pVec[pVec.size() - 1].name << pVec[pVec.size() - 2].name;
        outfile << endl;
    }
    
    infile.close();
    outfile.close();
    return 0;
}
