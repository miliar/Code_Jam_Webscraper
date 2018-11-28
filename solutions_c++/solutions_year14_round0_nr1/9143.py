//
//  main.cpp
//  Code Jam 1
//
//  Created by Tony on 4/12/14.
//  Copyright (c) 2014 Tony. All rights reserved.
//
#include <iostream>
#include <vector>
#include <fstream>
using namespace std;
ifstream infile;
ofstream outfile;
void magic(int row1, int row2, int arr1[4][4], int arr2[4][4]) {
    int ans = 0;
    for (int i = 0; i < 4; i++) {
        int t = arr1[row1-1][i];
        for (int j = 0; j < 4; j++) {
            if (arr2[row2-1][j] == t) {
                if (ans == 0) {
                    ans = t;
                    continue;
                } else {
                    ans = -1;
                    outfile<<"Bad magician!\n";
                    return;
                }
            }
        }
    }
    if (ans == 0) outfile<<"Volunteer cheated!\n";
    else outfile<<ans<<"\n";
}
int main(int argc, const char * argv[])
{
    infile.open("/Users/Tony/Desktop/code jam/Code Jam 1/Code Jam 1/magic.in");
    outfile.open("/Users/Tony/Desktop/code jam/Code Jam 1/Code Jam 1/magic.out");
    int num_t;
    infile>>num_t;
    for (int i = 0; i < num_t; i++) {
        int r1,r2;
        int a1[4][4],a2[4][4];
        infile>>r1;
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                infile>>a1[i][j];
        infile>>r2;
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                infile>>a2[i][j];
        outfile<<"Case #"<<i+1<<": ";
        magic(r1,r2,a1,a2);
    }
    infile.close();
    outfile.close();
    return 0;
}

