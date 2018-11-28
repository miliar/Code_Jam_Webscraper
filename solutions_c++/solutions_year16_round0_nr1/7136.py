//
//  QualificationRoundA.cpp
//  Google_Code_jam
//
//  Created by xys on 4/9/16.
//  Copyright © 2016 xys. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;

int main() {
    int T, N, kN;
    ifstream input("/Users/xys/Coding/Google_Code_jam/Google_Code_jam/A-large.in");
    ofstream output("/Users/xys/Coding/Google_Code_jam/Google_Code_jam/A-large.out");
    input >> T;
    for (int i = 1; i <= T; i++) {
        input >> N;
        kN = 0;
        if (N == 0) {
            output << "Case #" << i << ": INSOMNIA" << endl;
            continue;
        }
        int flag[10]{0};
        int zeroCnt = 10;
        while (1) {
            kN = kN + N;
            int temp = kN;
            while (temp > 0) {
                int lastDigit = temp % 10;
                if (flag[lastDigit] == 0) {
                    flag[lastDigit] = 1;
                    zeroCnt--;
                }
                temp = temp / 10;
            }
            if (zeroCnt == 0) {
                output << "Case #" << i << ": " <<  kN << endl;
                break;
            }
        }
        
    }
    output.close();
}
