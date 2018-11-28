//
//  main.cpp
//  codejam
//
//  Created by Will Sawyer on 4/12/14.
//  Copyright (c) 2014 Will Sawyer. All rights reserved.
//

#include <iostream>
#include <vector>
#include <stdio.h>

using namespace std;
int main(int argc, const char * argv[])
{
    int N;
    int row, num, count = 0, sol = 0;
    cin >> N;
    vector<int> first;
    vector<int> second;
    for (int j = 0; j<N; j++)
    {
        count = 0;
        sol = 0;
        cin >> row;
        for (int k=0; k<4; k++)
        {
            for (int i=0; i<4; i++)
            {
                if (k == row-1)
                {
                    cin >> num;
                    first.push_back(num);
                }
                else
                {
                    cin >> num;
                }
            }
        }
        cin >> row;
        for (int k=0; k<4; k++)
        {
            for (int i=0; i<4; i++)
            {
                if (k == row-1)
                {
                    cin >> num;
                    second.push_back(num);
                }
                else
                {
                    cin >> num;
                }
            }
        }
        for (int k=0; k<4; k++) {
            for (int i=0; i<4; i++) {
                if (first[k] == second[i]) {
                    sol = first[k];
                    count++;
                }
            }
        }
        if (count == 1) {
            printf("Case #%d: %d\n", j+1, sol);
        }
        else if(count > 1)
        {
            printf("Case #%d: Bad magician!\n", j+1);
        }
        else
        {
            printf("Case #%d: Volunteer cheated!\n", j+1);
        }
        first.clear();
        second.clear();
    }
    return 0;
}

