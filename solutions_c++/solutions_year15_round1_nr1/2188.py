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


int main()
{
    /** INITIALIZATION */
    FILE *fp = freopen("/home/alex/Projects/googlecodejam/A-large.in", "r", stdin); //small-attempt6
    freopen("/home/alex/Projects/googlecodejam/A-large.out", "w", stdout);
    if(fp==0) cout <<"ERROR reading input file" << endl;

    /** BEGIN ALGORITHM */
    int T;
    cin>> T; /// T test cases follow

    for(int t=1; t<=T; t++)
    {
        int N;
        cin >> N;
        vector<int> mush;
        for(int i=0;i<N;++i) {
            int Ni;
            cin >> Ni;
            mush.push_back(Ni);
        }

        /// first method
        int sum1 = 0;
        for(size_t i=1;i<mush.size();++i) {
            if(mush[i]<mush[i-1])
                sum1 += mush[i-1] - mush[i];
        }

        /// second method
        int max_diff = 0;
        for(size_t i=1;i<mush.size();++i) {
            if(mush[i]<mush[i-1]) {
                if(mush[i-1] - mush[i] > max_diff)
                    max_diff = mush[i-1] - mush[i];
            }
        }
        int sum2 = 0;
        if(max_diff != 0)
        {
            for(size_t i=1;i<mush.size();++i) {
                    sum2 += min(mush[i-1], max_diff);
            }
        }

        cout << "Case #" << t << ": " << sum1 <<" " << sum2 <<"\n";
    }
    /** END ALGORITHM */
}

































