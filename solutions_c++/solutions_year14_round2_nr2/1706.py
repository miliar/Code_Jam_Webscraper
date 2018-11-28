//
//  main.cpp
//
//  Created by Xiaowei Ma.
//  Copyright (c) 2014 Xiaowei Ma. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>
#include <string>
#include <cmath>
#include <iomanip>

using namespace std;


int main()
{
    //--------------- I/O ---------------------------------
    ifstream in;
    in.open("/Users/xiaoweima/Desktop/CodeJam/in");

    ofstream out;
    out.open("/Users/xiaoweima/Desktop/CodeJam/out");


    int T;
    in>>T;

    //-------------  sovle  ------------------------------

    for (int ca = 1; ca <= T; ca++)
    {
        int a, b, k;
        in>>a>>b>>k;

        long long int ans = 0;

        for (int i = 0; i < a; i++)
        {
            for (int j = 0; j < b; j++)
            {
                int key = i&j;
                if (key < k)
                    ans++;
            }
        }

        out<<"Case #"<<ca<<": "<<ans<<endl;
    }




    //------------  finishing  -----------------------------
    in.close();
    out.close();
    return 0;
}



