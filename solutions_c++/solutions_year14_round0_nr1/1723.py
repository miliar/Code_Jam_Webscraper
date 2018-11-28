//
//  main.cpp
//  Google1
//
//  Created by happy_1113xie on 14-4-12.
//  Copyright (c) 2014年 happy_1113xie. All rights reserved.
//

#include <fstream>
using namespace std;

int main(int argc, const char * argv[])
{
    ifstream f1;
    f1.open("/Users/happy_1113xie/Documents/develop/程序设计实习/Google1/A-small-attempt2.in");
    ofstream f2;
    f2.open("/Users/happy_1113xie/Documents/develop/程序设计实习/Google1/A.out");
    int num[4][4];
    int check[17];
    int answer = 0, flag, T, row;
    
    f1 >> T;
    for (int i = 1; i <= T; ++i){
        
        for (int j = 0; j < 17; ++j)
            check[j] = 0;
        
        f1 >> row;
        for (int j = 0; j < 4; ++j)
            for (int k = 0; k < 4; ++k)
                f1 >> num[j][k];
        
        for (int j = 0; j < 4; ++j)
            check[num[row - 1][j]]++;
        
        f1 >> row;
        for (int j = 0; j < 4; ++j)
            for (int k = 0; k < 4; ++k)
                f1 >> num[j][k];
        
        for (int j = 0; j < 4; ++j)
            check[num[row - 1][j]]++;
        
        flag = 0;
        for (int j = 1; j <= 16; ++j)
            if (check[j] == 2){
                ++flag;
                answer = j;
            }
        
        f2 << "Case #" << i << ": ";
        
        switch (flag){
            case 0:
                f2 << "Volunteer cheated!";
                break;
            case 1:
                f2 << answer;
                break;
            case 2:
                f2 << "Bad magician!";
                break;
            case 3:
                f2 << "Bad magician!";
                break;
            case 4:
                f2 << "Bad magician!";
                break;
            default:
                break;
        }
        
        f2 << endl;
    }
    f1.close();
    f2.close();
    return 0;
}

