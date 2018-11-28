//
//  main.cpp
//  cj13_round0_b
//
//  Created by Peizhi Wu on 4/12/13.
//  Copyright (c) 2013 Peizhi Wu. All rights reserved.
//

#include <iostream>
#include <cstdio>

#define MAX 100
int main()
{
    int T,TN, M, N, i, j, flag, mmax;
    int map[MAX][MAX],h[MAX][MAX];
    freopen("/Users/Peizhi/Documents/cpp/cj13_round0_b/cj13_round0_b/B-large.in","r",stdin);
    freopen("/Users/Peizhi/Documents/cpp/cj13_round0_b/cj13_round0_b/B-large.txt","w",stdout);
    scanf("%d\n", &TN);
    for (T = 0; T<TN; T++)
    {
        scanf("%d%d\n", &N, &M);
        for (i = 0; i<N; i++)
            for (j = 0; j<M; j++)
                scanf("%d", &map[i][j]);
//        for (i = 0; i<N; i++)
//        {   
//            for (j = 0; j<M; j++)
//                printf("%d ", map[i][j]);
//            putchar('\n');
//        }
        flag = 1;
        for (i = 0; i<N; i++)
        {
            mmax = 0;
            for (j = 0; j<M; j++)
                if (map[i][j] > mmax)
                    mmax =  map[i][j];
            for (j = 0; j<M; j++)
                if (map[i][j] < mmax)
                    h[i][j] =  1;
                else h[i][j] = 0;
        }
        if (flag)
        {
            for (j = 0; j<M; j++)
            {
                mmax = 0;
                for (i = 0; i<N; i++)
                    if (map[i][j] > mmax)
                        mmax =  map[i][j];
                for (i = 0; i<N; i++)
                    if (map[i][j] < mmax && h[i][j])
                    {   flag = 0;
                        break;
                    }
                if (flag == 0) break;
            }
        }
        if (flag)
            printf("Case #%d: YES\n", T+1);
        else
            printf("Case #%d: NO\n", T+1);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}


