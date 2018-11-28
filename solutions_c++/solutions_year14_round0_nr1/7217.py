//
//  main.cpp
//  Magic Trick
//
//  Created by SourKream on 12/04/14.
//  Copyright (c) 2014 SourKream. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;


int main(int argc, const char * argv[])
{
    fstream fil;
    fil.open("input.txt",ios::in);
    int cases;
    fil >> cases;
    for(int i=1;i<=cases;i++)
    {
        cout << "Case #" << i << ": ";
        int ans1, ans2;
        int grid1[4][4] = {};
        int grid2[4][4] = {};
        fil >> ans1;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                fil >> grid1[i][j];
        fil >> ans2;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                fil >> grid2[i][j];
        int check=0;
        int match;
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            if(grid1[ans1-1][j]==grid2[ans2-1][k])
            { check++;
            if(check==1)
                match = grid1[ans1-1][j];
                }
        }
        if(check==1)
            cout << match << endl;
        else if (check==0)
            cout << "Volunteer cheated!\n";
        else
            cout << "Bad magician!\n";
        
        
    }
    fil.close();
    
    return 0;
}

