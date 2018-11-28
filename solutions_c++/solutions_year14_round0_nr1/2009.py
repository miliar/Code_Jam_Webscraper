//
//  main.cpp
//  magictrick
//
//  Created by Lydia Yang on 14-4-12.
//  Copyright (c) 2014年 杨荔雅5110309443. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream infile("/Users/apple/Desktop/in2.txt");
    ofstream out("/Users/apple/Desktop/out2.txt");
    int T = 0;
    infile >> T;
    int a = 0;
    int b = 0;
    int card_1[4][4];
    int card_2[4][4];
    int flag = 0;
    int ans = 0;
    for (int j = 0; j < 4; j++) {
        for (int k = 0; k<4; k++) {
            card_1[j][k] = 0;
            card_2[j][k] = 0;
        }
    }
    for (int i = 0; i < T; i++) {
        flag = 0;
        ans = 0;
        infile >> a;
        for (int j = 0; j < 4; j++) {
            for (int k = 0; k<4; k++) {
                infile >> card_1[j][k];
            }
        }
        infile >> b;
        for (int j = 0; j < 4; j++) {
            for (int k = 0; k<4; k++) {
                infile >> card_2[j][k];
            }
        }
        for (int j = 0; j < 4; j++) {
            for (int k = 0; k<4; k++) {
                if (card_1[a-1][j] == card_2[b-1][k]) {
                    flag++;
                    ans = card_1[a-1][j];
                }
            }
        }
        if (flag == 1) {
            out<<"Case #"<< i+1<<": "<<ans<<endl;
        }
        if (flag > 1) {
            out<<"Case #"<< i+1<<": Bad magician!"<<endl;
        }
        if (flag == 0) {
            out<<"Case #"<< i+1<<": Volunteer cheated!"<<endl;
        }
        
        
    }
    infile.close();
    out.close();
    return 0;
}

