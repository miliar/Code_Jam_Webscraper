//
//  main.cpp
//  GoogleJam
//
//  Created by Alexandre Decuq on 24/03/14.
//  Copyright (c) 2014 Alexandre Decuq. All rights reserved.
//

#include "main.h"

#include <vector>
#include <set>
#include <map> ///set_intersection()
#include <queue>
#include <algorithm>
#include <stdio.h>
#include <iostream>
#include <string>  ///memset
#include <cstring>
#include <cassert>
#include <iomanip> ///setprecision()
#include <cmath> ///ceil() or floor()
#include <climits> ///INT_MAX

using namespace std; ///std::to_string(int)

int dp[1002];

int computeMid(int y) {
    int mid;
    if(y%2==0) mid = y/2; ///even
    else mid = (y/2)+1; ///odd
    return mid;
}

int computeMinimum(int y) {
    int mid = computeMid(y);
    int res = y;
    for(int j=y-1;j>=mid;--j) {
        int i = y - j;
        res = min( res, max( dp[i], dp[j] ) +1 );
    }
    dp[y] = res;
}

void displayVector(vector<int> P) {
    for(int i=0;i<P.size();++i)
        cout <<P[i]<<",";
    cout << endl;
}

int computeTotalCost(vector<int> P) {
    int res=0;
    for(int i=0;i<P.size();++i)
        res+=dp[P[i]];
    return res;
}

int main()
{
    /** INITIALIZATION */
    FILE *fp = freopen("/home/alex/Projects/googlecodejam/D-small-attempt14.in", "r", stdin); //small-attempt1
    freopen("/home/alex/Projects/googlecodejam/D-small-attempt14.out", "w", stdout);
    if(fp==0) cout <<"ERROR reading input file" << endl;

    /** BEGIN ALGORITHM */
    int T;
    cin>> T; /// T test cases follow

    for(int t=1; t<=T; t++)
    {
        int X, R, C;
        cin >> X;
        cin >> R;
        cin >> C;

        string res;
        switch(X) { ///GABRIEL DOIT FILL !!! et RICHARD PIEGE GABRIEL
            case(1):
                res="GABRIEL";                      ///toutes les matrices
                break;

            case(2):
                if( (R*C)%2==1 )                    ///matrice taille impaire
                    res="RICHARD";
                else
                    res="GABRIEL";
                break;

            case(3):
                if(R==1||C==1) {
                    /*if(C==3||R==3)
                        res="GABRIEL";               ///matrice 1*3
                    else*/
                        res="RICHARD";               ///matrice 1*1, 1*2 ou 1*4
                }
                else if((R==2&&C==3) ||(R==3&&C==2)) ///matrice 2*3
                    res="GABRIEL";
                else if(C==3||R==3)                  ///matrice 3*3 et 3*4
                    res="GABRIEL";
                else
                    res="RICHARD";                   ///matrice 2*2, 2*4 et 4*4
                break;

            case(4):
                if(R==1||C==1) {
                    /*if(C==4||R==4)
                        res="GABRIEL";              ///matrice 1*4
                    else*/
                        res="RICHARD";              ///matrice 1*1, 1*2 ou 1*3
                }
                else if((R==3&&C==4) ||(R==4&&C==3))///matrice 3*4
                    res="GABRIEL";
                else if(R==4&&C==4)                 ///matrice 4*4
                    res="GABRIEL";
                else if(R==2&&C==2)                 ///matrice 2*2
                    res="RICHARD";
                else                                ///matrice 2*3, 2*4 et 3*3
                    res="RICHARD";
                break;
        }

        cout << "Case #" << t << ": " << res <<"\n";
    }
    /** END ALGORITHM */
}

































