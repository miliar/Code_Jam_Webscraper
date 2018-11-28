//
//  main.cpp
//  QRA-StandingOvation
//
//  Created by Xiaoyu Zhai on 4/11/15.
//  Copyright (c) 2015 Xiaoyu Zhai. All rights reserved.
//

#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int char2num(char temp)
{
    return temp - '0';
}
int main(int argc, const char * argv[]) {
    int add = 0, total = 0, sMax = 0, caseNum = 0, curCase = 0;
    string line;
    ifstream infile("A-small-attempt0.in");
    ofstream outfile("A-small-attempt0.out");
    infile >> caseNum;
    while ((infile >> sMax >> line) && curCase < caseNum)
    {
        curCase++;
        for (int i = 0; i < sMax; i++)
        {
            total += char2num(line[i]);
            if (total < i+1 && char2num(line[i+1]) != 0)
            {
                add = add + (i + 1 - total);
                total += add;
            }
        }
        outfile << "Case #" <<curCase << ": " << add << endl;
        total = 0;
        add = 0;
    }
    return 0;
}
