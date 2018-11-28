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

bool check(vector<bool>&tab, int M) {
    char X[20]; sprintf(X, "%lld", M);
    string S = X;
    //update
    for(int i=0;i<S.size();++i) {
        char l = S[i];
        int num = atoi(&l);
        tab[num] = true;
    }
    //check
    for(int i=0;i<10;++i) {
        if(tab[i]==false)
            return false;
    }
    return true;
}

int main()
{
    /** INITIALIZATION */
    FILE *fp = freopen("/home/alex/Projects/googlecodejam/A-large.in", "r", stdin); //small-attempt2
    freopen("/home/alex/Projects/googlecodejam/A-large.out", "w", stdout);
    if(fp==0) cout <<"ERROR reading input file" << endl;

    /** BEGIN ALGORITHM */
    int T;
    cin>> T; /// T test cases follow
    vector<bool> tab;

    int R = 40000;

    for(int t=1; t<=T; t++)
    {
        int N;
        cin >> N;
        tab = vector<bool>(10,false);
        bool checker = check(tab,N);
        int i = 2;
        int M;
        while(!checker) {
            M = N * i;
            if(i > R)
                break;
            checker = check(tab,M);
            i++;
        }

        cout << "Case #"<<t<<": ";
        if(i > R)
            cout<< "INSOMNIA"<< endl;
        else
            cout << M << endl;

    }
    /** END ALGORITHM */
}


