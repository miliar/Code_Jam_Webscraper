//
//  ProblemC.cpp
//  CodeJam2014
//
//  Created by Benchmark on 4/12/14.
//  Copyright (c) 2014 Benchmark. All rights reserved.
//

#include <iostream>
#include <vector>
#include <algorithm>
#include "fstream"

using namespace std;
int getWinners(vector<float> first, vector<float> second);

int main()
{
    ifstream cin("D-large.in");
    ofstream cout("D-large.out");
    int testCases;
    cin >> testCases;
    for (int i = 1; i <= testCases; i++)
    {
        int n;
        cin >> n;
        vector<float> first,second;
        for (int j = 0; j < n; j++)
        {
            float temp;
            cin >> temp;
            first.push_back(temp);
        }

        for (int j = 0; j < n; j++)
        {
            float temp;
            cin >> temp;
            second.push_back(temp);
        }
        sort(first.begin(),first.end());
        sort(second.begin(), second.end());
        
        cout << "Case #" << i << ": " << getWinners(second, first) << " " << n - getWinners(first, second) << endl;
        
    }
    return 0;
}

int getWinners(vector<float> first, vector<float> second)
{
    int result = 0;
    for (int i = 0; i < first.size(); i++)
    {
        for (int k = 0; k < second.size(); k++)
        {
            if (first[i] < second[k] && first[i] > 0 && second[k] > 0)
            {
                result++;
                first[i] = -1;
                second[k] = -1;
                break;
            }
        }
    }
    return result;
}

