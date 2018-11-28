//
//  main.cpp
//  GoogleCodeJam
//
//  Created by Kasi Chonpimai on 4/13/56 BE.
//  Copyright (c) 2556 smiled0gz. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <cstdlib>

int tab[200][200];
int mrow[200] = {0};
int mcol[200] = {0};
int n, m;
int nQ;

int main(int argc, const char * argv[])
{
    //freopen("input", "r", stdin);
    //freopen("/Users/2hpwrrbm/Temp/codejam/GoogleCodeJam/output", "w", stdout);
    //system("pwd");
    scanf("%d",&nQ);
    
    for (int xx=0; xx<nQ; xx++) {
        //printf("%d ",xx);
        bool check = true;
        scanf("%d%d",&n,&m);
        for(int i=0;i<n;i++)for(int j=0;j<m;j++){
            scanf("%d",&tab[i][j]);
            //printf("(%d %d) %d\n",i,j, tab[i][j]);
        }
        for(int i=0;i<n;i++){
            int mx = 0;
            for(int j=0;j<m;j++){
                if(mx<tab[i][j]) mx=tab[i][j];
            }
            mrow[i] = mx;
        }
        for(int j=0;j<m;j++){
            int mx = 0;
            for(int i=0;i<n;i++){
                if(mx<tab[i][j]) mx=tab[i][j];
            }
            mcol[j] = mx;
        }
        for(int i=0;i<n;i++)for(int j=0;j<m;j++){
            if(tab[i][j]!=mrow[i] && tab[i][j]!=mcol[j]) {
                check = false;
                //printf("%d [%d %d][%d] (%d %d)\n",xx,i,j,tab[i][j],mrow[i],mcol[j]);
            }
        }
        if(check) printf("Case #%d: YES\n", xx+1);
        else printf("Case #%d: NO\n", xx+1);
    }
    
}

