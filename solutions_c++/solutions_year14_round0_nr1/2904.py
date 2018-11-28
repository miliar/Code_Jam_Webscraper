//
//  main.cpp
//  testalgo
//
//  Created by William Hutama on 12/4/14.
//  Copyright (c) 2014 William Hutama. All rights reserved.
//

#include <stdio.h>
#include <string.h>

int main()
{
    int n;
    int bin[17];
    
    scanf("%d", &n);

    for (int i = 0; i < n; ++i)
    {
        memset(bin, 0, sizeof(bin));
        int d = 0;
        int res = 0;
        
        for (int k = 0; k < 2; ++k)
        {
            int row;
            scanf("%d", &row);
            
            int a[4];
            int b;
            for (int j = 0; j < 4; ++j)
            {
                if (j == (row-1))
                {
                    scanf("%d %d %d %d", &a[0], &a[1], &a[2], &a[3]);
                }
                else
                {
                    scanf("%d %d %d %d", &b, &b, &b, &b);
                }
            }
            
            for (int j = 0; j < 4; ++j)
            {
                ++bin[a[j]];
                if (bin[a[j]] > 1)
                {
                    ++d;
                    res = a[j];
                }
            }
        }
        
        if (d == 0)
        {
            printf("Case #%d: Volunteer cheated!\n", (i+1));
        }
        else if (d == 1)
        {
            printf("Case #%d: %d\n", (i+1), res);
        }
        else if (d > 1)
        {
            printf("Case #%d: Bad magician!\n", (i+1));
        }
    }
    
    return 0;
}

