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

int maxNumber(int count[], int N)
{
    int maxNum = count[0];
    for (int i = 1; i < N; i++)
    {
        maxNum = max(maxNum, count[i]);
    }
    return maxNum;
}
//Senate Evacuation
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
        int N;
        int count[27] = {0};
        string result = "";
        input >> N;
        int total = 0;
        for (int i = 0; i < N; i++)
        {
            input >> count[i];
            total += count[i];
        }
        while (total != 0)
        {
            int maxNum = count[0];
            int maxIndex1 = 0;
            int maxIndex2 = 0;
            for (int i = 1; i < N; i++)
            {
                if (maxNum <= count[i])
                {
                    if (maxNum < count[i])
                    {
                        maxNum = count[i];
                        maxIndex1 = i;
                        maxIndex2 = i;
                    }
                    else // ==
                    {
                        maxIndex2 = i;
                    }
                }
            }
            
            if (maxIndex1 == maxIndex2)
            {
                if (total == 3)
                {
                    total -= 1;
                    result += string(1, maxIndex1 + 'A');
                    count[maxIndex1]-= 1;
                }
                else
                {
                    total -= 2;
                    result += string(1, maxIndex1 + 'A');
                    result += string(1, maxIndex2 + 'A');
                    count[maxIndex1]-= 2;
                }
            }
            else
            {
                if (total == 3)
                {
                    total -= 1;
                    result += string(1, maxIndex1 + 'A');
                    count[maxIndex1]-= 1;
                }
                else
                {
                    total -= 2;
                    result += string(1, maxIndex1 + 'A');
                    result += string(1, maxIndex2 + 'A');
                    count[maxIndex1]--;
                    count[maxIndex2]--;
                }
            }
            if (total != 0)
            {
                result += " ";
            }
        }
        
        output << "Case #" << t << ": " << result << endl;
    }
    
    
    input.close();
    return 0;
}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
