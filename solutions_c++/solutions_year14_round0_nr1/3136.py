//
//  main.cpp
//  EleProInter
//
//  Created by lhdgriver on 14-4-3.
//  Copyright (c) 2014年 lhdgriver. All rights reserved.
//

#include <iostream>
#include <vector>
#include <fstream>
using namespace std;


int one[5][5];
int two[5][5];

int main(int argc, const char * argv[])
{
    ifstream file;
    ofstream outfile;
    file.open("A.in");
    outfile.open("A.out");
    int T = 0, a1, a2;
    file >> T;
    for(int i = 1; i <= T; i++) {
        
        file >> a1;
        for(int j = 1; j <= 4; j++)
            for(int k = 1; k <= 4; k++)
                file >> one[j][k];
        
        file >> a2;
        for(int j = 1; j <= 4; j++)
            for(int k = 1; k <= 4; k++)
                file >> two[j][k];
        
        int tot = 0, ret = 0;
        for(int j = 1; j <= 4; j++)
            for(int k = 1; k <= 4; k++)
                if (one[a1][j] == two[a2][k]) {
                    tot++;
                    ret = one[a1][j];
                }
        if (tot == 0)
            outfile << "Case #" << i << ": Volunteer cheated!" << endl;
        else if (tot == 1)
            outfile << "Case #" << i << ": " << ret << endl;
        else
            outfile << "Case #" << i << ": Bad magician!" << endl;

    }
    file.close();
    outfile.close();
    return 0;
}