//
//  main.cpp
//  CodeJam2014
//
//  Created by Benchmark on 4/12/14.
//  Copyright (c) 2014 Benchmark. All rights reserved.
//

#include <iostream>
#include <map>
#include <fstream>
#include <unistd.h>

using namespace std;

int main()
{

    ifstream cin("A-small-attempt0.in");
    ofstream cout("A-small-attempt0.out");
    int testCases;
    cin >> testCases;
    for (int i = 1; i <= testCases; i++)
    {
        int cards[4][4];
        int row[4];
        int firstAnswer;
        cin >> firstAnswer;
        for (int j = 0; j < 4; j++)
        {
            for (int k = 0; k < 4; k++)
            {
                cin >> cards[j][k];
                if (j == firstAnswer - 1)
                {
                    row[k] = cards[j][k];
                }
            }
        }
        int secondAnswer;
        cin >> secondAnswer;
        map <int,int> m;
        for (int j = 0; j < 4; j++)
        {
            for (int k = 0; k < 4; k++)
            {
                cin >> cards[j][k];
                if (j == secondAnswer - 1)
                {
                    m[cards[j][k]]++;
                }
            }
        }
        
        int found = 0;
        int result;
        for (int j = 0; j < 4; j++)
        {
            if (m[row[j]] > 0)
            {
                found++;
                result = row[j];
            }
        }
        if (found == 0)
            cout << "Case #" << i << ": Volunteer cheated!" << endl;
        else if (found == 1)
            cout << "Case #" << i << ": "  << result << endl;
        else
            cout << "Case #" << i << ": Bad magician!" << endl;
    }
    return 0;
}

