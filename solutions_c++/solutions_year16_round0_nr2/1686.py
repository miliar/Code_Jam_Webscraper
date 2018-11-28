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

//Revenge of the Pancakes
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
        string S;
        
        input >> S;
        long SLength = S.length();
        long long result = 0;
        
        while (SLength > 0)
        {
            long index = 0;
            while (S[SLength - 1] == '+')
            {
                SLength--;
                if (SLength <= 0)
                    break;
            }
            if (SLength <= 0)
                break;
            
            if (S[0] == '+')
            {
                for (int i = 1; i < SLength; i++) {
                    if (S[i] == '-')
                        break;
                    index = i;
                }
            }
            else
                index = SLength - 1;
            string copyString = S.substr(0, index + 1);
            //flip
            for (int i = 0; i <= index; i++) {
                if (copyString[i] == '-')
                {
                    S[index - i] = '+';
                }
                else if (copyString[i] == '+')
                    S[index - i] = '-';
            }
            result++;
        }
        output << "Case #" << t << ": " << result << endl;
    }
    
    
    input.close();
    return 0;
}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////