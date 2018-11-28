//
//  main.cpp
//  a
//
//  Created by qylqy on 14-4-12.
//  Copyright (c) 2014年 linqiuyan. All rights reserved.
//

#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <map>
using namespace std;

int main(int argc, const char * argv[])
{
    int T, i, j, a, b, n, I, cnt, num, x, k;
    int ans[5];
    scanf ("%d", &T);
    n = 4;
    for (I=1; I<=T; I++)
    {
        scanf ("%d", &a);
        a--;
        for (i=0; i<n; i++)
        {
            for (j=0; j<n; j++)
            {
                scanf ("%d", &k);
                if (i==a)
                {
                    ans[j] = k;
                }
            }
        }
        //for (i=0; i<n; i++) printf ("%d ", ans[i]); printf ("\n");
        
        scanf ("%d", &b);
        b--;
        cnt = 0;
        num = -1;
        for (i=0; i<n; i++)
        {
            for (j=0;  j<n; j++)
            {
                scanf ("%d", &k);
                if (i==b)
                {
                    for (x=0; x<n; x++)
                    {
                        if (ans[x]==k)
                        {
                            cnt++;
                            num = k;
                        }
                    }
                }
            }
        }
        if (cnt==0)
        {
            printf ("Case #%d: Volunteer cheated!\n", I);
        }
        else if (cnt>1)
        {
            printf ("Case #%d: Bad magician!\n", I);
        }
        else{
            printf ("Case #%d: %d\n", I, num);
        }
    }
    
    return 0;
}

