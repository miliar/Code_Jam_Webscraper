//
//  main.cpp
//  codejam
//
//  Created by Stephen Zhu on 4/11/14.
//  Copyright (c) 2014 Stephen Zhu. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <algorithm>
#include <cmath>

using namespace std;

#define tr(i, end) \
for (int i = 0; i < end; ++i)


int main()
{
    
    ifstream ins("B-large.in");
    FILE * out;
    out = fopen("B-large.out", "w");
    
    int T;
    ins >> T;
    tr(i, T){
        fprintf(out, "Case #%i: ", i+1);
        double x,c,f;
        ins >> c >> f >> x;
        int numfarms = ceil(x/c - 2/f - 1);
        numfarms = max(numfarms, 0);
        
        double time = 0;
        tr(i, numfarms) time += (1.0/(2.0+f*i));
        time = time*c + x/(2+f*numfarms);
        fprintf(out, "%.7f\n", time);
    }
        
    return 0;
}



