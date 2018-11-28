//
//  Round1A_problemB.cpp
//  Google_Code_jam
//
//  Created by xys on 4/16/16.
//  Copyright © 2016 xys. All rights reserved.
//

#include <fstream>
#include <vector>
using namespace std;

int main(){
    ifstream infile("/Users/xys/Coding/Google_Code_jam/Google_Code_jam/Round1A_testCase/B-large.in");
    ofstream outfile("/Users/xys/Coding/Google_Code_jam/Google_Code_jam/Round1A_testCase/B-large.out");
    
    int T;
    infile >> T;
    
    for (int i = 1; i <= T; i++) {
        int N;
        infile >> N;
        int heightArray[2501]{0};
        for (int j = 0; j < 2 * N - 1; j++) {
            int soldierHeight;
            for (int k = 0; k < N; k++) {
                infile >> soldierHeight;
                heightArray[soldierHeight]++;
            }
        }
        vector<int> missingList;
        for (int height = 1; height <= 2500; height++) {
            if (heightArray[height] % 2 != 0) {
                missingList.push_back(height);
            }
        }
        
        outfile << "Case #" << i << ":";
        for (int j = 0; j < N; j++) {
            outfile << " " << missingList[j];
        }
        outfile << endl;
    }
    
    infile.close();
    outfile.close();
}
