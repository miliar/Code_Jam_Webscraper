//
//  main.cpp
//  googleJam
//
//  Created by Nguyen Viet Trung on 3/29/16.
//  Copyright © 2016 Nguyen Viet Trung. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <istream>
#include <string>
#include <sstream>
#include <algorithm>    // std::set_intersection, std::sort
#include <vector>       // std::vector
#include <iomanip>
#include <math.h>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <list>
#include <complex>
#include <stack>
#include <cmath>
#include <iostream>
#include <sstream>
#include <cctype>
#include <cstdlib>
#include <utility>
#include <bitset>
#include <assert.h>
#include <stdio.h>      /* printf, NULL */
#include <stdlib.h>

using namespace std;


//Fractiles
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
int main(int argc, const char * argv[]) {
    // insert code here...
    ifstream input;
    input.open("input.txt");
    
    ofstream output;
    output.open("output.txt");
    int T;
    input >> T;
    for (int t = 1; t <= T; t++) {
        vector<int>result;
        int K ,C, S;
        input >> K >> C >> S;
        bool IMPOSSIBLE = false;
        if (S < K && C == 1)
            IMPOSSIBLE = true;
        
//        if (C == 1 && S == K)
//        {
            for (int i = 1; i <= S; i++) {
                result.push_back(i);
            }
//        }
        if (IMPOSSIBLE)
        {
            output << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
        }
        else
        {
            output << "Case #" << t << ": ";
            for (int i = 0; i < result.size(); i++) {
                output << result[i] << " ";
            }
            output << endl;
        }
    }
    
    
    input.close();
    return 0;
}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////