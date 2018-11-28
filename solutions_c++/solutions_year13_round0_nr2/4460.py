//
//  codejamA.cpp
//  trycpp
//
//  Created by Tarun Goyal on 13/04/13.
//  Copyright (c) 2013 Tarun Goyal. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
    FILE *fin = fopen("codejamBinput.txt", "r");
    FILE *fout = fopen("codejamBoutput.txt", "w");
    int t;
    fscanf(fin,"%d",&t);
    for (int I=1; I<=t; I++) {
        int N,M;
        fscanf(fin, "%d%d", &N,&M);
        int **a = new int*[N];
        for (int i=0; i<N; i++) {
            a[i] = new int[M];
            for (int j=0;j<M; j++) {
                fscanf(fin, "%d",&a[i][j]);
            }
        }
        int *rw = new int[N];
        int *clmn = new int[M];
        for (int i=0; i<N; i++) {
            rw[i] = 0;
        }
        for (int i=0; i<M; i++) {
            clmn[i] = 0;
        }
        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                rw[i] = max(rw[i],a[i][j]);
                clmn[j] = max(clmn[j],a[i][j]);
            }
        }
        bool b = 1;
        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                if (a[i][j]!=rw[i]&&a[i][j]!=clmn[j]) {
                    b=0;
                    break;
                }
            }
            if (!b) {
                break;
            }
        }
        if (b) {
            fprintf(fout, "Case #%d: YES\n",I);
        }
        else
        {
            fprintf(fout, "Case #%d: NO\n",I);
        }
    }
    fclose(fin);
    fclose(fout);
    return 0;
}
