//
//  main.cpp
//  codeJam
//
//  Created by Wei Hu on 4/11/15.
//  Copyright (c) 2015 Wei Hu. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <unordered_map>
#include <vector>
#include <unordered_set>
#include <queue>
#include <map>
#include <sstream>
#include <stack>
#include <list>
#include <unordered_set>
#include <algorithm>

using namespace std;


void standingOvation()
{
    ifstream inFile("/Users/weihu/Desktop/me/leetcode/untitled folder/untitled folder/codeJam/codeJam/A-large.in");
    ofstream outFile("/Users/weihu/Desktop/me/leetcode/untitled folder/untitled folder/codeJam/codeJam/output_large");
    string line;
    if (!inFile.is_open())
    {
        cout << "input not found" << endl;
        return;
    }
    if (!outFile.is_open())
    {
        cout << "output cannot be opened" << endl;
        return;
    }
    int caseNum = 0;
    while(getline(inFile, line))
    {
        if (caseNum == 0)
        {
            caseNum ++;
            continue;
        }
        //cout << "line is " << line << endl;
        stringstream ss(line);
        int maxShyness;
        ss >> maxShyness;
        //cout << "maxShyness is " << maxShyness << endl;
        string operation;
        ss >> operation;
        //cout << "operation is " << operation << endl;
        int addFriend = 0;
        int preSum = 0;
        for (int i = 0; i < operation.size(); i ++)
        {
            int currNum = operation[i] - '0';
            if (i == 0)
            {
                preSum += currNum;
                continue;
            }
            if (preSum < i)
            {
                addFriend += i - preSum;
                preSum = i;
            }
            preSum += currNum;
        }
        outFile << "Case #" << caseNum << ": " << addFriend << endl;
        
        caseNum ++;
    }
    inFile.close();
    outFile.close();
    return;
}

int main(int argc, const char * argv[])
{
    standingOvation();
    return 0;
}

