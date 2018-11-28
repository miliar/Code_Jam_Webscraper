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
    int x = 0, r = 0, c = 0, caseNum = 0, curCase = 0;
    string line;
    ifstream infile("D-small-attempt0.in");
    ofstream outfile("D-small-attempt0.out");
    infile >> caseNum;
    while ((infile >> x >> r >> c) && curCase < caseNum)
    {
        curCase++;
        if ((r * c) % x != 0)
        {
            outfile << "Case #" <<curCase << ": RICHARD" << endl;
            continue;
        }
        else if (x >= 7)
        {
            outfile << "Case #" <<curCase << ": RICHARD" << endl;
            continue;
        }
        else if (x >= 2 && ((x - 1) > r || (x - 1) > c))
        {
            outfile << "Case #" <<curCase << ": RICHARD" << endl;
            continue;
        }
        else
        {
            outfile << "Case #" <<curCase << ": GABRIEL" << endl;
            continue;
        }
        
    }
    return 0;
}
