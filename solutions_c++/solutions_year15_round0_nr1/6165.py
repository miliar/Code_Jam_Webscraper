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

long long a, b;

int main()
{
    /** INITIALIZATION */
    FILE *fp = freopen("/home/alex/Projects/googlecodejam/A-large.in", "r", stdin);
    freopen("/home/alex/Projects/googlecodejam/A-large.out", "w", stdout);
    if(fp==0) cout <<"ERROR reading input file" << endl;

    /** BEGIN ALGORITHM */
    int T;
    cin>> T; /// T test cases follow

    for(int t=1; t<=T; t++)
    {
        int shiest;
        cin >> shiest;

        string tmp;
        cin >> tmp;

        /** for hard problem */

        int cum=int(tmp[0])-48;
        int tt_missing=0;
        for(int i=1;i<tmp.size();++i) {
            //cout << "cum("<<cum<<")" << " < i="<<i<<"? \n";
            if(cum<i) { ///missing some people
                tt_missing+=i-cum;
                cum+=i-cum; ///adding current missing
            }

            int current = int(tmp[i])-48;
            cum+=current;
        }

        cout << "Case #" << t << ": " << tt_missing<<"\n";
    }
    /** END ALGORITHM */
}

































