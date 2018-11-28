//
//  main.cpp
//  Fractiles
//
//  Created by Nabil SHF on 4/9/16.
//  Copyright © 2016 Nabil SHF. All rights reserved.
//

#include <iostream>
#include <cstdio>
using namespace std;

int main(){
    int t;
    int k, c, s;
    scanf ("%d",&t);
    for (int l=1; l<=t; ++l){
        scanf ("%d %d %d",&k,&c,&s);
        printf ("Case #%d:",l);
        
        if (c==1){
            if (s<k) printf (" IMPOSSIBLE\n");
            else{
                for (int i=1;i<=k;++i) printf (" %d",i);
                printf ("\n");
            }
        }
        else{
            if (k==1){
                if (s>=1) printf (" 1\n");
                else printf ("IMPOSSIBLE\n");
            }
            else {
                int sol = 2;
                if (s >= k-1){
                    for (int i=1;i<k;++i){
                        printf (" %d",sol);
                        sol += (k+1);
                    }
                    printf ("\n");
                }
                else printf (" IMPOSSIBLE\n");
            }
        }
    }
    
    return 0;
}