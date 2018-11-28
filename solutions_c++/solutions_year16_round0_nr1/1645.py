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

using namespace std;

//Counting Sheep
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
        long long n;
        long long N = 0;
        input >> n;
        
        int arrCount[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0 , 0} ;
        long long result = 0;
        bool check = true;
        bool INSOMNIA = false;
        int index = 0;
        long long maxLong = 1000000000000000;
        int count = 0;
        
        while (check && !INSOMNIA)
        {
            index++;
            N = n * index;
            string NString;
            NString = to_string(N);
            //check insonima here
            if (N == 0)
            {
                INSOMNIA = true;
                break;
            }
            
            for (int i = 0; i < NString.length(); i++) {
                if (arrCount[NString[i] - '0'] == 0)
                {
                    arrCount[NString[i] - '0']++;
                    count++;
                }
            }
            if (count == 10 || N > maxLong)
            {
                check = false;
            }
        }
        result = N;
        
        if (INSOMNIA)
            output << "Case #" << t << ": " << "INSOMNIA" << endl;
        else
            output << "Case #" << t << ": " << result << endl;
    }
    
    
    input.close();
    return 0;
}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////