//
//  main.cpp
//  c
//
//  Created by qylqy on 14-4-12.
//  Copyright (c) 2014年 linqiuyan. All rights reserved.
//

#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <map>
#include <cmath>
#include <cstring>
using namespace std;
const int maxn=13;

int bx[maxn*maxn], by[maxn*maxn], bn; //zero pos;
int vis[maxn][maxn]; //-1 is lei, 0 is zero, 1 is number;
int vn; //vis != -1;

int N, M, K;
bool found;


int dx[] = {-1, -1, -1, 0, 1, 1, 1, 0};
int dy[] = {-1, 0, 1, 1, 1, 0, -1, -1};

int ddx[] = {0, 1, 1};
int ddy[] = {1, 0, 1};

void dfscheck(int pi, int pj)
{
    if (found) return;
    
    int i, j, d, pre, x, bi, bj;
    bool chg[10];
    
    memset (chg, 0, sizeof chg);
    
    for (d=0; d<8; d++) //the round is 1;
    {
        i = pi+dx[d];
        j = pj+dy[d];
        if (i<0 || i>=N) continue;
        if (j<0 || j>=M) continue;
        if (vis[i][j]==-1)
        {
            chg[d] = 1;
            vis[i][j] = 1;
            vn++;
        }
    }
    
//    for (i=0; i<N; i++)
//    {
//        for (j=0; j<M; j++)
//        {
//            //if (bx[0]==i && by[0]==j) printf ("c");
//            if (vis[i][j]==0) printf ("c");
//            else if (vis[i][j]==-1)
//                printf ("*");
//            else
//                printf (".");
//        }
//        printf ("\n");
//    }
//    printf ("%d\n", vn);
    
    if (vn==K)
    {
        found = true;
        for (i=0; i<N; i++)
        {
            for (j=0; j<M; j++)
            {
                if (bx[0]==i && by[0]==j) printf ("c");
                //if (vis[i][j]==0) printf ("c");
                else if (vis[i][j]==-1)
                    printf ("*");
                else
                    printf (".");
            }
            printf ("\n");
        }
        return;
    }
    
    if (vn<K) for (x=0; x<bn; x++)
    {
        bi = bx[x]; //last 0;
        bj = by[x];
        for (d=0; d<3; d++)
        {
            i = bi+ddx[d];
            j = bj+ddy[d];
            if (i<0 || i>=N) continue;
            if (j<0 || j>=M) continue;
            if (vis[i][j]==0) continue;//is already;
            
            bx[bn] = i;
            by[bn++] = j;
            
            pre = vis[i][j];
            vis[i][j] = 0;
            if (pre==-1) vn++;
            
            dfscheck(i, j);
            if (found) break;
            
            bn--;
            vis[i][j] = pre;
            if (pre==-1) vn--;
            
        }
    }
    
    for (d=0; d<8; d++) //the round is 1;
    {
        i = pi+dx[d];
        j = pj+dy[d];
        if (i<0 || i>=N) continue;
        if (j<0 || j>=M) continue;
        if (chg[d] == 1)
        {
            vis[i][j] = -1;
            vn--;
        }
    }
//    
//    for (i=0; i<N; i++)
//    {
//        for (j=0; j<M; j++)
//        {
//            //if (bx[0]==i && by[0]==j) printf ("c");
//            if (vis[i][j]==0) printf ("c");
//            else if (vis[i][j]==-1)
//                printf ("*");
//            else
//                printf (".");
//        }
//        printf ("\n");
//    }
//    printf ("%d\n", vn);
}


int main()
{
    int T, I, i, j;
    scanf ("%d", &T);
    for (I=1; I<=T; I++)
    {
        scanf ("%d%d%d", &N, &M, &K);
        K = N*M - K;
        
        
        printf ("Case #%d:\n", I);
        
        if (K==1)
        {
            for (i=0; i<N; i++)
            {
                for (j=0; j<M; j++)
                    if (i==0 && j==0) printf ("c");
                    else printf ("*");
                printf ("\n");
            }
            continue;
        }
        
        found = false;
        bn=0; vn=0;
        memset (vis, -1, sizeof (vis));
        
        
        
        for (i=0; i<N; i++)
        {
            for (j=0; j<M; j++)
            {
                if (found) break;
                
                bx[bn] = i;
                by[bn++] = j;
                vis[i][j] = 0;
                vn++;
                
                dfscheck(i, j);
                if (found) break;
                
                bn--;
                vis[i][j] = -1;
                vn--;
                
                //printf ("yes: %d\n", vn);
                
            }
            if (found) break;
        }
        if (found)
        {
//            for (i=0; i<N; i++)
//            {
//                for (j=0; j<M; j++)
//                {
//                    if (bx[0]==i && by[0]==j) printf ("c");
//                    else if (vis[i][j]==-1)
//                        printf (".");
//                    else
//                        printf ("*");
//                }
//                printf ("\n");
//            }
        }
        else printf ("Impossible\n");
    }
    //cout << "end" << endl;
    return 1;
}







