//
//  main.cpp
//  CodeJam2014
//
//  Created by 马 丁 on 4/12/14.
//  Copyright (c) 2014 Ding Ma. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;


int main(int argc, const char * argv[])
{
    int n;
    FILE* pfile;
    pfile = fopen("./A-small-attempt0.in", "r");
    char* STR = new char[101];
    fscanf(pfile, "%d\n", &n);
    for (int tc = 1; tc <= n; ++tc)
    {
        int a[4];
        int g1, g2;
        fscanf(pfile, "%d\n", &g1);
        int beforeG1 = g1 - 1;
        int afterG1 = 4 - g1;
        for (int i = 0; i < beforeG1; ++i)
        {
            fgets(STR, 100, pfile);
        }
        fscanf(pfile, "%d %d %d %d\n", &a[0], &a[1], &a[2], &a[3]);
        for (int i = 0; i < afterG1; ++i)
        {
            fgets(STR, 100, pfile);
        }
        
        int b[4];
        fscanf(pfile, "%d\n", &g2);
        int beforeG2 = g2 - 1;
        int afterG2 = 4 - g2;
        for (int i = 0; i < beforeG2; ++i)
        {
            fgets(STR, 100, pfile);
        }
        fscanf(pfile, "%d %d %d %d\n", &b[0], &b[1], &b[2], &b[3]);
        for (int i = 0; i < afterG2; ++i)
        {
            fgets(STR, 100, pfile);
        }
        
        int res = -1;
        for (int i = 0; i < 4; ++i)
        {
            for (int j = 0; j < 4; ++j)
            {
                if (a[i] == b[j])
                {
                    if (res != -1)
                    {
                        printf("Case #%d: Bad magician!\n", tc);
                        i = 10;
                        j = 10;
                        res = -2;
                        continue;
                    }
                    res = a[i];
                }
            }
        }
        if (res == -2)
        {
            continue;
        }
        if (res == -1)
        {
            printf("Case #%d: Volunteer cheated!\n", tc);
        }
        else
        {
            printf("Case #%d: %d\n", tc, res);
        }
    }
}

